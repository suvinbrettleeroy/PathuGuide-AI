# PathGuide

## Complete Machine Learning-Based Career and Tamil Nadu Government Exam Guidance System

### 🎯 Features

- **Module 1: Dashboard** - Entry point with language toggle and path selection
- **Module 2: Career Path** - Personalized career guidance with ML predictions
- **Module 3: Government Exams** - Complete TN exam preparation with fitness checks
- **Module 4: Admin Panel** - Secure content management system

### 🛠️ Technology Stack

- **Backend:** Python 3.8+, Flask 2.3
- **Database:** SQLAlchemy, SQLite
- **Machine Learning:** Scikit-learn, NumPy, Pandas
- **Frontend:** Bootstrap 5, JavaScript
- **Languages:** English, Tamil (Bilingual)

### 📦 Installation

1. **Clone the repository:**
```bash
cd "C:\Users\ASUS\Desktop\Projects\PathGuide\Code"
```

2. **Create virtual environment:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. **Install dependencies:**
```powershell
pip install -r requirements.txt
```

4. **Initialize database:**
```powershell
python init_db.py
```

5. **Run the application:**
```powershell
python app.py
```

6. **Access the application:**
- Main App: http://127.0.0.1:5000
- Admin Panel: http://127.0.0.1:5000/admin-login
  - Username: `Darkknignt` (case-sensitive)
  - Password: `Suv001` (case-sensitive)

### 📁 Project Structure

```
PathGuide/
├── app.py                  # Main Flask application
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── init_db.py             # Database initialization
│
├── models/                 # Database models
│   ├── __init__.py
│   ├── database.py
│   ├── user.py            # User models
│   ├── career.py          # Career path models
│   ├── exam.py            # Government exam models
│   └── admin.py           # Admin models
│
├── ml/                     # Machine Learning components
│   ├── __init__.py
│   ├── success_predictor.py      # Success rate prediction
│   ├── recommendation_engine.py   # Study plan generation
│   ├── daily_plan_generator.py   # Daily task generator
│   └── fitness_checker.py        # Fitness eligibility checker
│
├── utils/                  # Utility functions
│   ├── __init__.py
│   ├── language.py        # Language management
│   ├── security.py        # Security features
│   └── analytics.py       # Analytics tracking
│
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html         # Dashboard
│   ├── admin_login.html   # Admin login
│   ├── career_input.html  # Career input form
│   ├── career_output.html # Career guidance output
│   ├── exam_input.html    # Exam input form
│   └── exam_output.html   # Exam preparation output
│
└── models/                # Trained ML models (auto-generated)
    └── success_predictor.pkl
```

### 🚀 Key Features

#### Module 1: Dashboard
- ✅ Bilingual support (Tamil/English)
- ✅ Language toggle
- ✅ Live location detection
- ✅ Path selection (Career/Govt Exam)
- ✅ Saved profiles
- ✅ Hidden admin access

#### Module 2: Career Path
- ✅ Smart form with filtered dropdowns
- ✅ ML-based success prediction
- ✅ Weekly study plan generation
- ✅ Daily task automation
- ✅ Salary estimation (India + 7 countries)
- ✅ Course recommendations
- ✅ Project suggestions
- ✅ Internship matching

#### Module 3: Government Exams
- ✅ Exam-Job mapping
- ✅ Complete syllabus display
- ✅ Study roadmap (6/12/18/24 months)
- ✅ Physical fitness checker
- ✅ Daily study plan
- ✅ Coaching center recommendations
- ✅ Mock test plans

#### Module 4: Admin Panel
- ✅ Secure login (case-sensitive)
- ✅ Content management
- ✅ Analytics dashboard
- ✅ Feature toggles
- ✅ Audit logging
- ✅ Version control

### 🔐 Security Features

- Case-sensitive login credentials
- Maximum 3 login attempts
- 30-minute account lockout
- Session timeout (60 minutes)
- Activity logging
- CSRF protection
- XSS prevention

### 📊 Machine Learning Models

1. **Success Predictor:** Random Forest Classifier
   - Predicts success rate based on study hours, roadmap duration, and alignment
   - Provides personalized feedback and suggestions

2. **Recommendation Engine:**
   - Generates weekly study plans
   - Creates exam preparation roadmaps
   - Adapts to user preferences

3. **Daily Plan Generator:**
   - Auto-generates daily tasks
   - Updates every 24 hours
   - Tracks progress

4. **Fitness Checker:**
   - BMI calculation
   - Eligibility verification
   - Improvement plan generation

### 🌐 Bilingual Support

- All UI elements in Tamil and English
- Dynamic language switching
- Content stored in both languages
- Translation management system

### 📱 Responsive Design

- Mobile-friendly interface
- Tablet optimized
- Desktop enhanced
- Cross-browser compatible

### 🔄 Data Privacy

- Optional data collection
- User consent required
- Easy data deletion
- No third-party sharing
- GDPR compliant

### 🧪 Testing

Run tests:
```powershell
pytest
```

### 📖 Documentation

- User Manual: `docs/user_manual.md`
- Admin Manual: `docs/admin_manual.md`
- API Documentation: `docs/api.md`
- Development Guide: `docs/development.md`

### 🤝 Contributing

This is a college project. For queries, contact the project team.

### 📄 License

Educational Project - All Rights Reserved

### 👥 Team
1. Suvin Brettlee Roy B - Lead, Core idea, System design and architecture planning, Developer, Designed UI/UX
2. Duraimurugan K - Data Preprocessing, Data collection, Developer, Worked on success prediction and recommendation system 
3. Brain Benton Nelson - Tester, Documentation, Developed output modules, Debugging

### 🙏 Acknowledgments

- Tamil Nadu Public Service Commission (TNPSC)
- Tamil Nadu Uniformed Services Recruitment Board (TNUSRB)
- Bootstrap Team
- Flask Community

---

**© 2026 PathGuide. All rights reserved.**
