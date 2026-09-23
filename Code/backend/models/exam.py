"""
Government Exam Models
"""
from datetime import datetime
from .database import db

class Exam(db.Model):
    """Tamil Nadu Government Exams"""
    __tablename__ = 'exams'
    
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(200), nullable=False)
    name_ta = db.Column(db.String(200))
    conducting_body = db.Column(db.String(100))  # TNPSC, TNUSRB, TRB, MRB
    exam_type = db.Column(db.String(50))  # Group I, Group II, etc.
    description_en = db.Column(db.Text)
    description_ta = db.Column(db.Text)
    official_website = db.Column(db.String(200))
    notification_frequency = db.Column(db.String(50))
    display_order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    jobs = db.relationship('Job', backref='exam', lazy=True)
    syllabus = db.relationship('Syllabus', backref='exam', lazy=True)
    
    def __repr__(self):
        return f'<Exam {self.name_en}>'

class Job(db.Model):
    """Government job positions"""
    __tablename__ = 'jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'), nullable=False)
    
    name_en = db.Column(db.String(200), nullable=False)
    name_ta = db.Column(db.String(200))
    job_code = db.Column(db.String(50))
    department = db.Column(db.String(100))
    grade = db.Column(db.String(50))
    
    # Job details
    description_en = db.Column(db.Text)
    description_ta = db.Column(db.Text)
    responsibilities_en = db.Column(db.Text)  # JSON
    responsibilities_ta = db.Column(db.Text)
    work_nature_en = db.Column(db.Text)
    work_nature_ta = db.Column(db.Text)
    career_growth_en = db.Column(db.Text)
    career_growth_ta = db.Column(db.Text)
    
    # Salary and benefits
    salary_scale = db.Column(db.String(100))
    benefits_en = db.Column(db.Text)  # JSON
    benefits_ta = db.Column(db.Text)
    
    # Requirements
    educational_requirement_en = db.Column(db.Text)
    educational_requirement_ta = db.Column(db.Text)
    age_limit_min = db.Column(db.Integer)
    age_limit_max = db.Column(db.Integer)
    
    # Fitness requirement
    fitness_required = db.Column(db.Boolean, default=False)
    
    # Application details
    application_frequency = db.Column(db.String(50))
    total_posts_approx = db.Column(db.Integer)
    
    display_order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    fitness_standards = db.relationship('FitnessStandard', backref='job', lazy=True)
    
    def __repr__(self):
        return f'<Job {self.name_en}>'

class Syllabus(db.Model):
    """Exam syllabus"""
    __tablename__ = 'syllabus'
    
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'), nullable=False)
    
    paper_number = db.Column(db.Integer, default=1)
    paper_name_en = db.Column(db.String(200))
    paper_name_ta = db.Column(db.String(200))
    
    subject_name_en = db.Column(db.String(200), nullable=False)
    subject_name_ta = db.Column(db.String(200))
    
    topics_en = db.Column(db.Text)  # JSON array
    topics_ta = db.Column(db.Text)
    
    weightage = db.Column(db.Integer)
    total_marks = db.Column(db.Integer)
    
    display_order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<Syllabus {self.subject_name_en}>'

class CoachingCenter(db.Model):
    """Coaching centers"""
    __tablename__ = 'coaching_centers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    
    # Location
    district = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50))
    address = db.Column(db.Text)
    
    # Contact
    phone = db.Column(db.String(20))
    website = db.Column(db.String(200))
    email = db.Column(db.String(100))
    
    # Details
    specialization = db.Column(db.Text)  # JSON - exams covered
    batch_timings = db.Column(db.Text)
    fees_range = db.Column(db.String(100))
    mode = db.Column(db.String(20))  # Online, Offline, Hybrid
    
    # Verification
    is_verified = db.Column(db.Boolean, default=False)
    rating = db.Column(db.Float)
    
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<CoachingCenter {self.name}>'

class FitnessStandard(db.Model):
    """Physical fitness standards"""
    __tablename__ = 'fitness_standards'
    
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    
    gender = db.Column(db.String(10), nullable=False)  # Male, Female
    
    # Height requirements (in cm)
    height_min = db.Column(db.Float)
    height_max = db.Column(db.Float)
    
    # Weight requirements (in kg)
    weight_min = db.Column(db.Float)
    weight_max = db.Column(db.Float)
    
    # BMI requirements
    bmi_min = db.Column(db.Float)
    bmi_max = db.Column(db.Float)
    
    # Running requirements
    running_distance_km = db.Column(db.Float)
    running_time_minutes = db.Column(db.Integer)
    
    # Other tests (JSON)
    other_tests = db.Column(db.Text)  # JSON
    
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<FitnessStandard {self.job.name_en} - {self.gender}>'

class MockTest(db.Model):
    """Mock test resources"""
    __tablename__ = 'mock_tests'
    
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'))
    
    name = db.Column(db.String(200), nullable=False)
    platform = db.Column(db.String(100))
    url = db.Column(db.String(300))
    test_type = db.Column(db.String(50))  # Subject-wise, Combined, Full-length
    cost_type = db.Column(db.String(20))  # Free, Paid
    description_en = db.Column(db.Text)
    description_ta = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<MockTest {self.name}>'
