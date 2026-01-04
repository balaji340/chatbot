================================================================================
                   HOST PROJECT ON GITHUB - COMPLETE GUIDE
================================================================================

Your GitHub Repository: https://github.com/balaji340/chatbot

================================================================================
                    PREREQUISITES - INSTALL GIT
================================================================================

IMPORTANT: Git must be installed first!

1. Download Git for Windows:
   https://git-scm.com/download/win

2. Run the installer:
   - Click through all prompts
   - Use default settings
   - Click "Install"
   - Click "Finish"

3. Restart PowerShell (close and reopen)

4. Verify installation:
   git --version
   (should show: git version 2.43.0.windows.1 or similar)

================================================================================
                         OPTION 1: AUTOMATED SCRIPT
================================================================================

The easiest way! We've created automated scripts for you.

CHOOSE ONE:

METHOD A: PowerShell Script (Recommended)
   1. Open PowerShell
   2. Navigate to: cd D:\project\health-chatbot
   3. Run: .\push-to-github.ps1
   4. The script will do everything automatically!

METHOD B: Batch Script
   1. Open Command Prompt (cmd.exe)
   2. Run: D:\project\health-chatbot\push-to-github.bat
   3. The script will do everything automatically!

Both scripts will:
   ✓ Initialize git
   ✓ Configure user
   ✓ Add all files
   ✓ Create commit
   ✓ Set up main branch
   ✓ Add GitHub remote
   ✓ Push to GitHub

================================================================================
                         OPTION 2: MANUAL STEPS
================================================================================

If the scripts don't work, follow these steps manually:

Step 1: Open PowerShell
   - Right-click Start menu
   - Select "Windows PowerShell" or "Terminal"

Step 2: Navigate to project
   cd D:\project\health-chatbot

Step 3: Initialize Git
   git init

Step 4: Configure Git
   git config user.email "your-email@gmail.com"
   git config user.name "Your Name"

Step 5: Add files
   git add .

Step 6: Create commit
   git commit -m "Initial commit - Health Chatbot with Django and ChatterBot"

Step 7: Rename branch
   git branch -M main

Step 8: Add GitHub remote
   git remote add origin https://github.com/balaji340/chatbot.git

Step 9: Push to GitHub
   git push -u origin main

Step 10: Enter credentials
   Username: balaji340
   Password: [Your GitHub Personal Access Token]

================================================================================
                    GETTING GITHUB PERSONAL ACCESS TOKEN
================================================================================

When git asks for password, you need a Personal Access Token (NOT your password).

Steps to get token:
   1. Go to: https://github.com/settings/tokens
   2. Click "Generate new token" → "Generate new token (classic)"
   3. Fill in:
      - Token name: "Chatbot Deployment"
      - Expiration: 90 days
   4. Check box: ☑ repo (full control of private repositories)
   5. Click "Generate token"
   6. COPY the token (shown only once!)
   7. Paste when git asks for password

The token will look like: ghp_1234567890abcdefghijklmnop

================================================================================
                         VERIFICATION
================================================================================

After running the script or manual commands:

✓ Check if files are on GitHub:
   1. Open: https://github.com/balaji340/chatbot
   2. You should see all your project files
   3. You should see the commit message you created

✓ If you see the files, SUCCESS! 🎉

================================================================================
                    EXPECTED OUTPUT
================================================================================

After running git push, you should see something like:

   Enumerating objects: 45, done.
   Counting objects: 100% (45/45), done.
   Delta compression using up to 8 threads
   Compressing objects: 100% (38/38), done.
   Writing objects: 100% (45/45), 1.23 MiB | 2.00 MiB/s, done.
   Total 45 (delta 5), reused 0 (delta 0), pack-reused 0
   remote: Resolving deltas: 100% (5/5), done.
   To https://github.com/balaji340/chatbot.git
    * [new branch]      main -> main
   Branch 'main' set up to track remote branch 'main' from 'origin'.

This means SUCCESS! ✓

================================================================================
                    TROUBLESHOOTING
================================================================================

