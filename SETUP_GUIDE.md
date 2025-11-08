# Installation & Setup Guide

This guide will help you set up all three projects in the Aeroleads assignment.

## Prerequisites

Before starting, ensure you have:
- Python 3.8 or higher installed
- Chrome browser (for LinkedIn scraper)
- Git (for cloning the repository)
- A code editor (VS Code recommended)

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Codewithnavy/Aeroleads_assignment.git
cd Aeroleads_assignment
```

### 2. LinkedIn Scraper Setup

```bash
cd linkedin_scraper

# Install dependencies
pip install -r requirements.txt

# Configure LinkedIn credentials
# Open scraper.py and update:
# LINKEDIN_EMAIL = 'your-test-email@gmail.com'
# LINKEDIN_PASSWORD = 'your-test-password'

# Run the scraper
python scraper.py
```

**Output**: `linkedin_profiles.csv` with scraped data

### 3. Autodialer App Setup

```bash
cd ../autodialer_app

# Install dependencies
pip install -r requirements.txt

# Set up Twilio credentials
# Option 1: Using PowerShell (Windows)
$env:TWILIO_ACCOUNT_SID="your_account_sid"
$env:TWILIO_AUTH_TOKEN="your_auth_token"
$env:TWILIO_PHONE_NUMBER="your_twilio_number"

# Option 2: Create .env file
# Copy .env.example to .env and fill in your credentials

# Run the application
python app.py
```

**Access**: http://localhost:5000

**Getting Twilio Credentials**:
1. Sign up at https://www.twilio.com/try-twilio
2. Get your Account SID and Auth Token from the dashboard
3. Get a free phone number from Twilio

### 4. Blog Generator Setup

```bash
cd ../blog_generator

# Install dependencies
pip install -r requirements.txt

# API key is already configured, but you can use your own
# Optional: Set your own Gemini API key
$env:GEMINI_API_KEY="your_api_key"

# Run the application
python app.py
```

**Access**: 
- Blog: http://localhost:5001/blog
- Admin: http://localhost:5001/blog/admin

**Getting Gemini API Key** (optional):
1. Go to https://ai.google.dev
2. Click "Get API Key"
3. Sign in and create a new key
4. Copy the key

## Testing the Applications

### LinkedIn Scraper
1. Ensure Chrome is installed
2. Update credentials in `scraper.py`
3. Run: `python scraper.py`
4. Check `linkedin_profiles.csv` for results

### Autodialer App
1. Open http://localhost:5000
2. Try AI command: "call 1800123456"
3. Or use single call interface
4. Check logs for call status

**IMPORTANT**: For testing, only call:
- Toll-free numbers (1800XXXXXX)
- Your own verified phone number
- Twilio test numbers

### Blog Generator
1. Open http://localhost:5001/blog
2. View 10 auto-generated articles
3. Go to `/blog/admin` to generate more
4. Try bulk generation with:
   ```
   1. Python Decorators
   2. REST API Design
   3. Docker Basics
   ```

## Common Issues & Solutions

### Issue: "Module not found"
**Solution**: Ensure you're in the correct directory and have run `pip install -r requirements.txt`

### Issue: Twilio credentials not working
**Solution**: 
- Verify credentials are correct
- Check if environment variables are set
- Restart the terminal after setting env vars

### Issue: LinkedIn scraper fails to login
**Solution**:
- Use a test LinkedIn account, not your main account
- Check if LinkedIn requires verification
- Try manual login first to ensure credentials work

### Issue: Gemini API errors
**Solution**:
- Check if API key is valid
- Ensure you haven't exceeded rate limits
- Verify internet connection

### Issue: ChromeDriver errors
**Solution**:
- Update Chrome browser
- webdriver-manager should auto-download correct driver
- Check if Chrome is in PATH

## Running Multiple Apps Simultaneously

Since the apps run on different ports, you can run all three at once:

1. **Terminal 1**: LinkedIn Scraper
   ```bash
   cd linkedin_scraper
   python scraper.py
   ```

2. **Terminal 2**: Autodialer (Port 5000)
   ```bash
   cd autodialer_app
   python app.py
   ```

3. **Terminal 3**: Blog Generator (Port 5001)
   ```bash
   cd blog_generator
   python app.py
   ```

## Project Structure Overview

```
Aeroleads_assignment/
├── linkedin_scraper/
│   ├── scraper.py              # Main script
│   ├── requirements.txt        # Dependencies
│   └── README.md              # Documentation
│
├── autodialer_app/
│   ├── app.py                 # Flask app
│   ├── templates/
│   │   └── index.html        # Dashboard
│   ├── requirements.txt       # Dependencies
│   ├── .env.example          # Config template
│   └── README.md             # Documentation
│
└── blog_generator/
    ├── app.py                 # Flask app
    ├── templates/
    │   ├── blog_index.html   # Blog home
    │   ├── blog_post.html    # Article page
    │   └── blog_admin.html   # Admin panel
    ├── requirements.txt       # Dependencies
    └── README.md             # Documentation
```

## Next Steps

1. **Test each application** to ensure it works
2. **Customize** as needed (add more profiles, articles, etc.)
3. **Deploy** to free hosting (Render, Railway, etc.)
4. **Create video** demonstrating the projects
5. **Submit** GitHub URL and video URL

## Support

For detailed information about each project, see the individual README files:
- [LinkedIn Scraper README](linkedin_scraper/README.md)
- [Autodialer README](autodialer_app/README.md)
- [Blog Generator README](blog_generator/README.md)

## Tips for Video Creation

1. **Introduction** (30 sec): Overview of all three projects
2. **LinkedIn Scraper** (1.5 min): Code walkthrough + demo
3. **Autodialer** (2 min): Explain features + live demo
4. **Blog Generator** (2 min): Show AI generation + blog
5. **Conclusion** (30 sec): Summary and deployment

Keep it concise, clear, and demonstrate understanding!
