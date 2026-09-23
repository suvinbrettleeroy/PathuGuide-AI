"""
User Models
"""
from datetime import datetime
from .database import db

class User(db.Model):
    """User session tracking"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), unique=True, nullable=False)
    language = db.Column(db.String(5), default='en')  # en or ta
    location_enabled = db.Column(db.Boolean, default=False)
    district = db.Column(db.String(50))
    city = db.Column(db.String(50))
    selected_path = db.Column(db.String(20))  # career or govt_exam
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_activity = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    profiles = db.relationship('SavedProfile', backref='user', lazy=True, cascade='all, delete-orphan')
    career_profile = db.relationship('UserProfile', backref='user', uselist=False, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.session_id}>'

class UserProfile(db.Model):
    """User profile data (career or exam)"""
    __tablename__ = 'user_profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Common fields
    name = db.Column(db.String(100))
    degree = db.Column(db.String(50))
    department = db.Column(db.String(100))
    college = db.Column(db.String(200))
    
    # Career Path specific
    year_of_study = db.Column(db.String(20))
    semester = db.Column(db.String(20))
    preferred_job_location = db.Column(db.String(50))
    preferred_work_language = db.Column(db.String(50))
    selected_domain = db.Column(db.String(100))
    selected_role = db.Column(db.String(100))
    study_hours_per_day = db.Column(db.String(20))
    roadmap_duration = db.Column(db.Integer)  # months
    budget = db.Column(db.String(20))
    
    # Government Exam specific
    degree_completed = db.Column(db.Boolean)
    expected_completion_date = db.Column(db.Date)
    study_material_language = db.Column(db.String(50))
    selected_exam = db.Column(db.String(100))
    selected_job = db.Column(db.String(100))
    coaching_preference = db.Column(db.String(50))
    mock_tests_required = db.Column(db.Boolean)
    
    # Fitness data (conditional)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    height = db.Column(db.Float)  # cm
    weight = db.Column(db.Float)  # kg
    running_ability = db.Column(db.String(100))
    fitness_eligible = db.Column(db.Boolean)
    
    # Metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<UserProfile {self.name}>'

class SavedProfile(db.Model):
    """Saved user profiles for resume functionality"""
    __tablename__ = 'saved_profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    profile_name = db.Column(db.String(100), nullable=False)
    path_type = db.Column(db.String(20), nullable=False)  # career or govt_exam
    progress_stage = db.Column(db.String(50))  # input, output, etc.
    progress_percentage = db.Column(db.Integer, default=0)
    
    # Store profile data as JSON
    profile_data = db.Column(db.Text)  # JSON string
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_accessed = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<SavedProfile {self.profile_name}>'
