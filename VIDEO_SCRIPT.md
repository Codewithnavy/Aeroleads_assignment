# Video Script for Aeroleads Assignment Demo

**Total Duration**: 6-7 minutes
**Format**: Screen recording with voice narration

---

## Introduction (30 seconds)

**[Show GitHub repository page]**

"Hello! I'm presenting my submission for the Aeroleads technical assignment. This repository contains three complete projects demonstrating full-stack development, API integration, and AI implementation.

Let me walk you through each project, explain the code, and show live demonstrations."

---

## Part 1: LinkedIn Scraper (1.5 minutes)

### Code Walkthrough (45 sec)

**[Open scraper.py in VS Code]**

"The first project is a LinkedIn profile scraper built with Selenium. Let me explain the key components:

1. **Anti-Detection Setup** [Show setup_driver() function]:
   - I'm using rotating user agents to avoid detection
   - Disabled automation flags with stealth mode
   - This makes the browser look like a real user, not a bot

2. **Smart Login** [Show login_via_google() function]:
   - Instead of going directly to LinkedIn, I navigate through Google search
   - This helps avoid LinkedIn's bot detection
   - Falls back to direct login if needed

3. **Profile Scraping** [Show scrape_profile() function]:
   - Extracts name, headline, location, connections
   - Handles missing elements gracefully with try-except blocks
   - Uses random delays (3-6 seconds) to mimic human behavior
   - Scrolls the page to load dynamic content

4. **Data Export** [Show save_to_csv() function]:
   - Saves all scraped data to CSV format
   - Easy to open in Excel or process further"

### Demo (45 sec)

**[Run the scraper OR show sample output]**

"Here's the scraper in action... [If running live, show browser opening, navigating, scraping]

As you can see, it successfully:
- Opens Chrome in stealth mode
- Navigates to LinkedIn profiles
- Extracts all relevant data
- Exports to CSV

[Show the CSV file in Excel/Notepad]

Here's the output - clean, structured data with all profile information."

---

## Part 2: Autodialer App (2 minutes)

### Code Walkthrough (1 minute)

**[Open autodialer_app/app.py in VS Code]**

"The second project is a Flask-based autodialer application with AI capabilities.

1. **AI Command Parsing** [Show parse_ai_command() function]:
   - Uses regex patterns to understand natural language
   - Handles various phrasings: 'call', 'dial', 'phone', 'make a call to'
   - Extracts phone numbers from commands

2. **Twilio Integration** [Show make_call() function]:
   - Connects to Twilio API for making calls
   - Creates TwiML for voice synthesis
   - Implements webhooks for real-time status updates

3. **AI Voice** [Show voice() function]:
   - Uses Amazon Polly's Kajal voice
   - Indian English accent for natural-sounding calls
   - Dynamic message content

4. **Call Logging** [Show CallLog class]:
   - Tracks every call with timestamp, status, duration
   - Updates in real-time via webhooks
   - Provides detailed statistics"

### Live Demo (1 minute)

