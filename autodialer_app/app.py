from flask import Flask, render_template, request, jsonify, send_file
from twilio.rest import Client
# Try to import Twilio's VoiceResponse/Say; if unavailable, provide a minimal fallback
import importlib
try:
    _twilio_module = importlib.import_module('twilio.twiml.voice_response')
    VoiceResponse = getattr(_twilio_module, 'VoiceResponse')
    Say = getattr(_twilio_module, 'Say')
    _TWILIO_AVAILABLE = True
except Exception:
    _TWILIO_AVAILABLE = False
    class VoiceResponse:
        def __init__(self):
            self._parts = []
        def append(self, part):
            self._parts.append(str(part))
        def pause(self, length=1):
            self._parts.append(f'<Pause length="{length}"/>')
        def say(self, text, voice=None, language=None):
            # voice and language ignored in fallback
            self._parts.append(f'<Say>{text}</Say>')
        def __str__(self):
            return '<?xml version="1.0" encoding="UTF-8"?><Response>' + ''.join(self._parts) + '</Response>'
    class Say:
        def __init__(self, text, voice=None, language=None):
            self._text = text
            self._voice = voice
            self._language = language
        def __str__(self):
            return f'<Say>{self._text}</Say>'
import os
import csv
import json
from datetime import datetime
import re

app = Flask(__name__)

# Twilio Configuration (set these in environment variables or config)
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', '')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', '')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER', '')

# Initialize Twilio client
twilio_client = None
if TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN:
    twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# In-memory storage for call logs
call_logs = []

class CallLog:
    def __init__(self, phone_number, status, message):
        self.phone_number = phone_number
        self.status = status
        self.message = message
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.call_sid = None
        self.duration = 0

