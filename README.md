# PathGuide

**Career and Tamil Nadu Government Exam Guidance System**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-black)
![Language](https://img.shields.io/badge/Language-English%20%7C%20தமிழ்-orange)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

## About

PathGuide is a bilingual (English / தமிழ்) web app that helps students plan their future. Many students don't know which career suits their degree, or how to prepare for Tamil Nadu government exams. PathGuide gives them clear, personalized guidance in their own language.

It offers two paths:

- **Career Path:** pick a degree, department, domain and role, and get a detailed career plan with a study plan, courses, projects, internships and salary details.
- **TN Government Exams:** get preparation guidance for Tamil Nadu exams such as TNPSC and TNUSRB, with a preparation plan and a success estimate.

An admin dashboard lets staff manage feature toggles, the welcome banner, reports and backups.

## Highlights

- Bilingual interface: switch between English and Tamil at any time
- 1000 career roles across degrees, departments and domains
- Personalized plans based on the student's choices and location
- Responsive design for mobile, tablet and desktop


An admin dashboard lets staff manage feature toggles, the welcome banner and reports.

---

## Features

### Dashboard
- English / Tamil language toggle across the whole app
- Live location detection with Tamil Nadu district and city selection
- Path selection: Career Path or Government Exams
- Saved profiles: resume, view, rename and delete
- Resume last activity
- Data-deletion request option
- Configurable welcome banner (set from the admin panel)

### Career Path
- Cascading dropdowns: Degree → Department → Domain → Role
- Career plan generated from a dataset of 1000 roles
- Weekly study plan
- Recommended courses, projects and internships
- Salary information for the chosen role
- City-based guidance using the selected district
- Save and resume progress

### Government Exams
- Exam input form with qualification and preparation duration
- Exam preparation plan for Tamil Nadu exams (TNPSC, TNUSRB)
- Success-score estimate based on the preparation details
- Physical fitness check (BMI and eligibility) for uniformed services

### Admin Panel
- Login-protected dashboard with logout
- Feature toggles to turn modules on or off
- Welcome banner editor
- Report export
- Audit-log export
- Backup trigger
- Light and dark theme

### Machine Learning
- Success predictor (Random Forest)
- Recommendation engine for study plans and roadmaps
- Daily plan generator
- Fitness checker

### User Interface
- Fully bilingual interface (English and Tamil)
- Responsive layout for mobile, tablet and desktop
- Shared design system with a consistent brand and logo
- Light and dark theme on the admin dashboard
- Smooth page transitions and scroll animations


---

## Tech Stack

| Layer     | Technology                                    |
|-----------|-----------------------------------------------|
| Backend   | Python 3.8+, Flask                            |
| Data      | Python data modules + CSV role dataset        |
| ML / Data | scikit-learn, NumPy, Pandas, joblib           |
| Frontend  | Jinja2 templates, custom CSS/JS design system |
| Languages | English, Tamil                                |

---

## Project Structure

```
PathGuide/
├── README.md
├── index.html                  # Static GitHub Pages landing page
├── requirements.txt
│
└── Code/
    ├── app.py                  # Launcher: runs backend/app.py
    ├── requirements.txt        # Python dependencies
    ├── .env.example            # Example environment settings
    │
    ├── backend/
    │   ├── app.py                       # Flask app and routes
    │   ├── career_output_generator.py   # Builds the career plan
    │   ├── config.py                    # Configuration settings
    │   ├── init_db.py                   # Database seeding script
    │   ├── ml/                          # Success predictor, recommendation
    │   │                                #   engine, daily plan, fitness checker
    │   ├── models/                      # Database models
    │   └── utils/                       # Language, security, analytics helpers
    │
    ├── data/
    │   ├── career_data.py               # Degree → Dept → Domain → Role data
    │   ├── role_content.py              # Role content
    │   └── Career Path Roles.csv        # Role dataset
    │
    ├── frontend/
    │   ├── templates/                   # Jinja2 pages
    │   │   └── partials/                # Shared nav, footer, logo, modals
    │   └── static/
    │       ├── css/                     # pg-core, brand, page stylesheets
    │       ├── js/                      # pg-core, home, admin scripts
    │       └── img/                     # Brand logo and page imagery
    │
    ├── docs/                            # Project summary, quickstart, architecture
    └── scripts/                         # run.ps1, verify_setup.ps1
```

---

## Getting Started

### Prerequisites
- Python 3.8 or newer
- Git

### Installation

1. **Clone the repository and open the `Code` folder**
   ```powershell
   git clone https://github.com/<your-username>/PathGuide.git
   cd PathGuide\Code
   ```

2. **Create and activate a virtual environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```powershell
   python app.py
   ```
   Or use the helper script, which does steps 2–4 for you:
   ```powershell
   .\scripts\run.ps1
   ```

5. **Open it in your browser**
   - Main app: http://127.0.0.1:5000
   - Admin login: http://127.0.0.1:5000/admin-login

### Configuration
Copy `.env.example` to `.env` and set your own values. Set your own admin
credentials and a strong `SECRET_KEY`. Never commit real credentials.

---

## Routes

| Route                      | Purpose                     |
|----------------------------|-----------------------------|
| `/`                        | Dashboard                   |
| `/career/input`            | Career form                 |
| `/career/output`           | Career plan                 |
| `/exam/input`              | Exam form                   |
| `/exam/output`             | Exam preparation plan       |
| `/admin-login`, `/admin`   | Admin login and dashboard   |
| `/api/career/*`            | Dropdown data and progress  |

---

## Machine Learning Components

The `backend/ml/` package contains:

- **Success Predictor:** Random Forest–based success-rate estimate
- **Recommendation Engine:** study-plan and roadmap generation
- **Daily Plan Generator:** daily task generation
- **Fitness Checker:** BMI and eligibility checks for uniformed services

> **Status:** the running app currently uses the career data and generator
> modules directly. The database models, full ML pipeline and `init_db.py`
> are in the codebase but are still being integrated.

---

## Testing

```powershell
pytest
```

---

## Team

| Name                     | Role                                                                     |
|--------------------------|--------------------------------------------------------------------------|
| Suvin Brettlee Roy B     | Team Lead and ML Developer: core idea, system architecture, Flask backend, admin panel and UI/UX design |
| Duraimurugan K           | Data and ML Developer: data collection and preprocessing, success prediction and recommendation system |
| Brain Benton Nelson      | Tester and Documentation: output modules, testing, debugging and project documentation |

---

## Acknowledgments

- Tamil Nadu Public Service Commission (TNPSC)
- Tamil Nadu Uniformed Services Recruitment Board (TNUSRB)
- Flask community

---

## License

Educational Project. All Rights Reserved.

© 2026 PathGuide
