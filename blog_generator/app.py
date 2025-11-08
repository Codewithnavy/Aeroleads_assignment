from flask import Flask, render_template, request, jsonify, redirect, url_for
import google.generativeai as genai
import os
import json
from datetime import datetime
import re

app = Flask(__name__)

# Configure Gemini API
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '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')

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
else:
    model = None

# In-memory blog storage (in production, use a database)
blog_posts = []

class BlogPost:
    def __init__(self, title, content, author="AI", tags=None):
        self.id = len(blog_posts) + 1
        self.title = title
        self.content = content
        self.author = author
        self.tags = tags or []
        self.created_at = datetime.now()
        self.slug = self.generate_slug(title)
        self.excerpt = self.generate_excerpt(content)
    
    def generate_slug(self, title):
        """Generate URL-friendly slug from title"""
        slug = title.lower()
        slug = re.sub(r'[^a-z0-9]+', '-', slug)
        slug = slug.strip('-')
        return slug
    
    def generate_excerpt(self, content):
        """Generate excerpt from content"""
        # Remove markdown formatting
        plain = re.sub(r'[#*`_\[\]()]', '', content)
        # Get first 200 characters
        excerpt = plain[:200]
        if len(plain) > 200:
            excerpt += '...'
        return excerpt
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'tags': self.tags,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'slug': self.slug,
            'excerpt': self.excerpt
        }

def generate_article_with_ai(title, details="", topic_keywords=""):
    """Generate article content using Gemini AI"""
    if not model:
        return None, "Gemini API not configured"
    
    try:
        prompt = f"""Write a comprehensive, well-structured blog article about: {title}

Additional details: {details}

Keywords to focus on: {topic_keywords}

Requirements:
- Write in a professional yet engaging tone
- Include an introduction that hooks the reader
- Use clear headings and subheadings (use ## for main headings, ### for subheadings)
- Provide practical examples and code snippets where relevant
- Include best practices and tips
- End with a conclusion that summarizes key points
- Aim for 1000-1500 words
- Use markdown formatting
- Make it informative and valuable for developers

Please write the complete article now:"""

        response = model.generate_content(prompt)
        
        if response and response.text:
            return response.text, None
        else:
            return None, "Failed to generate content"
    
    except Exception as e:
        return None, str(e)

def parse_ai_blog_request(request_text):
    """Parse natural language request for blog generation"""
    # Try to extract titles and details from the request
    articles = []
    
    # Pattern 1: Numbered list
    lines = request_text.strip().split('\n')
    current_article = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check if it's a numbered item (1. Title or 1) Title)
        match = re.match(r'^(\d+)[.)]\s*(.+)$', line)
        if match:
            if current_article:
                articles.append(current_article)
            current_article = {
                'title': match.group(2).strip(),
                'details': '',
                'keywords': ''
            }
        elif current_article and (line.startswith('-') or line.startswith('•')):
            # Additional details
            current_article['details'] += ' ' + line.lstrip('-•').strip()
        elif current_article and not re.match(r'^\d+[.)]', line):
            # Continuation of details
            if current_article['details']:
                current_article['details'] += ' ' + line
            else:
                current_article['details'] = line
    
    if current_article:
        articles.append(current_article)
    
    # If no numbered format found, treat each non-empty line as a title
    if not articles:
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                articles.append({
                    'title': line,
                    'details': '',
                    'keywords': ''
                })
    
    return articles

@app.route('/')
def home():
    """Home page redirects to blog"""
    return redirect(url_for('blog_index'))

@app.route('/blog')
def blog_index():
    """Blog listing page"""
    return render_template('blog_index.html', posts=blog_posts)

@app.route('/blog/<slug>')
def blog_post(slug):
    """Individual blog post page"""
    post = next((p for p in blog_posts if p.slug == slug), None)
    if not post:
        return "Post not found", 404
    return render_template('blog_post.html', post=post)

@app.route('/blog/admin')
def blog_admin():
    """Admin interface for creating blog posts"""
    return render_template('blog_admin.html')

@app.route('/api/generate-single', methods=['POST'])
def generate_single():
    """Generate a single blog post"""
    data = request.json
    title = data.get('title', '')
    details = data.get('details', '')
    keywords = data.get('keywords', '')
    
    if not title:
        return jsonify({'success': False, 'error': 'Title is required'}), 400
    
    content, error = generate_article_with_ai(title, details, keywords)
    
    if error:
        return jsonify({'success': False, 'error': error}), 500
    
    # Extract tags from keywords
    tags = [k.strip() for k in keywords.split(',') if k.strip()]
    
    post = BlogPost(title, content, tags=tags)
    blog_posts.insert(0, post)  # Add to beginning
    
    return jsonify({
        'success': True,
        'post': post.to_dict()
    })

