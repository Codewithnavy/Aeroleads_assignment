# Autodialer App - AI-Powered Automated Calling System

A Flask-based web application for making automated phone calls using Twilio API with AI natural language command support.

## Features

- **AI Voice Commands**: Natural language processing for call commands
  - "call +91XXXXXXXXXX"
  - "dial 1800123456"
  - "make a call to +911234567890"

- **Multiple Input Methods**:
  - Single call interface
  - Bulk calls (paste multiple numbers)
  - CSV file upload

- **AI Voice Integration**: Uses Amazon Polly AI voices (Indian English)

- **Real-time Dashboard**:
  - Total calls, successful, failed, in-progress stats
  - Live call logs with timestamps
  - Call status tracking
  - Duration monitoring

- **Call Logging**:
  - Complete call history
  - Export logs to CSV
  - Real-time status updates via webhooks

## Technology Stack

- **Backend**: Python Flask
- **Telephony**: Twilio API
- **AI Voice**: Amazon Polly (via Twilio)
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Storage**: In-memory (can be extended to database)

## Setup Instructions

### Prerequisites

1. Python 3.8 or higher
2. A Twilio account (Free trial available at [twilio.com](https://www.twilio.com))
3. Twilio phone number (provided with free trial)

### Twilio Setup

1. Sign up at [https://www.twilio.com/try-twilio](https://www.twilio.com/try-twilio)
2. Get your Account SID and Auth Token from the console
3. Get a Twilio phone number (Voice-enabled)
4. For testing, use verified numbers or 1800 toll-free numbers

### Installation

1. Navigate to the autodialer_app directory:
```bash
cd autodialer_app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
# Copy the example file
cp .env.example .env

# Edit .env with your credentials
TWILIO_ACCOUNT_SID=your_actual_sid
TWILIO_AUTH_TOKEN=your_actual_token
TWILIO_PHONE_NUMBER=your_twilio_number
```

On Windows PowerShell:
```powershell
$env:TWILIO_ACCOUNT_SID="your_actual_sid"
$env:TWILIO_AUTH_TOKEN="your_actual_token"
$env:TWILIO_PHONE_NUMBER="your_twilio_number"
```

### Running the Application

```bash
python app.py
```

The application will start at `http://localhost:5000`

## Usage Guide

### 1. AI Voice Commands

The most intuitive way to make calls:

1. Type a natural language command in the AI prompt box
2. Examples:
   - "call +918001234567"
   - "dial 1800123456"
   - "make a call to +911234567890"
3. Click "Execute Command"

The AI will parse your command, extract the phone number, and initiate the call.

### 2. Single Call

1. Click on "Single Call" tab
2. Enter phone number (e.g., +91XXXXXXXXXX or 1800XXXXXX)
3. Customize the message to be spoken
4. Click "Make Call"

### 3. Bulk Calls

1. Click on "Bulk Calls" tab
2. Enter phone numbers (one per line)
3. Customize the message
4. Click "Make All Calls"

**Note**: For testing, use 1800 toll-free numbers to avoid calling real people.

### 4. CSV Upload

1. Click on "Upload CSV" tab
2. Prepare a CSV file with phone numbers in the first column
3. Click to upload
4. Review the loaded numbers
5. Customize message and click "Call All Numbers"

### Sample CSV Format:
```csv
1800123456
1800234567
1800345678
```

## Features Explained

### AI Natural Language Processing

The app uses regex patterns to understand various call commands:
- "call \<number\>"
- "dial \<number\>"
- "phone \<number\>"
- "make a call to \<number\>"
- "ring \<number\>"

### AI Voice Configuration

Uses Amazon Polly's "Kajal" voice (Indian English female):
```python
Say(message, voice='Polly.Kajal', language='en-IN')
```

Available voices:
- Polly.Kajal (Indian Female)
- Polly.Aditi (Indian Female)
- Polly.Raveena (Indian Female)

### Call Status Tracking

The app tracks calls through Twilio webhooks:
- **Initiated**: Call request sent
- **Ringing**: Phone is ringing
- **Answered**: Call was picked up
- **Completed**: Call ended
- **Failed**: Call couldn't connect

### Statistics Dashboard

Real-time metrics:
- Total calls made
- Successful calls (initiated/answered/completed)
- Failed calls
- Calls in progress

## API Endpoints

### POST /api/call/single
Make a single call
```json
{
  "phone_number": "+918001234567",
  "message": "Custom message"
}
```

### POST /api/call/bulk
Make multiple calls
```json
{
  "phone_numbers": ["+918001234567", "+918009876543"],
  "message": "Custom message"
}
```

### POST /api/call/ai-command
Process AI command
```json
{
  "command": "call +918001234567",
  "message": "Custom message"
}
```

### GET /api/logs
Get call logs

### GET /api/stats
Get call statistics

### GET /export-logs
Download logs as CSV

## Testing Recommendations

**IMPORTANT**: For testing, use these types of numbers:

1. **Toll-Free Numbers**: 1800XXXXXX (India)
2. **Twilio Test Numbers**: Provided in Twilio console
3. **Your Own Verified Numbers**: Add in Twilio console

**DO NOT** call random real people during testing!

### Sample Safe Test Numbers (1800):
- 1800-180-1551 (Common toll-free format)
- Use directory assistance or customer service numbers
- Your own mobile number (verified in Twilio)

## Deployment

### Free Hosting Options

1. **Heroku** (Free tier):
   - Create `Procfile`: `web: python app.py`
   - Add buildpack: `heroku/python`
   - Set environment variables in Heroku dashboard

2. **Render** (Free tier):
   - Connect GitHub repo
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `python app.py`
   - Add environment variables

3. **PythonAnywhere** (Free tier):
   - Upload code
   - Configure WSGI
   - Set environment variables

4. **Railway** (Free tier):
   - Connect GitHub
   - Auto-detects Flask
   - Add environment variables

### For Production

Set environment variables:
```bash
export FLASK_ENV=production
export TWILIO_ACCOUNT_SID=your_sid
export TWILIO_AUTH_TOKEN=your_token
export TWILIO_PHONE_NUMBER=your_number
```

## File Structure

```
autodialer_app/
├── app.py                  # Main Flask application
├── templates/
│   └── index.html         # Frontend interface
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## Troubleshooting

### Twilio Not Configured Error
- Ensure environment variables are set correctly
- Restart the application after setting variables

### Calls Not Going Through
- Verify Twilio account is active
- Check if phone numbers are in correct format (+91XXXXXXXXXX)
- Ensure you have Twilio credits
- For trial accounts, verify the destination number in Twilio console

### Webhook Issues
- If using localhost, use ngrok for webhooks: `ngrok http 5000`
- Update Twilio webhook URLs to ngrok URL

### Voice Not Playing
- Check Twilio TwiML logs in console
- Verify voice parameter is correct
- Ensure message text is not empty

## Cost Considerations

### Twilio Free Trial:
- $15.50 USD credit
- Can make ~500 calls (depending on duration)
- Must verify numbers first

### Twilio Pricing (Paid):
- Outbound calls: ~$0.01-0.02 per minute
- Phone number: ~$1/month
- Very affordable for small-scale use

## Security Notes

- Never commit `.env` file with real credentials
- Use environment variables for production
- Implement rate limiting for production use
- Add authentication for production deployment
- Validate phone numbers before calling

## Future Enhancements

- Database integration (PostgreSQL/MongoDB)
- User authentication
- Schedule calls for later
- Call recording
- SMS integration
- Multiple language support
- Call scripts with interactive menus
- CRM integration
- Analytics dashboard
- Call quality monitoring

## Legal & Ethical Considerations

- Obtain consent before automated calling
- Comply with TCPA (US) / TRAI (India) regulations
- Don't call numbers on DND lists
- Provide opt-out mechanism
- Only use for legitimate business purposes
- This is an educational project - use responsibly

## License

Created for Aeroleads technical assignment. Use responsibly and ethically.

## Support

For Twilio-specific issues, check:
- [Twilio Documentation](https://www.twilio.com/docs)
- [Twilio Support](https://support.twilio.com)

For application issues, refer to the code comments or create an issue in the repository.