❌ "git: command not found" or "git is not recognized"
   Solution: Git is not installed. Install from https://git-scm.com/download/win

❌ "fatal: could not read Username for 'https://github.com'"
   Solution: This is normal. Enter credentials:
      Username: balaji340
      Password: [Personal Access Token]

❌ "fatal: not a git repository"
   Solution: Run "git init" first

❌ "fatal: destination path already exists and is not an empty directory"
   Solution: Repository already exists. Either:
      - Delete .git folder: Remove-Item -Recurse -Force .git
      - Use different repo name
      - Clone first: git clone https://github.com/balaji340/chatbot.git

❌ "Permission denied (publickey)"
   Solution: Use HTTPS URL (which we are), not SSH

❌ "Repository not found"
   Solution: 
      - Verify URL: https://github.com/balaji340/chatbot.git
      - Make sure repository exists on GitHub
      - Check credentials

❌ "error: failed to push some refs to origin"
   Solution: The remote already has content. Try:
      git pull origin main --allow-unrelated-histories
      git push -u origin main

================================================================================
                    WHAT GETS UPLOADED
================================================================================

Files that WILL be uploaded:
   ✓ Django project files (settings.py, urls.py, etc.)
   ✓ Chatbot app (views.py, models.py, etc.)
   ✓ HTML templates
   ✓ Training data
   ✓ Procfile, requirements.txt, runtime.txt
   ✓ README and documentation

Files that WON'T be uploaded (protected by .gitignore):
   ✗ Virtual environment (.venv folder)
   ✗ Database files (db.sqlite3, database.sqlite3)
   ✗ Python cache (__pycache__)
   ✗ .env files
   ✗ IDE settings

This is good! We don't want to upload environment files.

================================================================================
                    AFTER UPLOADING TO GITHUB
================================================================================

Your repository link:
   https://github.com/balaji340/chatbot

Next step: DEPLOY from GitHub

Option 1: Railway (Recommended) ⭐
   1. Go to: https://railway.app
   2. Sign in with GitHub
   3. Click "New Project"
   4. Select "Deploy from GitHub repo"
   5. Choose: balaji340/chatbot
   6. Click "Deploy"
   
   Your deployed link: https://[project-name].up.railway.app

Option 2: Render
   1. Go to: https://render.com
   2. Click "New" → "Web Service"
   3. Connect: balaji340/chatbot
   4. Configure and deploy
   
   Your deployed link: https://[service-name].onrender.com

Option 3: Heroku
   1. Go to: https://heroku.com
   2. Connect GitHub: balaji340/chatbot
   3. Deploy
   
   Your deployed link: https://[app-name].herokuapp.com

================================================================================
                    QUICK SUMMARY
================================================================================

✓ Git installed from: https://git-scm.com/download/win
✓ Run script: .\push-to-github.ps1
✓ Enter credentials when prompted
✓ Verify at: https://github.com/balaji340/chatbot
✓ Deploy using Railway/Render/Heroku

You'll get TWO links:
   1. GitHub: https://github.com/balaji340/chatbot (code)
   2. Deployed: https://app-name.up.railway.app (live site)

================================================================================
                        SUPPORT
================================================================================

Scripts provided:
   - push-to-github.ps1 (PowerShell - Recommended)
   - push-to-github.bat (Batch)

Documentation:
   - PUSH_TO_GITHUB.md - Detailed manual guide
   - DEPLOYMENT.md - Deployment guide
   - DEPLOYMENT_STATUS.txt - Status summary
   - GITHUB_SETUP.md - GitHub setup guide

Links:
   - Git: https://git-scm.com/download/win
   - GitHub: https://github.com/balaji340/chatbot
   - Railway: https://railway.app
   - Render: https://render.com
   - Heroku: https://heroku.com

================================================================================
                    YOU'RE READY! 🚀
================================================================================

Step 1: Install Git
Step 2: Run script: .\push-to-github.ps1
Step 3: Success! Visit: https://github.com/balaji340/chatbot

Questions? See the documentation files in your project folder.

================================================================================
