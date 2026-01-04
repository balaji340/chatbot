# Django Health Chatbot - Deployment Guide

## Quick Deploy on Railway

Follow these steps to deploy your Django Health Chatbot to Railway (free tier available):

### Step 1: Push to GitHub
```bash
cd d:\project\health-chatbot
git config user.email "your-email@example.com"
git config user.name "Your Name"
git add .
git commit -m "Initial commit - deployment ready"
git branch -M main
```

Create a repository on GitHub and push:
```bash
git remote add origin https://github.com/YOUR_USERNAME/health-chatbot.git
git push -u origin main
```

### Step 2: Deploy on Railway

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your "health-chatbot" repository
5. Railway will automatically detect Django and configure it

### Step 3: Set Environment Variables

In Railway dashboard, go to your project → Variables and add:

```
DEBUG=False
ALLOWED_HOSTS=*.railway.app
SECRET_KEY=your-random-secret-key-here
DATABASE_URL=postgresql://...  (Railway provides this automatically)
```

### Step 4: Configure Database

Railway provides PostgreSQL by default. Your migrations will run automatically.

## Deploy on Render (Alternative)

### Step 1: Connect GitHub Repository
- Go to https://render.com
- Click "New +" → "Web Service"
- Connect your GitHub repo

### Step 2: Configure Service
- Name: health-chatbot
- Runtime: Python 3.11
- Build Command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
- Start Command: `gunicorn django_chatbot_project.wsgi:application`

### Step 3: Add Environment Variables
- `DEBUG`: False
- `ALLOWED_HOSTS`: *.render.com
- `SECRET_KEY`: (generate a random key)

## Deploy on Heroku (if needed)

1. Install Heroku CLI
2. Run: `heroku create your-app-name`
3. Run: `git push heroku main`
4. Set environment variables: `heroku config:set DEBUG=False`

## Local Testing Before Deployment

```bash
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Collect static files
python manage.py collectstatic --noinput

# Run tests
python manage.py test

# Start server
python manage.py runserver
```

## Troubleshooting

- If static files don't load, run: `python manage.py collectstatic --clear --noinput`
- Check logs: `heroku logs --tail` or visit your platform's log viewer
- Ensure all environment variables are set correctly

## Your Deployment Link

After deployment, your app will be available at:
- **Railway**: `https://your-app-name.up.railway.app`
- **Render**: `https://your-app-name.onrender.com`
- **Heroku**: `https://your-app-name.herokuapp.com`

Replace `your-app-name` with the actual name you chose during deployment.
