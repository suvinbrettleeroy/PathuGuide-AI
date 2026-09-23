"""
PathGuide - Project Overview and Architecture
"""

# ============================================
# PROJECT: PathGuide
# ============================================
# A comprehensive Machine Learning-based Career and Tamil Nadu Government 
# Exam Guidance System designed to help students and aspirants make 
# informed decisions about their future.

# ============================================
# SYSTEM ARCHITECTURE
# ============================================

"""
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                           │
│  (Bilingual: Tamil/English, Responsive, Bootstrap 5)           │
└────────────────────┬────────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────────┐
│                     FLASK APPLICATION                           │
│  ┌──────────────┬──────────────┬──────────────┬──────────────┐ │
│  │  Module 1    │  Module 2    │  Module 3    │  Module 4    │ │
│  │  Dashboard   │  Career Path │  Govt Exams  │  Admin Panel │ │
│  └──────────────┴──────────────┴──────────────┴──────────────┘ │
└────────────────────┬────────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────────┐
│                  BUSINESS LOGIC LAYER                           │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │           MACHINE LEARNING COMPONENTS                     │  │
│  │  ┌──────────────┬──────────────┬──────────────────────┐  │  │
│  │  │ Success      │ Recommendation│ Daily Plan          │  │  │
│  │  │ Predictor    │ Engine       │ Generator           │  │  │
│  │  └──────────────┴──────────────┴──────────────────────┘  │  │
│  │  ┌──────────────────────────────────────────────────────┐  │
│  │  │ Fitness Checker (BMI, Eligibility)                   │  │
│  │  └──────────────────────────────────────────────────────┘  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              UTILITY COMPONENTS                           │  │
│  │  - Language Manager  - Security Manager  - Analytics    │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────────┐
│                  DATA ACCESS LAYER                              │
│  (SQLAlchemy ORM)                                              │
└────────────────────┬────────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────────┐
│                   DATABASE (SQLite)                             │
│  ┌──────────────┬──────────────┬──────────────┬──────────────┐ │
│  │ User Data    │ Career Data  │ Exam Data    │ Admin Data   │ │
│  │ - Users      │ - Degrees    │ - Exams      │ - Logs       │ │
│  │ - Profiles   │ - Domains    │ - Jobs       │ - Analytics  │ │
│  │ - Sessions   │ - Roles      │ - Syllabus   │ - Settings   │ │
│  │              │ - Courses    │ - Coaching   │ - Versions   │ │
│  └──────────────┴──────────────┴──────────────┴──────────────┘ │
└─────────────────────────────────────────────────────────────────┘
"""

# ============================================
# MODULE BREAKDOWN
# ============================================

"""
MODULE 1: DASHBOARD (Entry Point)
├── Language Toggle (Tamil/English)
├── Path Selection
│   ├── Career Path
│   └── Government Exams
├── Location Detection (Optional)
├── Saved Profiles
└── Admin Login (Hidden)

MODULE 2: CAREER PATH
├── Input Form
│   ├── Profile Details (Degree, Department, etc.)
│   ├── Location
│   ├── Career Selection (Domain, Role)
│   ├── Study Availability
│   ├── Roadmap Duration
│   └── Budget
├── ML Processing
│   ├── Success Rate Prediction
│   ├── Weekly Study Plan Generation
│   └── Daily Task Generation
└── Output Display
    ├── Job Role Explanation
    ├── Learning Roadmap
    ├── Tools & Technologies
    ├── Course Recommendations
    ├── Project Suggestions
    ├── Salary Estimation
    ├── Top Companies
    ├── Weekly Study Plan
    ├── Daily Study Plan (Auto-updates)
    └── Success Rate Prediction

MODULE 3: GOVERNMENT EXAMS
├── Input Form
│   ├── Basic Details
│   ├── Location
│   ├── Exam & Job Selection
│   ├── Study Details
│   └── Fitness Data (Conditional)
├── Processing
│   ├── Fitness Eligibility Check
│   ├── Study Roadmap Generation
│   └── Daily Plan Generation
└── Output Display
    ├── Exam & Job Summary
    ├── Job Role Explanation
    ├── Complete Syllabus
    ├── Study Roadmap (6/12/18/24 months)
    ├── Fitness Plan (if applicable)
    ├── Coaching Guidance
    ├── Notes & Resources
    ├── Mock Test Plan
    ├── Application Process
    └── Daily Study Plan (Auto-updates)

MODULE 4: ADMIN PANEL
├── Authentication (Secure Login)
├── Dashboard Management
│   ├── Edit Content
│   ├── Add/Delete Elements
│   └── Reorder Sections
├── Career Path Management
│   ├── Manage Dropdowns (Degree→Dept→Domain→Role)
│   ├── Edit Output Content
│   └── Feature Toggles
├── Govt Exams Management
│   ├── Manage Exams & Jobs
│   ├── Edit Syllabus
│   └── Coaching Centers
├── Job Details Panel Management
├── Feature Control Panel
├── Language & Content Management
├── Analytics & Reports
├── Privacy & Data Management
└── System Settings
"""

