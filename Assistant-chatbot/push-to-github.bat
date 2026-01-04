@echo off
REM ============================================================
REM Health Chatbot - GitHub Push Script
REM ============================================================
REM This script will push your project to GitHub

setlocal enabledelayedexpansion

echo ============================================================
echo   Health Chatbot - GitHub Setup & Push
echo ============================================================
echo.

REM Check if Git is installed
where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Git is not installed!
    echo.
    echo Please install Git from: https://git-scm.com/download/win
    echo Then run this script again.
    echo.
    pause
    exit /b 1
)

echo ✓ Git is installed
echo.

REM Change to project directory
cd /d D:\project\health-chatbot
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Could not navigate to project folder
    pause
    exit /b 1
)

echo ✓ Changed to project directory: %CD%
echo.

REM Initialize Git
echo [1/7] Initializing Git repository...
git init
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to initialize git
    pause
    exit /b 1
)
echo ✓ Git initialized
echo.

REM Configure Git user
echo [2/7] Configuring Git user...
git config user.email "chatbot@health.app"
git config user.name "Health Chatbot Bot"
echo ✓ Git user configured
echo.

REM Add all files
echo [3/7] Adding all files...
git add .
echo ✓ Files staged
echo.

REM Create initial commit
echo [4/7] Creating initial commit...
git commit -m "Initial commit - Health Chatbot with Django and ChatterBot"
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to commit files
    pause
    exit /b 1
)
echo ✓ Initial commit created
echo.

REM Rename branch to main
echo [5/7] Setting up main branch...
git branch -M main
echo ✓ Branch renamed to main
echo.

REM Add remote
echo [6/7] Adding GitHub remote...
git remote add origin https://github.com/balaji340/chatbot.git
echo ✓ Remote added
echo.

REM Push to GitHub
echo [7/7] Pushing to GitHub...
echo.
echo NOTE: You may be prompted for credentials.
echo Username: balaji340
echo Password: Your GitHub Personal Access Token (from https://github.com/settings/tokens)
echo.
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ============================================================
    echo   ✓ SUCCESS! Project pushed to GitHub
    echo ============================================================
    echo.
    echo Your repository is now available at:
    echo   https://github.com/balaji340/chatbot
    echo.
    echo Next steps:
    echo   1. Visit: https://github.com/balaji340/chatbot
    echo   2. Deploy using Railway: https://railway.app
    echo   3. Connect GitHub repo and deploy
    echo.
    pause
) else (
    echo.
    echo ============================================================
    echo   ERROR: Failed to push to GitHub
    echo ============================================================
    echo.
    echo Possible reasons:
    echo   - Internet connection issue
    echo   - GitHub credentials incorrect
    echo   - Repository already has content
    echo.
    pause
    exit /b 1
)
