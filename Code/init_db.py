"""
Database Initialization Script
Populates the database with initial data
"""
from app import app, db
from models.career import (
    Degree, Department, Domain, Role, Tool, Course, Project, Company, Internship,
    role_tools, role_courses, role_projects, role_companies, role_internships
)
from models.exam import Exam, Job, Syllabus, CoachingCenter, FitnessStandard

def init_database():
    """Initialize database with sample data"""
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        print("Creating database tables...")
        
        # ==========================================
        # CAREER PATH DATA
        # ==========================================
        
        # Degrees
        degrees_data = [
            {'name_en': 'B.E / B.Tech', 'name_ta': 'பொறியியல் பட்டம்'},
            {'name_en': 'B.Sc', 'name_ta': 'அறிவியல் பட்டம்'},
            {'name_en': 'BCA', 'name_ta': 'கணினி பயன்பாடுகள் பட்டம்'},
            {'name_en': 'M.E / M.Tech', 'name_ta': 'முதுகலை பொறியியல்'},
            {'name_en': 'MCA', 'name_ta': 'முதுகலை கணினி பயன்பாடுகள்'},
        ]
        
        degrees = []
        for idx, deg_data in enumerate(degrees_data):
            deg = Degree(**deg_data, display_order=idx)
            db.session.add(deg)
            degrees.append(deg)
        
        db.session.commit()
        print(f"✓ Created {len(degrees)} degrees")
        
        # Departments
        be_btech = degrees[0]
        
        departments_data = [
            {'degree_id': be_btech.id, 'name_en': 'Computer Science & Engineering', 'name_ta': 'கணினி அறிவியல் பொறியியல்'},
            {'degree_id': be_btech.id, 'name_en': 'Information Technology', 'name_ta': 'தகவல் தொழில்நுட்பம்'},
            {'degree_id': be_btech.id, 'name_en': 'Electronics & Communication Engineering', 'name_ta': 'மின்னணுவியல் மற்றும் தொடர்பாடல் பொறியியல்'},
            {'degree_id': be_btech.id, 'name_en': 'Mechanical Engineering', 'name_ta': 'இயந்திர பொறியியல்'},
        ]
        
        departments = []
        for idx, dept_data in enumerate(departments_data):
            dept = Department(**dept_data, display_order=idx)
            db.session.add(dept)
            departments.append(dept)
        
        db.session.commit()
        print(f"✓ Created {len(departments)} departments")
        
        # Domains
        cse_dept = departments[0]
        
        domains_data = [
            {
                'department_id': cse_dept.id,
                'name_en': 'Software Development',
                'name_ta': 'மென்பொருள் மேம்பாடு',
                'description_en': 'Build software applications and systems',
                'description_ta': 'மென்பொருள் பயன்பாடுகள் மற்றும் அமைப்புகளை உருவாக்குதல்'
            },
            {
                'department_id': cse_dept.id,
                'name_en': 'Data Science & Analytics',
                'name_ta': 'தரவு அறிவியல் மற்றும் பகுப்பாய்வு',
                'description_en': 'Analyze data and derive insights',
                'description_ta': 'தரவை பகுப்பாய்வு செய்து நுண்ணறிவுகளைப் பெறுதல்'
            },
            {
                'department_id': cse_dept.id,
                'name_en': 'Web Development',
                'name_ta': 'வலை மேம்பாடு',
                'description_en': 'Create websites and web applications',
                'description_ta': 'இணையதளங்கள் மற்றும் வலை பயன்பாடுகளை உருவாக்குதல்'
            },
        ]
        
        domains = []
        for idx, dom_data in enumerate(domains_data):
            dom = Domain(**dom_data, display_order=idx)
            db.session.add(dom)
            domains.append(dom)
        
        db.session.commit()
        print(f"✓ Created {len(domains)} domains")
        
        # Roles
        software_dev_domain = domains[0]
        data_science_domain = domains[1]
        
        roles_data = [
            {
                'domain_id': software_dev_domain.id,
                'name_en': 'Full Stack Developer',
                'name_ta': 'முழு ஸ்டேக் உருவாக்குநர்',
                'description_en': 'Develops both frontend and backend of applications',
                'description_ta': 'பயன்பாடுகளின் முன்பக்கம் மற்றும் பின்பக்கம் இரண்டையும் உருவாக்குகிறது',
                'salary_india_entry_min': 300000,
                'salary_india_entry_max': 600000,
                'salary_india_mid_min': 800000,
                'salary_india_mid_max': 1500000,
                'salary_india_senior_min': 1800000,
                'salary_india_senior_max': 3500000
            },
            {
                'domain_id': data_science_domain.id,
                'name_en': 'Data Analyst',
                'name_ta': 'தரவு பகுப்பாய்வாளர்',
                'description_en': 'Analyzes data to help make business decisions',
                'description_ta': 'வணிக முடிவுகளை எடுக்க தரவை பகுப்பாய்வு செய்கிறது',
                'salary_india_entry_min': 350000,
                'salary_india_entry_max': 550000,
                'salary_india_mid_min': 700000,
                'salary_india_mid_max': 1200000,
                'salary_india_senior_min': 1500000,
                'salary_india_senior_max': 2500000
            },
        ]
        
        roles = []
        for idx, role_data in enumerate(roles_data):
            role = Role(**role_data, display_order=idx)
            db.session.add(role)
            roles.append(role)
        
        db.session.commit()
        print(f"✓ Created {len(roles)} roles")
        
        # ==========================================
        # GOVERNMENT EXAM DATA
        # ==========================================
        
        # Exams
        exams_data = [
            {
                'name_en': 'TNPSC Group I',
                'name_ta': 'TNPSC குழு I',
                'conducting_body': 'TNPSC',
                'exam_type': 'Group I',
                'description_en': 'Combined Civil Services Examination',
                'description_ta': 'ஒருங்கிணைந்த சிவில் சர்வீசஸ் தேர்வு',
                'official_website': 'https://www.tnpsc.gov.in'
            },
            {
                'name_en': 'TNPSC Group II',
                'name_ta': 'TNPSC குழு II',
                'conducting_body': 'TNPSC',
                'exam_type': 'Group II',
                'description_en': 'Non-Interview Posts',
                'description_ta': 'நேர்முகத்தேர்வு இல்லாத பதவிகள்',
                'official_website': 'https://www.tnpsc.gov.in'
            },
            {
                'name_en': 'TNPSC Group IV',
                'name_ta': 'TNPSC குழு IV',
                'conducting_body': 'TNPSC',
                'exam_type': 'Group IV',
                'description_en': 'Non-Interview Posts',
                'description_ta': 'நேர்முகத்தேர்வு இல்லாத பதவிகள்',
                'official_website': 'https://www.tnpsc.gov.in'
            },
            {
                'name_en': 'TNUSRB Police Constable',
                'name_ta': 'TNUSRB காவல் காப்பாளர்',
                'conducting_body': 'TNUSRB',
                'exam_type': 'Police',
                'description_en': 'Tamil Nadu Uniformed Services Recruitment',
                'description_ta': 'தமிழ்நாடு சீருடை சேவைகள் ஆட்சேர்ப்பு',
                'official_website': 'https://www.tnusrb.tn.gov.in'
            },
        ]
        
        exams = []
        for idx, exam_data in enumerate(exams_data):
            exam = Exam(**exam_data, display_order=idx)
            db.session.add(exam)
            exams.append(exam)
        
        db.session.commit()
        print(f"✓ Created {len(exams)} exams")
        
        # Jobs
        group1_exam = exams[0]
        group4_exam = exams[2]
        police_exam = exams[3]
        
        jobs_data = [
            {
                'exam_id': group1_exam.id,
                'name_en': 'Deputy Collector',
                'name_ta': 'துணை ஆட்சியர்',
                'department': 'Revenue',
                'grade': 'Group I',
                'description_en': 'Administrative position in revenue department',
                'description_ta': 'வருவாய் துறையில் நிர்வாக பதவி',
                'salary_scale': 'Level 22: ₹56,100 - ₹1,77,500',
                'fitness_required': False
            },
            {
                'exam_id': group4_exam.id,
                'name_en': 'Junior Assistant',
                'name_ta': 'இளைய உதவியாளர்',
                'department': 'Various',
                'grade': 'Group IV',
                'description_en': 'Clerical and office assistance work',
                'description_ta': 'எழுத்தர் மற்றும் அலுவலக உதவி வேலை',
                'salary_scale': 'Level 5: ₹19,500 - ₹62,000',
                'fitness_required': False
            },
            {
                'exam_id': police_exam.id,
                'name_en': 'Police Constable',
                'name_ta': 'காவல் காப்பாளர்',
                'department': 'Police',
                'grade': 'Constable',
                'description_en': 'Law enforcement and public safety',
                'description_ta': 'சட்ட அமலாக்கம் மற்றும் பொது பாதுகாப்பு',
                'salary_scale': 'Level 3: ₹19,500 - ₹62,000',
                'fitness_required': True
            },
        ]
        
        jobs = []
        for idx, job_data in enumerate(jobs_data):
            job = Job(**job_data, display_order=idx)
            db.session.add(job)
            jobs.append(job)
        
        db.session.commit()
        print(f"✓ Created {len(jobs)} jobs")
        
        # Fitness Standards (for Police Constable)
        police_job = jobs[2]
        
        fitness_data = [
            {
                'job_id': police_job.id,
                'gender': 'Male',
                'height_min': 170.0,
                'height_max': 195.0,
                'weight_min': 50.0,
                'weight_max': 85.0,
                'bmi_min': 18.5,
                'bmi_max': 25.0,
                'running_distance_km': 5.0,
                'running_time_minutes': 30
            },
            {
                'job_id': police_job.id,
                'gender': 'Female',
                'height_min': 159.0,
                'height_max': 185.0,
                'weight_min': 45.0,
                'weight_max': 75.0,
                'bmi_min': 18.5,
                'bmi_max': 25.0,
                'running_distance_km': 5.0,
                'running_time_minutes': 35
            },
        ]
        
        for fitness in fitness_data:
            fit_std = FitnessStandard(**fitness)
            db.session.add(fit_std)
        
        db.session.commit()
        print("✓ Created fitness standards")
        
        print("\n✅ Database initialized successfully!")
        print(f"   - {len(degrees)} degrees")
        print(f"   - {len(departments)} departments")
        print(f"   - {len(domains)} domains")
        print(f"   - {len(roles)} roles")
        print(f"   - {len(exams)} exams")
        print(f"   - {len(jobs)} jobs")

if __name__ == '__main__':
    init_database()
