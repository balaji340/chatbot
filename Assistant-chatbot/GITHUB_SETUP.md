================================================================================
                        GITHUB SETUP GUIDE
================================================================================

GOAL: Push your Health Chatbot to GitHub and get a public repository link

================================================================================
                    STEP 1: INSTALL GIT (if not installed)
================================================================================

Windows Users:
1. Go to: https://git-scm.com/download/win
2. Download Git for Windows
3. Run the installer
4. Use all default settings (click "Next" through the installer)
5. Once installed, restart your terminal/PowerShell

Verify Git is installed:
   Open PowerShell and run: git --version
   You should see: git version X.X.X

================================================================================
                 STEP 2: CREATE GITHUB REPOSITORY
================================================================================

1. Go to: https://github.com (create account if you don't have one)

2. Click the "+" icon in top-right → "New repository"

3. Fill in the form:
   Repository name: health-chatbot
   Description: AI-powered health chatbot using Django and ChatterBot
   Public: YES (so anyone can access)
   ✓ Add a README file (optional)
   ✓ Add .gitignore → Select "Python"
   ✓ Choose a license (optional)

4. Click "Create repository"

5. You'll see your repository URL:
   https://github.com/YOUR_USERNAME/health-chatbot

================================================================================
              STEP 3: CONFIGURE GIT (First time only)
================================================================================

Open PowerShell and run:

   git config --global user.name "Your Name"
   git config --global user.email "your-email@github.com"

Example:
   git config --global user.name "John Doe"
   git config --global user.email "john@example.com"

================================================================================
           STEP 4: PUSH YOUR PROJECT TO GITHUB
================================================================================

In PowerShell, navigate to your project and run these commands:

   cd D:\project\health-chatbot

   git init

   git add .

   git commit -m "Initial commit - Health Chatbot with Django and ChatterBot"

   git branch -M main

   git remote add origin https://github.com/YOUR_USERNAME/health-chatbot.git

   git push -u origin main

Replace YOUR_USERNAME with your actual GitHub username!

Examples:
   If your GitHub username is "john_doe":
   git remote add origin https://github.com/john_doe/health-chatbot.git
   git push -u origin main

================================================================================
                     STEP 5: VERIFY ON GITHUB
================================================================================

1. Go to: https://github.com/YOUR_USERNAME/health-chatbot

2. You should see:
   - All your project files
   - Code structure visible
   - README.md (if you added one)

3. Your public repository link is:
   https://github.com/YOUR_USERNAME/health-chatbot

================================================================================
                      YOUR GITHUB LINKS WILL BE
================================================================================

Main Repository:
   https://github.com/YOUR_USERNAME/health-chatbot

Raw file example:
   https://raw.githubusercontent.com/YOUR_USERNAME/health-chatbot/main/README.md

Clone command for others:
   git clone https://github.com/YOUR_USERNAME/health-chatbot.git

================================================================================
                   TROUBLESHOOTING
================================================================================

❌ "git: command not found"
   → Git not installed. Follow Step 1 above.

❌ "fatal: could not read Username for 'https://github.com'"
   → GitHub asking for credentials. Use Personal Access Token:
     1. Go to GitHub Settings → Developer settings → Personal access tokens
     2. Generate new token with "repo" scope
     3. Copy token
     4. Paste when prompted (token will be hidden)

❌ "fatal: destination path already exists"
   → Repository already initialized. Delete .git folder first:
     Remove-Item -Recurse -Force .git

❌ "Please tell me who you are" error
   → Run the config commands from Step 3

================================================================================
                    QUICK COMMAND SUMMARY
================================================================================

# One-time setup
git config --global user.name "Your Name"
git config --global user.email "your.email@github.com"

# For each new repository
git init
git add .
git commit -m "Your message"
git branch -M main
git remote add origin https://github.com/USERNAME/health-chatbot.git
git push -u origin main

# For future updates
git add .
git commit -m "Description of changes"
git push

================================================================================
                    NEXT STEPS AFTER GITHUB
================================================================================

1. Share your GitHub link: https://github.com/YOUR_USERNAME/health-chatbot

2. Deploy from GitHub using:
   - Railway: https://railway.app (recommended)
   - Render: https://render.com
   - Heroku: https://heroku.com

3. Your deployed app link will be separate from GitHub:
   Example: https://health-chatbot.up.railway.app

================================================================================
                        SUPPORT LINKS
================================================================================

GitHub Help: https://docs.github.com/
Git Documentation: https://git-scm.com/doc/
GitHub SSH Setup: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
Personal Access Tokens: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

================================================================================
