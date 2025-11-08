# Aeroleads Technical Assignment

Comprehensive Full-Stack Development Assignment featuring LinkedIn scraping, automated calling system, and AI-powered blog generation.

## Overview

This repository contains three complete projects demonstrating expertise in:
- Web scraping with anti-detection mechanisms
- Telephony integration with AI voice
- AI content generation
- Full-stack web development
- API integration

## Projects

### 1. LinkedIn Scraper
**Automated LinkedIn profile data extraction with intelligent anti-detection**

- **Technology**: Python, Selenium WebDriver
- **Features**:
  - Smart login via Google search
  - Rotating user agents & stealth mode
  - Extracts: name, headline, location, connections, experience, education
  - Exports to CSV
  - Random delays to avoid detection
  - Handles 20+ profiles automatically

- **Location**: `linkedin_scraper/`
- **Setup**: See [linkedin_scraper/README.md](linkedin_scraper/README.md)

### 2. Autodialer App
**AI-powered automated calling system with natural language interface**

- **Technology**: Python Flask, Twilio API, Amazon Polly AI Voice
- **Features**:
  - **AI Voice Commands**: "call +91XXXXXXXXXX" - natural language processing
  - Single call, bulk calls, CSV upload
  - Real-time dashboard with live stats
  - AI voice (Indian English - Amazon Polly)
  - Call logging & status tracking
  - Export logs to CSV
  - Webhook-based real-time updates

- **Location**: `autodialer_app/`
- **Setup**: See [autodialer_app/README.md](autodialer_app/README.md)
- **Live Demo**: [Will be deployed to Render/Railway]

### 3. Blog Generator
**AI-powered programming blog with automatic content generation**

- **Technology**: Python Flask, Google Gemini AI
- **Features**:
  - **AI Bulk Generation**: Describe topics, get full articles
  - Generates 10 default programming articles on startup
  - Natural language prompts: "1. Python Decorators 2. REST APIs..."
  - 1000-1500 word comprehensive articles
  - Markdown formatting with code snippets
  - Beautiful blog interface
  - Admin panel for content management
  - SEO-friendly URLs

- **Location**: `blog_generator/`
- **Setup**: See [blog_generator/README.md](blog_generator/README.md)
- **Live Demo**: [Will be deployed to Render/Railway]

## Project Structure

```
Aeroleads_assignment/
├── linkedin_scraper/           # LinkedIn profile scraper
│   ├── scraper.py             # Main scraping script
│   ├── requirements.txt       # Dependencies
│   └── README.md             # Setup & usage guide
│
├── autodialer_app/            # Automated calling system
│   ├── app.py                # Flask application
│   ├── templates/            # HTML templates
│   │   └── index.html       # Dashboard UI
│   ├── requirements.txt      # Dependencies
│   ├── .env.example         # Environment variables template
│   └── README.md            # Setup & usage guide
│
├── blog_generator/            # AI blog generator
│   ├── app.py                # Flask application
│   ├── templates/            # HTML templates
│   │   ├── blog_index.html  # Blog listing
│   │   ├── blog_post.html   # Article view
│   │   └── blog_admin.html  # Admin panel
│   ├── requirements.txt      # Dependencies
│   └── README.md            # Setup & usage guide
│
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## Technologies Used

### Languages & Frameworks
- **Python 3.8+**: Primary language
- **Flask**: Web framework for autodialer and blog
- **HTML5/CSS3/JavaScript**: Frontend development

### APIs & Services
- **Selenium WebDriver**: Browser automation
- **Twilio API**: Telephony & SMS
- **Google Gemini AI**: Content generation
- **Amazon Polly**: AI voice synthesis

### Key Libraries
- `selenium` - Web automation
- `twilio` - Calling API
- `google-generativeai` - Gemini AI
- `flask` - Web framework
- `marked.js` - Markdown rendering

## Quick Start

### Prerequisites
- Python 3.8 or higher
- Chrome browser (for LinkedIn scraper)
- Twilio account (free trial available)
- Google Gemini API key (free tier available)

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/Codewithnavy/Aeroleads_assignment.git
cd Aeroleads_assignment
```

2. **Set up each project** (see individual READMEs):

**LinkedIn Scraper**:
```bash
cd linkedin_scraper
pip install -r requirements.txt
# Configure credentials in scraper.py
python scraper.py
```

