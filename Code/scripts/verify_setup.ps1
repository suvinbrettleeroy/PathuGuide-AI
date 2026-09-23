# PathGuide - Setup Verification Script
# This script checks if everything is set up correctly

Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "   PathGuide - Setup Verification" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

$allGood = $true

# Check 1: Python Installation
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found! Please install Python 3.8+" -ForegroundColor Red
    $allGood = $false
}

# Check 2: Project Files
Write-Host ""
Write-Host "Checking project files..." -ForegroundColor Yellow
$requiredFiles = @(
    "app.py",
    "config.py",
    "requirements.txt",
    "init_db.py",
    "README.md"
)

foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "✅ Found: $file" -ForegroundColor Green
    } else {
        Write-Host "❌ Missing: $file" -ForegroundColor Red
        $allGood = $false
    }
}

# Check 3: Directories
Write-Host ""
Write-Host "Checking directories..." -ForegroundColor Yellow
$requiredDirs = @("models", "ml", "utils", "templates")

foreach ($dir in $requiredDirs) {
    if (Test-Path $dir) {
        Write-Host "✅ Found: $dir/" -ForegroundColor Green
    } else {
        Write-Host "❌ Missing: $dir/" -ForegroundColor Red
        $allGood = $false
    }
}

# Check 4: Virtual Environment
Write-Host ""
Write-Host "Checking virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "✅ Virtual environment exists" -ForegroundColor Green
} else {
    Write-Host "⚠️  Virtual environment not found" -ForegroundColor Yellow
    Write-Host "   Run: python -m venv venv" -ForegroundColor Gray
}

# Check 5: Database
Write-Host ""
Write-Host "Checking database..." -ForegroundColor Yellow
if (Test-Path "pathguide.db") {
    Write-Host "✅ Database file exists" -ForegroundColor Green
} else {
    Write-Host "⚠️  Database not initialized" -ForegroundColor Yellow
    Write-Host "   Run: python init_db.py" -ForegroundColor Gray
}

# Summary
Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan

if ($allGood) {
    Write-Host "   ✅ ALL CHECKS PASSED!" -ForegroundColor Green
    Write-Host "================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Your PathGuide project is ready! 🎉" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Yellow
    Write-Host "1. Run: .\run.ps1" -ForegroundColor White
    Write-Host "2. Open: http://127.0.0.1:5000" -ForegroundColor White
    Write-Host ""
} else {
    Write-Host "   ⚠️  SOME ISSUES FOUND" -ForegroundColor Yellow
    Write-Host "================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Please fix the issues above and run this script again." -ForegroundColor Yellow
    Write-Host ""
}

Write-Host "For help, see: README.md or QUICKSTART.md" -ForegroundColor Gray
Write-Host ""
