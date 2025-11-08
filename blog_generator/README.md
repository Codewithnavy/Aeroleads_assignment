# Blog Generator - AI-Powered Content Creation

A Flask-based web application that generates high-quality programming blog articles using Google's Gemini AI API.

## Features

- **AI-Powered Generation**: Uses Google Gemini Pro to generate comprehensive articles
- **Bulk Generation**: Process natural language requests to generate multiple articles at once
- **AI Prompt Interface**: Simply describe what articles you want, and the AI generates them
- **10 Default Articles**: Automatically generates 10 programming articles on startup
- **Beautiful Blog Interface**: Clean, modern design for reading articles
- **Admin Panel**: Easy-to-use interface for generating and managing content
- **Markdown Support**: Articles are formatted in Markdown and rendered beautifully
- **Tags & Categories**: Automatic tagging based on keywords
- **SEO-Friendly URLs**: Slug-based URLs for better SEO

## Technology Stack

- **Backend**: Python Flask
- **AI API**: Google Gemini Pro (free tier available)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Markdown Rendering**: Marked.js
- **Storage**: In-memory (easily extensible to database)

## Setup Instructions

### Prerequisites

1. Python 3.8 or higher
2. Google Gemini API key (free at [ai.google.dev](https://ai.google.dev))

### Getting Gemini API Key

1. Go to [https://ai.google.dev](https://ai.google.dev)
2. Click "Get API Key in Google AI Studio"
3. Sign in with your Google account
4. Create a new API key
5. Copy the API key

**Note**: The provided API key in the code is already configured, but you can use your own.

### Installation

1. Navigate to the blog_generator directory:
```bash
cd blog_generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set environment variable (optional, if not using the default key):
```bash
# Windows PowerShell
$env:GEMINI_API_KEY="your_api_key_here"

# Linux/Mac
export GEMINI_API_KEY="your_api_key_here"
```

### Running the Application

```bash
python app.py
```

The application will:
1. Start the Flask server
2. Automatically generate 10 default programming articles
3. Be accessible at `http://localhost:5001`

**URLs**:
- Blog Home: `http://localhost:5001/blog`
- Admin Panel: `http://localhost:5001/blog/admin`

## Usage Guide

### 1. AI Bulk Article Generation (Recommended)

This is the most powerful feature - just describe what you want!

1. Go to the Admin Panel (`/blog/admin`)
2. In the AI Bulk Generation section, type your request

**Example Requests**:

```
1. Python Decorators Explained
2. RESTful API Design Best Practices
3. Docker for Beginners
4. JavaScript Async/Await
5. SQL vs NoSQL Databases
```

Or with more details:

```
Title: Understanding Python Decorators
Details: Cover function decorators, class decorators, with practical examples

Title: Building RESTful APIs
Details: Include HTTP methods, status codes, versioning, and security best practices

Title: Introduction to Docker
Details: Explain containerization, basic Docker commands, and deployment
```

3. Click "Generate All Articles"
4. Wait 1-2 minutes (AI generates each article)
5. Articles will appear in your blog!

### 2. Single Article Generation

1. Go to Admin Panel
2. Click "Single Article" tab
3. Enter:
   - **Title**: Main topic (e.g., "Understanding Python Decorators")
   - **Details**: Specific requirements (optional)
   - **Keywords**: Comma-separated tags (e.g., "Python, decorators, advanced")
4. Click "Generate Article"

### 3. View Blog

1. Navigate to `/blog`
2. Browse all generated articles
3. Click any article to read the full content

### 4. Manage Articles

1. Go to Admin Panel
2. Click "Manage Articles" tab
3. View all articles
4. Delete unwanted articles

## Default Articles

On startup, the app generates 10 articles on these topics:

1. Understanding Python Decorators
2. RESTful API Design Best Practices
3. Introduction to Docker for Developers
4. JavaScript Async/Await Explained
5. SQL vs NoSQL: Choosing the Right Database
6. Git Workflow Strategies for Teams
7. Building Scalable Microservices Architecture
8. Modern CSS: Flexbox and Grid Layouts
9. Understanding Time Complexity and Big O Notation
10. Secure Coding Practices for Web Applications

Each article is 1000-1500 words with:
- Engaging introduction
- Clear headings and subheadings
- Practical examples
- Code snippets (where relevant)
- Best practices
- Comprehensive conclusion

## AI Content Generation

### How It Works

The app sends a detailed prompt to Gemini AI:

```python
prompt = f"""Write a comprehensive blog article about: {title}

Additional details: {details}
Keywords: {keywords}

Requirements:
- Professional yet engaging tone
- Clear structure with headings
- Practical examples and code snippets
- Best practices and tips
- 1000-1500 words
- Markdown formatting
"""
```

### AI Features

- **Context-Aware**: Understands programming topics deeply
- **Code Examples**: Generates relevant code snippets
- **Best Practices**: Includes industry standards
- **Comprehensive**: 1000-1500 word detailed articles
- **Well-Structured**: Uses proper headings and formatting

## API Endpoints

### POST /api/generate-single
Generate a single article

**Request**:
```json
{
  "title": "Understanding Python Decorators",
  "details": "Cover function and class decorators",
  "keywords": "Python, decorators, advanced"
}
```

**Response**:
```json
{
  "success": true,
  "post": {
    "id": 1,
    "title": "Understanding Python Decorators",
    "content": "...",
    "slug": "understanding-python-decorators",
    "tags": ["Python", "decorators", "advanced"]
  }
}
```

### POST /api/generate-bulk
Generate multiple articles from natural language

**Request**:
```json
{
  "request": "1. Python Decorators\n2. RESTful APIs\n3. Docker Basics"
}
```

**Response**:
```json
{
  "success": true,
  "generated": 3,
  "posts": [...],
  "errors": []
}
```

### GET /api/posts
Get all blog posts

### DELETE /api/posts/:id
Delete a specific post

### GET /api/export-posts
Export all posts as JSON

## Natural Language Processing

The app can parse various request formats:

**Numbered Lists**:
```
1. Topic One
2. Topic Two
3. Topic Three
```

**With Details**:
```
1. Topic One
   - Include specific points
   - Add examples

2. Topic Two - Cover basics and advanced topics
```

**Title/Details Format**:
```
Title: Topic One
Details: Specific requirements

Title: Topic Two
Details: More details here
```

## File Structure

```
blog_generator/
├── app.py                      # Main Flask application
├── templates/
│   ├── blog_index.html        # Blog listing page
│   ├── blog_post.html         # Individual post page
│   └── blog_admin.html        # Admin interface
├── requirements.txt            # Python dependencies
└── README.md                  # This file
```

## Deployment

### Free Hosting Options

1. **Render** (Recommended):
   - Connect GitHub repo
   - Build: `pip install -r requirements.txt`
   - Start: `python app.py`
   - Add `GEMINI_API_KEY` env variable

2. **Heroku**:
   - Create `Procfile`: `web: python app.py`
   - Add buildpack: `heroku/python`
   - Set env variables

3. **PythonAnywhere**:
   - Upload code
   - Configure WSGI
   - Set env variables

4. **Railway**:
   - Connect GitHub
   - Auto-detects Flask
   - Add env variables

### Environment Variables for Production

```bash
GEMINI_API_KEY=your_actual_api_key
FLASK_ENV=production
```

### Procfile for Heroku/Railway:
```
web: python app.py
```

## Customization

### Change Default Articles

Edit the `default_topics` list in `app.py`:

```python
default_topics = [
    {
        'title': 'Your Custom Topic',
        'details': 'Specific requirements',
        'keywords': 'tag1, tag2, tag3'
    },
    # Add more...
]
```

### Modify AI Prompt

Edit the `generate_article_with_ai()` function to customize how articles are generated:

```python
prompt = f"""Your custom prompt here..."""
```

### Add Database Storage

Replace the `blog_posts` list with database models (SQLAlchemy, MongoDB, etc.).

## Limitations

- **Rate Limits**: Gemini API has rate limits (60 requests/minute for free tier)
- **Generation Time**: Each article takes 30-60 seconds to generate
- **In-Memory Storage**: Posts are lost on restart (use database for persistence)
- **No User Authentication**: Admin panel is publicly accessible

## Future Enhancements

- Database integration (PostgreSQL/MongoDB)
- User authentication and authorization
- Article editing capabilities
- Image generation for articles (using DALL-E/Stable Diffusion)
- SEO metadata generation
- Social media sharing
- Comment system
- Article scheduling
- Multiple AI models (GPT-4, Claude, etc.)
- Rich text editor
- Article versioning
- Analytics dashboard

## Troubleshooting

### API Key Errors
- Verify the API key is correct
- Check if you've exceeded rate limits
- Ensure the key has Gemini API access

### Generation Failures
- Check internet connection
- Verify API key has sufficient quota
- Try simpler prompts
- Check Gemini API status

### Slow Generation
- Normal for comprehensive articles (30-60 seconds each)
- Gemini processes complex requests
- For bulk generation, expect 5-10 minutes for 10 articles

### Empty Blog
- Ensure AI generation completed successfully
- Check console for error messages
- Verify API key is configured

## Cost Considerations

### Gemini API Pricing (as of 2024):
- **Free Tier**: 60 requests per minute, sufficient for testing
- **Paid Tier**: Pay-per-use pricing for higher limits

For this assignment:
- Free tier is more than sufficient
- Can generate hundreds of articles monthly
- No credit card required for free tier

## Content Quality

The AI generates:
- ✅ Professional, well-researched content
- ✅ Proper code examples with explanations
- ✅ Best practices and industry standards
- ✅ Clear structure and readability
- ✅ SEO-friendly content
- ✅ Factually accurate information

**Note**: Always review AI-generated content for accuracy, especially for technical topics.

## Legal & Ethical Considerations

- AI-generated content should be reviewed before publishing
- Attribute AI generation where required
- Ensure content accuracy for technical topics
- Don't use for malicious purposes (spam, misinformation)
- Respect copyright and intellectual property
- This is for educational/demonstration purposes

## License

Created for Aeroleads technical assignment. Use responsibly and ethically.

## Support

For Gemini API issues:
- [Google AI Documentation](https://ai.google.dev/docs)
- [API Reference](https://ai.google.dev/api)

For application issues, refer to code comments or create an issue in the repository.