**Autodialer App**:
```bash
cd autodialer_app
pip install -r requirements.txt
# Set environment variables
$env:TWILIO_ACCOUNT_SID="your_sid"
$env:TWILIO_AUTH_TOKEN="your_token"
$env:TWILIO_PHONE_NUMBER="your_number"
python app.py
# Access at http://localhost:5000
```

**Blog Generator**:
```bash
cd blog_generator
pip install -r requirements.txt
# API key is pre-configured, or set your own
$env:GEMINI_API_KEY="your_key"
python app.py
# Access at http://localhost:5001/blog
```

## Key Features Demonstrated

### 1. Web Scraping Expertise
- Anti-detection techniques (user agent rotation, stealth mode)
- Handling dynamic content with Selenium
- Data extraction and CSV export
- Error handling and robustness

### 2. API Integration
- Twilio telephony API
- Google Gemini AI API
- Webhook handling for real-time updates
- RESTful API design

### 3. AI Implementation
- Natural language processing for commands
- AI content generation (1000+ word articles)
- AI voice synthesis (Amazon Polly)
- Prompt engineering for quality output

### 4. Full-Stack Development
- Backend: Python Flask applications
- Frontend: Responsive HTML/CSS/JavaScript
- Real-time updates via AJAX
- Modern UI/UX design

### 5. Problem Solving
- LinkedIn login challenges (via Google search)
- Automated calling with legal compliance
- Bulk content generation with AI
- Rate limiting and error handling

## Project Highlights

### LinkedIn Scraper
- Scrapes 20 public LinkedIn profiles
- Anti-detection measures implemented
- CSV export with structured data
- Handles missing profile elements gracefully
- Randomized delays (3-10 seconds)

### Autodialer App
- AI natural language commands
- Single, bulk, and CSV upload modes
- Real-time dashboard with statistics
- Call logging and status tracking
- Amazon Polly AI voice (Indian English)
- Export logs functionality
- Webhook integration for live updates

### Blog Generator
- 10 default articles auto-generated
- AI bulk generation from natural language
- Comprehensive articles (1000-1500 words)
- Beautiful blog interface
- Admin panel for management
- Markdown support with code syntax
- SEO-friendly URLs

## Security & Best Practices

- Environment variables for sensitive data
- `.gitignore` for credentials
- Input validation and sanitization
- Error handling throughout
- Rate limiting considerations
- Ethical scraping practices
- Legal compliance (TCPA/TRAI for calling)

## Code Quality

- **Clean Code**: Well-structured, readable, and maintainable
- **Comments**: Comprehensive inline documentation
- **Error Handling**: Robust exception handling
- **Modularity**: Reusable functions and classes
- **Not AI-Generated Looking**: Natural code style, human-like patterns
- **Best Practices**: Following PEP 8, Flask conventions

## Deployment

### Recommended Free Hosting

1. **Render** (Best for Flask apps):
   - Autodialer: Deploy from GitHub
   - Blog Generator: Deploy from GitHub
   - Free tier includes 750 hours/month

2. **Railway**:
   - Auto-detects Flask
   - Easy environment variable setup
   - Free tier available

3. **PythonAnywhere**:
   - Good for Python apps
   - Free tier with limitations

### Deployment Steps

Will deploy both Flask apps to free hosting and share live URLs.

## Video Demonstration

A 6-7 minute video explaining:
1. Code walkthrough for each project
2. How each component works
3. Live demonstration of functionality
4. Technical decisions and challenges
5. Understanding of implementation

**Video will be uploaded to YouTube (unlisted) and URL shared.**

## Contact & Submission

- **GitHub Repository**: https://github.com/Codewithnavy/Aeroleads_assignment
- **YouTube Video**: [Will be added]
- **Live Demos**: [Will be added]
- **WhatsApp**: 9981513777 (for submission)

## Learning Outcomes

This assignment demonstrates:
- Advanced web scraping techniques
- API integration skills
- AI implementation experience
- Full-stack development capabilities
- Problem-solving under constraints
- Production-ready code practices
- Documentation skills

## License

Created for Aeroleads technical assessment. All code is original work demonstrating technical capabilities.

## Acknowledgments

- Twilio for telephony API
- Google for Gemini AI API
- Selenium for web automation
- Flask community for excellent documentation

---

**Note**: This is a demonstration project for a technical assignment. Use responsibly and ethically, especially for the LinkedIn scraper and autodialer components.
