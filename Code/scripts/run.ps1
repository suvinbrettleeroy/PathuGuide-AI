# PathGuide Run Script
# This script automates the startup process

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "   PathGuide - Career Guidance System" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-Not (Test-Path "venv")) {
    Write-Host "❌ Virtual environment not found!" -ForegroundColor Red
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✅ Virtual environment created!" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Check if dependencies are installed
Write-Host "Checking dependencies..." -ForegroundColor Yellow
$pipList = pip list
if ($pipList -notmatch "Flask") {
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    pip install -r requirements.txt
    Write-Host "✅ Dependencies installed!" -ForegroundColor Green
}

# Check if database exists
if (-Not (Test-Path "pathguide.db")) {
    Write-Host "❌ Database not found!" -ForegroundColor Red
    Write-Host "Initializing database..." -ForegroundColor Yellow
    python init_db.py
    Write-Host "✅ Database initialized!" -ForegroundColor Green
}

Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "   Starting PathGuide Server..." -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "🌐 Application will be available at:" -ForegroundColor Green
Write-Host "   http://127.0.0.1:5000" -ForegroundColor White
Write-Host ""
Write-Host "🔐 Admin Panel:" -ForegroundColor Yellow
Write-Host "   http://127.0.0.1:5000/admin-login" -ForegroundColor White
Write-Host "   Username: Darkknignt" -ForegroundColor White
Write-Host "   Password: Suv001" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""

# Run the application
python app.py
