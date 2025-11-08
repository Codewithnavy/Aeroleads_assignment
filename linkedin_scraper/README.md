# LinkedIn Profile Scraper

A Python-based tool to scrape LinkedIn profile data using Selenium WebDriver with intelligent anti-detection measures.

## Features

- **Smart Login**: Attempts login via Google search to avoid direct LinkedIn detection
- **Anti-Detection**: Rotating user agents, randomized delays, and stealth configurations
- **Profile Data Extraction**: Name, headline, location, connections, about, experience, education
- **CSV Export**: Saves all scraped data to a structured CSV file
- **Error Handling**: Robust error handling for missing profile elements

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Chrome browser installed
- ChromeDriver (automatically managed by webdriver-manager)

### Installation

1. Navigate to the linkedin_scraper directory:
```bash
cd linkedin_scraper
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Configuration

Before running the scraper, you need to configure your LinkedIn test account credentials:

1. Open `scraper.py`
2. Update the credentials in the `main()` function:
```python
LINKEDIN_EMAIL = 'your-test-email@gmail.com'
LINKEDIN_PASSWORD = 'your-test-password'
```

**IMPORTANT**: Use a test LinkedIn account, not your main account, as web scraping may violate LinkedIn's Terms of Service.

## Usage

Run the scraper:
```bash
python scraper.py
```

The script will:
1. Set up Chrome driver with anti-detection measures
2. Navigate via Google to LinkedIn login
3. Attempt to log in with your credentials
4. Scrape 20 pre-configured LinkedIn profiles
5. Save the data to `linkedin_profiles.csv`

## Sample Profile URLs

The script includes 20 public LinkedIn profiles of tech leaders:
- Satya Nadella (Microsoft CEO)
- Bill Gates
- Sundar Pichai (Google CEO)
- Tim Cook (Apple CEO)
- And 16 more...

You can modify the `profile_urls` list in `scraper.py` to scrape different profiles.

## Output Format

The CSV file contains the following fields:
- `url`: LinkedIn profile URL
- `name`: Full name
- `headline`: Professional headline
- `location`: Location information
- `about`: About section (first 200 characters)
- `connections`: Number of connections
- `experience`: First experience entry (first 200 characters)
- `education`: Education information (first 200 characters)

## Anti-Detection Measures

1. **User Agent Rotation**: Randomly selects from multiple browser user agents
2. **Stealth Mode**: Disables automation flags in Chrome
3. **Random Delays**: 3-6 seconds between page loads, 5-10 seconds between profiles
4. **Google Entry Point**: Attempts login via Google search instead of direct navigation
5. **Human-like Scrolling**: Scrolls page to load dynamic content

## Limitations & Challenges

- LinkedIn actively blocks automated scraping
- May require CAPTCHA solving in some cases
- Rate limiting may occur with many requests
- Profile visibility depends on privacy settings
- May require manual intervention for login verification

## Ethical Considerations

This tool is created for educational purposes as part of a technical assignment. When using web scrapers:
- Respect robots.txt and Terms of Service
- Don't overload servers with requests
- Use only publicly available data
- Consider privacy implications
- Use test accounts, not production accounts

## Troubleshooting

**Login fails**: 
- Verify credentials are correct
- Check if LinkedIn requires email verification
- Try manual login first to ensure account is accessible

**Profiles not loading**:
- Ensure you're logged in successfully
- Check if profiles are public
- Increase wait times if network is slow

**ChromeDriver errors**:
- Ensure Chrome browser is up to date
- webdriver-manager should auto-download correct driver version

## Alternative Approaches Considered

1. **Proxy Rotation**: Could implement residential proxies to avoid IP blocking
2. **Alternative Data Sources**: Could scrape sites that aggregate LinkedIn data
3. **API Access**: LinkedIn API has strict limitations for personal use
4. **Headless Mode**: Could run in headless mode for faster execution (but easier to detect)

## Technical Implementation

The scraper uses:
- **Selenium WebDriver**: Browser automation
- **Chrome Options**: Custom browser configuration
- **WebDriverWait**: Dynamic element waiting
- **Random Module**: Delay randomization
- **CSV Module**: Data export

## Future Enhancements

- Proxy rotation support
- CAPTCHA solving integration
- Parallel scraping with multiple accounts
- More detailed profile data extraction
- Database storage option
- Resume capability for interrupted scrapes