# ============================================
# KEY TECHNOLOGIES
# ============================================

BACKEND = {
    'framework': 'Flask 2.3',
    'language': 'Python 3.8+',
    'orm': 'SQLAlchemy',
    'database': 'SQLite (Production: PostgreSQL/MySQL)',
}

MACHINE_LEARNING = {
    'library': 'Scikit-learn',
    'models': [
        'Random Forest Classifier (Success Prediction)',
        'Custom Recommendation Engine',
        'Daily Plan Generator',
        'Fitness Eligibility Checker'
    ],
    'data_processing': ['NumPy', 'Pandas']
}

FRONTEND = {
    'framework': 'Bootstrap 5.3',
    'languages': ['HTML5', 'CSS3', 'JavaScript'],
    'features': ['Responsive', 'Bilingual', 'Accessible']
}

SECURITY = {
    'authentication': 'Session-based',
    'password': 'Case-sensitive validation',
    'protection': ['CSRF', 'XSS', 'SQL Injection'],
    'logging': 'Admin activity audit trail'
}

# ============================================
# DATA FLOW
# ============================================

"""
CAREER PATH FLOW:
1. User selects Career Path
2. Fills input form (degree, domain, role, etc.)
3. System validates and stores data
4. ML model predicts success rate
5. Recommendation engine generates study plans
6. Daily plan generator creates today's task
7. Output displayed with all recommendations
8. Daily task auto-updates every 24 hours

GOVERNMENT EXAM FLOW:
1. User selects Government Exams
2. Fills input form (exam, job, etc.)
3. If fitness-required job → collect fitness data
4. System checks fitness eligibility
5. Generates month-by-month roadmap
6. Creates daily study task
7. Fetches coaching centers (location-based)
8. Output displayed with syllabus, roadmap, resources
9. Daily task auto-updates

ADMIN FLOW:
1. Admin accesses hidden login page
2. Enters case-sensitive credentials
3. System validates (max 3 attempts)
4. Session created (60-minute timeout)
5. Admin manages content via dashboard
6. All changes logged with audit trail
7. Changes can be previewed before publishing
8. Analytics dashboard shows usage stats
"""

# ============================================
# ML MODEL DETAILS
# ============================================

class SuccessPredictor:
    """
    Predicts career success probability
    
    Inputs:
    - study_hours_per_day: float
    - roadmap_duration: int (months)
    - department: string
    - domain: string
    - role: string
    - year_of_study: string
    
    Algorithm: Random Forest Classifier
    
    Output:
    - success_rate: int (0-100%)
    - rating: string (High/Medium/Low)
    - feedback: dict (en, ta)
    - suggestions: list of improvements
    """