def parse_ai_command(command):
    """Parse natural language commands for making calls"""
    command = command.lower().strip()
    
    # Pattern: "call <number>"
    patterns = [
        r'call\s+(\+?\d[\d\s\-\(\)]+)',
        r'dial\s+(\+?\d[\d\s\-\(\)]+)',
        r'phone\s+(\+?\d[\d\s\-\(\)]+)',
        r'make\s+a\s+call\s+to\s+(\+?\d[\d\s\-\(\)]+)',
        r'ring\s+(\+?\d[\d\s\-\(\)]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, command)
        if match:
            # Clean the phone number
            number = match.group(1).replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
            return number
    
    return None

def make_call(to_number, message="Hello, this is an automated call from the Autodialer system."):
    """Make a call using Twilio"""
    if not twilio_client:
        log = CallLog(to_number, "Failed", "Twilio not configured")
        call_logs.append(log)
        return {"success": False, "error": "Twilio credentials not configured"}
    
    try:
        # Create TwiML for the call
        twiml_url = request.url_root + 'voice?message=' + message
        
        call = twilio_client.calls.create(
            to=to_number,
            from_=TWILIO_PHONE_NUMBER,
            url=twiml_url,
            status_callback=request.url_root + 'call-status',
            status_callback_event=['initiated', 'ringing', 'answered', 'completed']
        )
        
        log = CallLog(to_number, "Initiated", message)
        log.call_sid = call.sid
        call_logs.append(log)
        
        return {"success": True, "call_sid": call.sid, "status": "initiated"}
    
    except Exception as e:
        log = CallLog(to_number, "Failed", str(e))
        call_logs.append(log)
        return {"success": False, "error": str(e)}

@app.route('/')
def index():
    """Main dashboard"""
    return render_template('index.html')

@app.route('/api/call/single', methods=['POST'])
def call_single():
    """Make a single call"""
    data = request.json
    phone_number = data.get('phone_number')
    message = data.get('message', 'Hello, this is an automated call.')
    
    if not phone_number:
        return jsonify({"success": False, "error": "Phone number required"}), 400
    
    result = make_call(phone_number, message)
    return jsonify(result)

@app.route('/api/call/bulk', methods=['POST'])
def call_bulk():
    """Make multiple calls"""
    data = request.json
    phone_numbers = data.get('phone_numbers', [])
    message = data.get('message', 'Hello, this is an automated call.')
    
    if not phone_numbers:
        return jsonify({"success": False, "error": "Phone numbers required"}), 400
    
    results = []
    for number in phone_numbers:
        result = make_call(number.strip(), message)
        results.append({"number": number, "result": result})
    
    return jsonify({"success": True, "results": results})

@app.route('/api/call/ai-command', methods=['POST'])
def ai_command():
    """Process AI natural language command"""
    data = request.json
    command = data.get('command', '')
    message = data.get('message', 'Hello, this is an automated call.')
    
    phone_number = parse_ai_command(command)
    
    if not phone_number:
        return jsonify({
            "success": False, 
            "error": "Could not understand the command. Try: 'call +91XXXXXXXXXX'"
        }), 400
    
    result = make_call(phone_number, message)
    result['parsed_number'] = phone_number
    return jsonify(result)

@app.route('/api/upload-csv', methods=['POST'])
def upload_csv():
    """Upload CSV file with phone numbers"""
    if 'file' not in request.files:
        return jsonify({"success": False, "error": "No file uploaded"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"success": False, "error": "No file selected"}), 400
    
    if not file.filename.endswith('.csv'):
        return jsonify({"success": False, "error": "File must be CSV"}), 400
    
    try:
        # Read CSV
        content = file.read().decode('utf-8')
        csv_reader = csv.reader(content.splitlines())
        
        phone_numbers = []
        for row in csv_reader:
            if row and row[0].strip():
                phone_numbers.append(row[0].strip())
        
        return jsonify({"success": True, "phone_numbers": phone_numbers, "count": len(phone_numbers)})
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/logs')
def get_logs():
    """Get call logs"""
    logs_data = [{
        "phone_number": log.phone_number,
        "status": log.status,
        "message": log.message,
        "timestamp": log.timestamp,
        "call_sid": log.call_sid,
        "duration": log.duration
    } for log in call_logs]
    
    return jsonify({"logs": logs_data})

@app.route('/api/stats')
def get_stats():
    """Get call statistics"""
    total = len(call_logs)
    successful = len([log for log in call_logs if log.status in ['Initiated', 'Completed', 'Answered']])
    failed = len([log for log in call_logs if log.status == 'Failed'])
    in_progress = len([log for log in call_logs if log.status in ['Ringing', 'In Progress']])
    
    return jsonify({
        "total": total,
        "successful": successful,
        "failed": failed,
        "in_progress": in_progress
    })

@app.route('/voice')
def voice():
    """TwiML response for voice calls"""
    message = request.args.get('message', 'Hello, this is an automated call.')
    
    response = VoiceResponse()
    
    # Use AI voice with proper settings
    say = Say(
        message,
        voice='Polly.Kajal',  # Indian female voice
        language='en-IN'
    )
    response.append(say)
    
    # Add a pause
    response.pause(length=1)
    
    # Optional: Add another message
    response.say('Thank you for your time. Goodbye!', voice='Polly.Kajal', language='en-IN')
    
    return str(response), 200, {'Content-Type': 'text/xml'}

@app.route('/call-status', methods=['POST'])
def call_status():
    """Webhook for call status updates"""
    call_sid = request.form.get('CallSid')
    call_status = request.form.get('CallStatus')
    duration = request.form.get('CallDuration', 0)
    
    # Update log
    for log in call_logs:
        if log.call_sid == call_sid:
            log.status = call_status
            log.duration = int(duration)
            break
    
    return '', 200

@app.route('/export-logs')
def export_logs():
    """Export logs as CSV"""
    # Create CSV in memory
    import io
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['Timestamp', 'Phone Number', 'Status', 'Message', 'Call SID', 'Duration'])
    
    # Write data
    for log in call_logs:
        writer.writerow([
            log.timestamp,
            log.phone_number,
            log.status,
            log.message,
            log.call_sid or 'N/A',
            log.duration
        ])
    
    # Create response
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'call_logs_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    )


@app.route('/health')
def health():
    return jsonify({"status": "ok", "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}), 200

if __name__ == '__main__':
    print("=" * 60)
    print("Autodialer App Starting...")
    print("=" * 60)
    if not twilio_client:
        print("WARNING: Twilio credentials not configured!")
        print("Set TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_PHONE_NUMBER")
    port = int(os.environ.get('PORT', 5000))
    host = '0.0.0.0'
    print(f"Access the app at: http://{host}:{port} or http://localhost:{port}")
    print("=" * 60)
    debug_mode = os.environ.get('FLASK_ENV', 'development') != 'production'
    app.run(debug=debug_mode, host=host, port=port)