@app.route('/api/generate-bulk', methods=['POST'])
def generate_bulk():
    """Generate multiple blog posts from AI request"""
    data = request.json
    request_text = data.get('request', '')
    
    if not request_text:
        return jsonify({'success': False, 'error': 'Request text is required'}), 400
    
    # Parse the request
    articles = parse_ai_blog_request(request_text)
    
    if not articles:
        return jsonify({'success': False, 'error': 'Could not parse any articles from request'}), 400
    
    generated_posts = []
    errors = []
    
    for article in articles:
        content, error = generate_article_with_ai(
            article['title'],
            article['details'],
            article['keywords']
        )
        
        if error:
            errors.append(f"Failed to generate '{article['title']}': {error}")
            continue
        
        tags = [k.strip() for k in article['keywords'].split(',') if k.strip()]
        post = BlogPost(article['title'], content, tags=tags)
        blog_posts.insert(0, post)
        generated_posts.append(post.to_dict())
    
    return jsonify({
        'success': True,
        'generated': len(generated_posts),
        'posts': generated_posts,
        'errors': errors
    })

@app.route('/api/posts')
def get_posts():
    """Get all blog posts"""
    return jsonify({
        'posts': [post.to_dict() for post in blog_posts]
    })

@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """Delete a blog post"""
    global blog_posts
    blog_posts = [p for p in blog_posts if p.id != post_id]
    return jsonify({'success': True})

@app.route('/api/export-posts')
def export_posts():
    """Export all posts as JSON"""
    posts_data = [post.to_dict() for post in blog_posts]
    return jsonify(posts_data)

# Generate 10 default articles on startup
def generate_default_articles():
    """Generate 10 default programming articles"""
    default_topics = [
        {
            'title': 'Understanding Python Decorators: A Complete Guide',
            'details': 'Explain what decorators are, how they work, and practical use cases',
            'keywords': 'Python, decorators, advanced Python, functions'
        },
        {
            'title': 'RESTful API Design Best Practices in 2024',
            'details': 'Cover HTTP methods, status codes, versioning, and security',
            'keywords': 'REST API, web development, backend, HTTP'
        },
        {
            'title': 'Introduction to Docker for Developers',
            'details': 'Basics of containerization, Docker commands, and deployment',
            'keywords': 'Docker, containers, DevOps, deployment'
        },
        {
            'title': 'JavaScript Async/Await Explained Simply',
            'details': 'Promises, async functions, error handling, and best practices',
            'keywords': 'JavaScript, async, promises, ES6'
        },
        {
            'title': 'SQL vs NoSQL: Choosing the Right Database',
            'details': 'Compare SQL and NoSQL databases with use cases and examples',
            'keywords': 'databases, SQL, NoSQL, MongoDB, PostgreSQL'
        },
        {
            'title': 'Git Workflow Strategies for Teams',
            'details': 'Git flow, trunk-based development, and collaboration best practices',
            'keywords': 'Git, version control, collaboration, workflow'
        },
        {
            'title': 'Building Scalable Microservices Architecture',
            'details': 'Microservices patterns, communication, and deployment strategies',
            'keywords': 'microservices, architecture, scalability, backend'
        },
        {
            'title': 'Modern CSS: Flexbox and Grid Layouts',
            'details': 'Master responsive layouts with Flexbox and CSS Grid',
            'keywords': 'CSS, Flexbox, Grid, responsive design, frontend'
        },
        {
            'title': 'Understanding Time Complexity and Big O Notation',
            'details': 'Algorithm analysis, common complexities, and optimization',
            'keywords': 'algorithms, Big O, performance, data structures'
        },
        {
            'title': 'Secure Coding Practices for Web Applications',
            'details': 'XSS, CSRF, SQL injection prevention, and security best practices',
            'keywords': 'security, web security, OWASP, secure coding'
        }
    ]
    
    print("Generating default blog articles...")
    for idx, topic in enumerate(default_topics, 1):
        print(f"Generating article {idx}/10: {topic['title']}")
        content, error = generate_article_with_ai(
            topic['title'],
            topic['details'],
            topic['keywords']
        )
        
        if content:
            tags = [k.strip() for k in topic['keywords'].split(',')]
            post = BlogPost(topic['title'], content, tags=tags)
            blog_posts.append(post)
            print(f"✓ Generated: {topic['title']}")
        else:
            print(f"✗ Failed: {topic['title']} - {error}")
    
    print(f"\nGenerated {len(blog_posts)} articles successfully!")

if __name__ == '__main__':
    print("=" * 60)
    print("Blog Generator App Starting...")
    print("=" * 60)
    
    if not model:
        print("WARNING: Gemini API not configured!")
        print("Set GEMINI_API_KEY environment variable")
    else:
        # Generate default articles
        generate_default_articles()
    
    print("\nAccess the blog at: http://localhost:5001/blog")
    print("Access admin at: http://localhost:5001/blog/admin")
    print("=" * 60)
    
    app.run(debug=True, port=5001)