class RecommendationEngine:
    """
    Generates personalized study plans
    
    Career Path:
    - Weekly breakdown for entire roadmap duration
    - Phase-based learning (Foundation → Intermediate → Specialization → Revision)
    - Task allocation by day
    - Resource recommendations
    
    Government Exams:
    - Monthly roadmap (6/12/18/24 months)
    - Subject-wise study plan
    - Mock test schedule
    - Revision strategy
    """

class DailyPlanGenerator:
    """
    Creates daily study tasks
    
    Features:
    - Auto-updates every 24 hours
    - Syncs with weekly/monthly plans
    - Provides specific topics for the day
    - Includes resources and checklist
    - Shows yesterday's task and tomorrow's preview
    - Tracks weekly progress
    
    Career Path:
    - Programming topics
    - Practice exercises
    - Project work
    
    Government Exams:
    - Subject rotation
    - Current affairs
    - Practice questions
    - Study tips
    """

class FitnessChecker:
    """
    Validates physical fitness eligibility
    
    Checks:
    - Height (gender-specific)
    - Weight (BMI calculation)
    - Running ability
    - Age eligibility
    
    Output:
    - Eligible/Not Eligible status
    - Comparison table
    - Improvement plan (if not eligible)
    - Weekly fitness routine
    - Diet recommendations
    - Timeline estimation
    """

# ============================================
# BILINGUAL SUPPORT
# ============================================

LANGUAGE_FEATURES = {
    'supported': ['English (en)', 'Tamil (ta)'],
    'toggle': 'Global language switch (persists across pages)',
    'content': 'All UI elements and output in both languages',
    'storage': 'Separate fields for en/ta content in database',
    'fallback': 'English if Tamil translation missing'
}

# ============================================
# SECURITY MEASURES
# ============================================

ADMIN_SECURITY = {
    'credentials': {
        'username': 'Darkknignt',  # Case-sensitive!
        'password': 'Suv001'        # Case-sensitive!
    },
    'login_attempts': {
        'max': 3,
        'lockout_duration': 1800,  # 30 minutes
        'ip_tracking': True
    },
    'session': {
        'timeout': 3600,        # 60 minutes
        'inactivity': 1800,     # 30 minutes
        'secure_cookie': True
    },
    'logging': {
        'all_attempts': True,
        'ip_address': True,
        'timestamp': True,
        'action_audit': True
    }
}

USER_PRIVACY = {
    'data_collection': 'Optional and minimal',
    'consent': 'Required for location',
    'storage': 'Encrypted database',
    'deletion': 'User-initiated anytime',
    'third_party': 'No sharing',
    'compliance': 'GDPR-ready'
}

# ============================================
# DEPLOYMENT CHECKLIST
# ============================================

PRODUCTION_SETUP = [
    '1. Change SECRET_KEY in config.py',
    '2. Update ADMIN_USERNAME and ADMIN_PASSWORD',
    '3. Switch to PostgreSQL/MySQL database',
    '4. Enable HTTPS',
    '5. Set FLASK_ENV=production',
    '6. Configure proper logging',
    '7. Set up backup system',
    '8. Enable rate limiting',
    '9. Configure email notifications (optional)',
    '10. Deploy to cloud (AWS/Azure/GCP)'
]

# ============================================
# FUTURE ENHANCEMENTS
# ============================================

FUTURE_FEATURES = [
    'User authentication (email/phone)',
    'Email/SMS notifications',
    'Mobile app (React Native/Flutter)',
    'Discussion forums',
    'Study groups',
    'Video tutorials integration',
    'Live coaching sessions',
    'Job application tracking',
    'Interview preparation module',
    'Alumni mentorship',
    'Gamification (badges, streaks)',
    'Social sharing',
    'Multi-language support (Hindi, etc.)',
    'Voice-based interaction',
    'AI chatbot for instant help'
]

# ============================================
# PROJECT STATISTICS
# ============================================

PROJECT_STATS = {
    'total_files': 25,
    'lines_of_code': '~5000+',
    'database_models': 15,
    'ml_models': 4,
    'api_endpoints': 15,
    'html_templates': 10,
    'languages': 2,
    'modules': 4
}

print(__doc__)