**[Open http://localhost:5000 in browser]**

"Here's the application running:

[Show the dashboard]
1. Real-time statistics at the top - total calls, successful, failed

[Show AI command interface]
2. The AI voice command - I can just type 'call 1800123456' and it understands

[Type a command and execute - or show pre-recorded result]

[Show Single Call tab]
3. Single call interface - enter number and custom message

[Show Bulk Calls tab]
4. Bulk calling - paste multiple numbers

[Show CSV Upload tab]
5. CSV upload - upload a file with phone numbers

[Show Call Logs section]
6. Live call logs - see status updates in real-time
7. Can export to CSV for record-keeping

The UI is responsive, modern, and user-friendly. For testing, I'm using toll-free 1800 numbers - never real people!"

---

## Part 3: Blog Generator (2 minutes)

### Code Walkthrough (1 minute)

**[Open blog_generator/app.py in VS Code]**

"The third project is an AI-powered blog generator using Google Gemini.

1. **AI Content Generation** [Show generate_article_with_ai() function]:
   - Sends detailed prompts to Gemini AI
   - Requests 1000-1500 word articles
   - Includes requirements for structure, examples, best practices
   - Returns markdown-formatted content

2. **Natural Language Parsing** [Show parse_ai_blog_request() function]:
   - Understands numbered lists: '1. Topic 2. Topic'
   - Extracts titles and details
   - Handles various input formats

3. **Auto-Generation on Startup** [Show generate_default_articles() function]:
   - Automatically generates 10 programming articles when app starts
   - Topics: Python, APIs, Docker, JavaScript, databases, etc.

4. **Blog Post Model** [Show BlogPost class]:
   - Generates URL-friendly slugs
   - Creates excerpts automatically
   - Handles tagging and metadata"

### Live Demo (1 minute)

**[Open http://localhost:5001/blog in browser]**

"Here's the blog running:

[Show blog home page]
1. Beautiful card layout with 10 auto-generated articles
2. Each card shows title, excerpt, tags, and timestamp

[Click on an article]
3. Individual article page with full content
4. Markdown rendered beautifully with code syntax highlighting
5. Professional formatting with headings, lists, code blocks

[Navigate to /blog/admin]
6. Admin panel for content management

[Show AI Bulk Generation]
7. AI prompt interface - I can type a list of topics

[Type or show example: '1. Python Decorators 2. REST APIs']

8. It parses my request and generates complete articles

[Show Single Article Generation if time allows]

[Back to blog home]

All 10 articles were auto-generated on startup - no manual content creation needed!"

---

## Conclusion (30 seconds)

**[Show GitHub repository again]**

"To summarize, I've built three complete projects:

1. **LinkedIn Scraper**: Advanced web scraping with anti-detection
2. **Autodialer**: AI-powered calling system with Twilio integration
3. **Blog Generator**: Automated content creation with Gemini AI

All code is well-documented, follows best practices, and is production-ready. The repository includes:
- Comprehensive README files for each project
- Setup and deployment guides
- Clean, maintainable code
- Security best practices

Thank you for reviewing my submission. The repository is available at github.com/Codewithnavy/Aeroleads_assignment, and I'll be deploying the apps to free hosting platforms.

[Optional: Mention current and expected salary if comfortable]

Looking forward to your feedback!"

---

## Recording Tips

1. **Preparation**:
   - Test all apps before recording
   - Close unnecessary tabs/applications
   - Use a good microphone
   - Record in a quiet environment
   - Prepare test data (phone numbers, topics)

2. **Screen Recording Tools**:
   - **Windows**: OBS Studio (free), Xbox Game Bar
   - **Cross-platform**: OBS Studio, Loom
   - **Quality**: 1080p, 30fps minimum

3. **Editing**:
   - Trim any mistakes
   - Add transitions if needed
   - Include text overlays for GitHub URL
   - Background music (optional, keep low volume)

4. **Voice Tips**:
   - Speak clearly and at moderate pace
   - Show confidence and understanding
   - Explain WHY you made certain decisions
   - Demonstrate you understand the code, not just generated it

5. **YouTube Upload**:
   - Title: "Aeroleads Technical Assignment - [Your Name]"
   - Description: Include GitHub link and project summary
   - Set to "Unlisted"
   - Add relevant tags: python, flask, twilio, AI, web scraping

6. **Timing**:
   - Practice once or twice
   - Keep to 6-7 minutes (no longer than 8)
   - Pause briefly between sections

## Alternative Approach (If Apps Don't Run Smoothly)

If you face issues running the apps live:
1. Show code walkthrough thoroughly
2. Show screenshots/pre-recorded GIFs of working apps
3. Focus on explaining the logic and architecture
4. Show the output files (CSV, logs, etc.)

## What Reviewers Want to See

1. ✅ You understand the code (explain key functions)
2. ✅ You can navigate the codebase confidently
3. ✅ You made conscious technical decisions
4. ✅ You can demonstrate working features
5. ✅ You know how to troubleshoot issues
6. ✅ Professional presentation

Good luck with your video! 🎥
