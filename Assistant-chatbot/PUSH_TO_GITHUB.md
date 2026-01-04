================================================================================
                   PUSH TO GITHUB - MANUAL STEPS
================================================================================

Your GitHub Repository:
   https://github.com/balaji340/chatbot.git

Your Project Location:
   D:\project\health-chatbot

================================================================================
                    STEP 1: INSTALL GIT FOR WINDOWS
================================================================================

1. Download Git for Windows:
   https://git-scm.com/download/win

2. Run the installer (Git-2.x.x-64-bit.exe)

3. Follow the installation wizard:
   - Accept license
   - Use default installation path
   - Use default options (click "Next")
   - Click "Install"
   - Click "Finish"

4. Restart PowerShell (close and open new window)

5. Verify installation:
   git --version
   (should show: git version 2.x.x.windows.x)

================================================================================
              STEP 2: OPEN POWERSHELL IN PROJECT FOLDER
================================================================================

1. Navigate to your project:
   cd D:\project\health-chatbot

2. Verify you're in the right folder:
   ls  (should show your project files)

================================================================================
                STEP 3: INITIALIZE GIT REPOSITORY
================================================================================

Run these commands in PowerShell (one at a time):

   git init

   git config user.email "your-email@gmail.com"
   
   git config user.name "Your Name"

   git add .

   git commit -m "Initial commit - Health Chatbot with Django and ChatterBot"

   git branch -M main

   git remote add origin https://github.com/balaji340/chatbot.git

   git push -u origin main

When prompted for username/password, use:
   - Username: your GitHub username (balaji340)
   - Password: Your GitHub Personal Access Token (NOT your password)

================================================================================
                   GETTING GITHUB PERSONAL ACCESS TOKEN
================================================================================

If you don't have a Personal Access Token:

1. Go to: https://github.com/settings/tokens

2. Click "Generate new token"

3. Name: "Chatbot Deployment"

4. Check boxes:
   ☑ repo (full control of private repositories)

5. Click "Generate token"

6. COPY the token (you'll only see it once!)

7. When git asks for password, paste this token

================================================================================
                        EXPECTED RESULT
================================================================================

After running git push, you should see:
   Enumerating objects...
   Counting objects...
   Compressing objects...
   Writing objects...
   ...
   To https://github.com/balaji340/chatbot.git
    * [new branch]      main -> main
   Branch 'main' set up to track remote branch 'main' from 'origin'.

Then visit: https://github.com/balaji340/chatbot
You'll see all your project files uploaded!

================================================================================
                   TROUBLESHOOTING
================================================================================

❌ "git: command not found"
   → Git is not installed. Follow Step 1 above.
   → After installing, restart PowerShell.

❌ "fatal: could not read Username"
   → This is normal. Enter your GitHub credentials:
   Username: balaji340
   Password: [Your Personal Access Token]

❌ "Repository not found"
   → Check URL is correct: https://github.com/balaji340/chatbot.git
   → Make sure the repository is empty or clone first

❌ "Permission denied (publickey)"
   → Use HTTPS URL (the one provided) not SSH
   → Or set up SSH keys: https://docs.github.com/en/authentication

❌ "fatal: destination path already exists"
   → Remove .git folder: Remove-Item -Recurse -Force .git
   → Then try again

================================================================================
                   QUICK SUMMARY
================================================================================

1. Install Git: https://git-scm.com/download/win
2. Restart PowerShell
3. cd D:\project\health-chatbot
4. Run the git commands from Step 3 above
5. Visit: https://github.com/balaji340/chatbot
6. Done! All files are now on GitHub

================================================================================
                    AFTER PUSHING TO GITHUB
================================================================================

Your GitHub repository link:
   https://github.com/balaji340/chatbot

To deploy from this repository:

Option 1: Railway (Recommended)
   1. Go to: https://railway.app
   2. Sign in with GitHub
   3. New Project → Deploy from GitHub repo
   4. Select: balaji340/chatbot
   5. Deploy!
   Link will be: https://[app-name].up.railway.app

Option 2: Render
   1. Go to: https://render.com
   2. New Web Service
   3. Connect GitHub repo: balaji340/chatbot
   4. Configure and deploy
   Link will be: https://[service-name].onrender.com

================================================================================
