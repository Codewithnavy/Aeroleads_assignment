# Deployment Guide

Guide for deploying the Autodialer and Blog Generator apps to free hosting platforms.

## Recommended Platforms

### 1. Render (Recommended)
- Free tier: 750 hours/month
- Easy deployment from GitHub
- Supports environment variables
- Auto-deploy on git push

### 2. Railway
- Free tier available
- Auto-detects Flask
- Simple setup

### 3. PythonAnywhere
- Free tier with limitations
- Good for Python apps

## Deploying to Render

### Autodialer App

1. **Prepare the app**:

Create `render.yaml` in `autodialer_app/`:
```yaml
services:
  - type: web
    name: autodialer
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: TWILIO_ACCOUNT_SID
        sync: false
      - key: TWILIO_AUTH_TOKEN
        sync: false
      - key: TWILIO_PHONE_NUMBER
        sync: false
```

Add `gunicorn` to `requirements.txt`:
```
flask==3.0.0
twilio==8.11.0
python-dotenv==1.0.0
gunicorn==21.2.0
```

Update `app.py` to bind to 0.0.0.0:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

2. **Deploy**:
- Go to https://render.com
- Sign up/login with GitHub
- Click "New +" → "Web Service"
- Connect your GitHub repository
- Select the `autodialer_app` directory
- Set environment variables in Render dashboard
- Click "Create Web Service"

3. **Set Environment Variables**:
- `TWILIO_ACCOUNT_SID`: Your Twilio SID
- `TWILIO_AUTH_TOKEN`: Your Twilio token
- `TWILIO_PHONE_NUMBER`: Your Twilio number

### Blog Generator App

1. **Prepare the app**:

Create `render.yaml` in `blog_generator/`:
```yaml
services:
  - type: web
    name: blog-generator
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: GEMINI_API_KEY
        sync: false
```

Add `gunicorn` to `requirements.txt`:
```
flask==3.0.0
google-generativeai==0.3.2
markdown==3.5.1
gunicorn==21.2.0
```

Update `app.py`:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
```

2. **Deploy**:
- Same process as autodialer
- Set `GEMINI_API_KEY` environment variable

## Deploying to Railway

### Setup

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository

### Configuration

Railway auto-detects Flask apps. Just ensure:

1. `requirements.txt` is present
2. Update `app.py` to use PORT env variable:
```python
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

3. Set environment variables in Railway dashboard

## Deploying to PythonAnywhere

### Autodialer App

1. Create account at https://www.pythonanywhere.com
2. Upload files via "Files" tab
3. Create virtual environment:
```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
pip install -r requirements.txt
```

4. Configure WSGI file:
```python
import sys
import os

path = '/home/yourusername/autodialer_app'
if path not in sys.path:
    sys.path.append(path)

os.environ['TWILIO_ACCOUNT_SID'] = 'your_sid'
os.environ['TWILIO_AUTH_TOKEN'] = 'your_token'
os.environ['TWILIO_PHONE_NUMBER'] = 'your_number'

from app import app as application
```

5. Reload web app

## Production Checklist

- [ ] Add `gunicorn` to requirements.txt
- [ ] Update `app.run()` to use 0.0.0.0 and PORT env var
- [ ] Set `FLASK_ENV=production`
- [ ] Configure all environment variables
- [ ] Test deployment locally first
- [ ] Set up custom domain (optional)
- [ ] Enable HTTPS (usually automatic)
- [ ] Monitor logs for errors

## Environment Variables Summary

### Autodialer App
- `TWILIO_ACCOUNT_SID`: From Twilio dashboard
- `TWILIO_AUTH_TOKEN`: From Twilio dashboard
- `TWILIO_PHONE_NUMBER`: Your Twilio number
- `PORT`: Auto-set by platform
- `FLASK_ENV`: Set to "production"

### Blog Generator
- `GEMINI_API_KEY`: From Google AI Studio
- `PORT`: Auto-set by platform
- `FLASK_ENV`: Set to "production"

## Testing Deployment

After deployment:

1. **Autodialer**:
   - Visit deployed URL
   - Test AI command with safe number
   - Check logs in platform dashboard

2. **Blog Generator**:
   - Visit /blog route
   - Check if 10 articles loaded
   - Try generating new article from /blog/admin

## Troubleshooting

### App won't start
- Check logs in platform dashboard
- Verify all dependencies are in requirements.txt
- Ensure PORT is correctly configured

### Environment variables not working
- Verify they're set in platform dashboard
- Restart the app after setting variables
- Check variable names match exactly

### Twilio calls fail
- Ensure webhook URLs point to deployed app
- Check Twilio console for error details
- Verify phone number format

### Gemini API errors
- Check API key is valid
- Ensure you haven't exceeded rate limits
- Verify API key has correct permissions

## Free Tier Limitations

### Render
- 750 hours/month
- Sleeps after 15 min inactivity
- Takes 30-60s to wake up

### Railway
- $5 free credit/month
- Usage-based pricing

### PythonAnywhere
- Limited CPU time
- Single web app on free tier

## Webhooks Configuration

For Autodialer, you need to configure Twilio webhooks:

1. Go to Twilio Console
2. Navigate to Phone Numbers
3. Select your number
4. Under "Voice & Fax", set:
   - **A Call Comes In**: `https://your-app.onrender.com/voice`
   - **Status Callback**: `https://your-app.onrender.com/call-status`

Replace `your-app.onrender.com` with your actual deployment URL.

## Performance Optimization

1. Use persistent storage (database) instead of in-memory
2. Implement caching for blog posts
3. Add rate limiting
4. Optimize AI API calls
5. Use CDN for static assets

## Security Considerations

- Never commit `.env` files
- Use environment variables for all secrets
- Enable HTTPS (usually automatic)
- Implement rate limiting
- Add authentication for admin panels
- Validate all inputs
- Use CORS appropriately

## Monitoring

After deployment, monitor:
- Error rates (check platform logs)
- API usage (Twilio/Gemini dashboards)
- Response times
- Uptime

## Custom Domain (Optional)

Most platforms support custom domains:
1. Purchase domain (Namecheap, GoDaddy, etc.)
2. Add domain in platform settings
3. Configure DNS records
4. Wait for SSL certificate provisioning

## Maintenance

- Keep dependencies updated
- Monitor API quotas
- Check logs regularly
- Backup data if using database
- Test after platform updates

## Cost Management

To stay within free tiers:
- Monitor Twilio usage (free trial has limits)
- Track Gemini API requests
- Keep an eye on hosting hours
- Set up billing alerts

## Alternative Deployment Options

1. **Heroku** (No longer has free tier)
2. **Fly.io** (Free tier available)
3. **Vercel** (Good for static sites, limited for Flask)
4. **Netlify** (Static sites only)
5. **Google Cloud Run** (Free tier available)
6. **AWS Free Tier** (12 months free)

## Final Steps

1. Deploy both apps
2. Test thoroughly
3. Note down URLs
4. Update README with live demo links
5. Include in video demonstration
6. Submit URLs with assignment

## Sample Deployment URLs

After deployment, update README:
```markdown
## Live Demo Links

- **Autodialer App**: https://autodialer-xyz.onrender.com
- **Blog Generator**: https://blog-generator-xyz.onrender.com
```

Good luck with deployment! 🚀
