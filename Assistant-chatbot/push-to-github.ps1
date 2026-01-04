# ============================================================
# Health Chatbot - GitHub Push Script (PowerShell)
# ============================================================
# Run this script to automatically push your project to GitHub

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Health Chatbot - GitHub Setup & Push" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
try {
    $gitVersion = git --version 2>$null
    Write-Host "✓ Git is installed: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ ERROR: Git is not installed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host "Then run this script again." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Navigate to project directory
$projectPath = "D:\project\health-chatbot"
if (-not (Test-Path $projectPath)) {
    Write-Host "✗ ERROR: Project folder not found at $projectPath" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Set-Location $projectPath
Write-Host "✓ Changed to project directory: $(Get-Location)" -ForegroundColor Green
Write-Host ""

# Initialize Git
Write-Host "[1/7] Initializing Git repository..." -ForegroundColor Yellow
git init | Out-Null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Git initialized" -ForegroundColor Green
} else {
    Write-Host "✗ ERROR: Failed to initialize git" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

# Configure Git user
Write-Host "[2/7] Configuring Git user..." -ForegroundColor Yellow
git config user.email "chatbot@health.app" | Out-Null
git config user.name "Health Chatbot Bot" | Out-Null
Write-Host "✓ Git user configured" -ForegroundColor Green
Write-Host ""

# Add all files
Write-Host "[3/7] Adding all files..." -ForegroundColor Yellow
git add . | Out-Null
Write-Host "✓ Files staged" -ForegroundColor Green
Write-Host ""

# Create initial commit
Write-Host "[4/7] Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit - Health Chatbot with Django and ChatterBot" 2>&1 | Out-Null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Initial commit created" -ForegroundColor Green
} else {
    Write-Host "✗ ERROR: Failed to commit files" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

# Rename branch to main
Write-Host "[5/7] Setting up main branch..." -ForegroundColor Yellow
git branch -M main | Out-Null
Write-Host "✓ Branch renamed to main" -ForegroundColor Green
Write-Host ""

# Add remote
Write-Host "[6/7] Adding GitHub remote..." -ForegroundColor Yellow
git remote add origin https://github.com/balaji340/chatbot.git 2>&1 | Out-Null
Write-Host "✓ Remote added" -ForegroundColor Green
Write-Host ""

# Push to GitHub
Write-Host "[7/7] Pushing to GitHub..." -ForegroundColor Yellow
Write-Host ""
Write-Host "NOTE: You may be prompted for credentials." -ForegroundColor Yellow
Write-Host "  Username: balaji340" -ForegroundColor Yellow
Write-Host "  Password: Your GitHub Personal Access Token" -ForegroundColor Yellow
Write-Host "  (Get token from: https://github.com/settings/tokens)" -ForegroundColor Yellow
Write-Host ""

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host "  ✓ SUCCESS! Project pushed to GitHub" -ForegroundColor Green
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Your repository is now available at:" -ForegroundColor Cyan
    Write-Host "  https://github.com/balaji340/chatbot" -ForegroundColor White
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Yellow
    Write-Host "  1. Visit: https://github.com/balaji340/chatbot" -ForegroundColor Yellow
    Write-Host "  2. Deploy using Railway: https://railway.app" -ForegroundColor Yellow
    Write-Host "  3. Connect GitHub repo and deploy" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "For detailed deployment guide, see: DEPLOYMENT.md" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
} else {
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Red
    Write-Host "  ✗ ERROR: Failed to push to GitHub" -ForegroundColor Red
    Write-Host "============================================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Possible reasons:" -ForegroundColor Yellow
    Write-Host "  - Internet connection issue" -ForegroundColor Yellow
    Write-Host "  - GitHub credentials incorrect" -ForegroundColor Yellow
    Write-Host "  - Repository already has content" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Troubleshooting:" -ForegroundColor Yellow
    Write-Host "  1. Check your internet connection" -ForegroundColor Yellow
    Write-Host "  2. Verify GitHub username: balaji340" -ForegroundColor Yellow
    Write-Host "  3. Get Personal Access Token: https://github.com/settings/tokens" -ForegroundColor Yellow
    Write-Host "  4. See PUSH_TO_GITHUB.md for detailed instructions" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}
