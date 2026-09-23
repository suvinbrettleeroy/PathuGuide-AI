"""
Career Path Models
"""
from datetime import datetime
from .database import db

class Degree(db.Model):
    """Degree types"""
    __tablename__ = 'degrees'
    
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(100), nullable=False)
    name_ta = db.Column(db.String(100))
    display_order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    
    departments = db.relationship('Department', backref='degree', lazy=True)
    
    def __repr__(self):
        return f'<Degree {self.name_en}>'

class Department(db.Model):
    """Departments/Specializations"""
    __tablename__ = 'departments'
    
    id = db.Column(db.Integer, primary_key=True)
    degree_id = db.Column(db.Integer, db.ForeignKey('degrees.id'), nullable=False)
    name_en = db.Column(db.String(100), nullable=False)
    name_ta = db.Column(db.String(100))
    display_order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    
    domains = db.relationship('Domain', backref='department', lazy=True)
    
    def __repr__(self):
        return f'<Department {self.name_en}>'

class Domain(db.Model):
    """Career domains"""
    __tablename__ = 'domains'
    
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    name_en = db.Column(db.String(100), nullable=False)
    name_ta = db.Column(db.String(100))
    description_en = db.Column(db.Text)
    description_ta = db.Column(db.Text)
    display_order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    
    roles = db.relationship('Role', backref='domain', lazy=True)
    
    def __repr__(self):
        return f'<Domain {self.name_en}>'

class Role(db.Model):
    """Job roles"""
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    domain_id = db.Column(db.Integer, db.ForeignKey('domains.id'), nullable=False)
    name_en = db.Column(db.String(100), nullable=False)
    name_ta = db.Column(db.String(100))
    
    # Role explanation
    description_en = db.Column(db.Text)
    description_ta = db.Column(db.Text)
    responsibilities_en = db.Column(db.Text)  # JSON array
    responsibilities_ta = db.Column(db.Text)
    work_environment_en = db.Column(db.Text)
    work_environment_ta = db.Column(db.Text)
    
    # Salary ranges
    salary_india_entry_min = db.Column(db.Integer)
    salary_india_entry_max = db.Column(db.Integer)
    salary_india_mid_min = db.Column(db.Integer)
    salary_india_mid_max = db.Column(db.Integer)
    salary_india_senior_min = db.Column(db.Integer)
    salary_india_senior_max = db.Column(db.Integer)
    
    # International salaries (JSON)
    salary_international = db.Column(db.Text)  # JSON
    
    # Skills required (JSON arrays)
    core_skills_en = db.Column(db.Text)
    core_skills_ta = db.Column(db.Text)
    supporting_skills_en = db.Column(db.Text)
    supporting_skills_ta = db.Column(db.Text)
    
    display_order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    tools = db.relationship('Tool', secondary='role_tools', backref='roles')
    courses = db.relationship('Course', secondary='role_courses', backref='roles')
    projects = db.relationship('Project', secondary='role_projects', backref='roles')
    companies = db.relationship('Company', secondary='role_companies', backref='roles')
    internships = db.relationship('Internship', secondary='role_internships', backref='roles')
    
    def __repr__(self):
        return f'<Role {self.name_en}>'

class Tool(db.Model):
    """Tools and technologies"""
    __tablename__ = 'tools'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description_en = db.Column(db.Text)
    description_ta = db.Column(db.Text)
    category = db.Column(db.String(50))  # Development, Framework, Platform, etc.
    official_url = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<Tool {self.name}>'

class Course(db.Model):
    """Course recommendations"""
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    platform = db.Column(db.String(100))  # Coursera, Udemy, etc.
    duration_weeks = db.Column(db.Integer)
    level = db.Column(db.String(20))  # Beginner, Intermediate, Advanced
    cost_type = db.Column(db.String(20))  # Free, Paid
    cost_amount = db.Column(db.Integer)
    language = db.Column(db.String(20))
    url = db.Column(db.String(300))
    description_en = db.Column(db.Text)
    description_ta = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<Course {self.name}>'

class Project(db.Model):
    """Project suggestions"""
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(200), nullable=False)
    name_ta = db.Column(db.String(200))
    description_en = db.Column(db.Text)
    description_ta = db.Column(db.Text)
    difficulty = db.Column(db.String(20))  # Beginner, Intermediate, Advanced
    duration_weeks = db.Column(db.Integer)
    skills_used = db.Column(db.Text)  # JSON array
    tech_stack = db.Column(db.Text)  # JSON array
    tutorial_url = db.Column(db.String(300))
    github_url = db.Column(db.String(300))
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<Project {self.name_en}>'

class Company(db.Model):
    """Hiring companies"""
    __tablename__ = 'companies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    company_type = db.Column(db.String(50))  # MNC, Startup, Product, Service
    size = db.Column(db.String(50))
    career_url = db.Column(db.String(300))
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<Company {self.name}>'

class Internship(db.Model):
    """Internship opportunities"""
    __tablename__ = 'internships'
    
    id = db.Column(db.Integer, primary_key=True)
    organization = db.Column(db.String(200), nullable=False)
    duration_months = db.Column(db.Integer)
    stipend_type = db.Column(db.String(20))  # Free, Paid
    stipend_amount_min = db.Column(db.Integer)
    stipend_amount_max = db.Column(db.Integer)
    skills_required = db.Column(db.Text)  # JSON array
    description_en = db.Column(db.Text)
    description_ta = db.Column(db.Text)
    application_url = db.Column(db.String(300))
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<Internship {self.organization}>'

# Association tables
role_tools = db.Table('role_tools',
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True),
    db.Column('tool_id', db.Integer, db.ForeignKey('tools.id'), primary_key=True)
)

role_courses = db.Table('role_courses',
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True)
)

role_projects = db.Table('role_projects',
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('projects.id'), primary_key=True)
)

role_companies = db.Table('role_companies',
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True),
    db.Column('company_id', db.Integer, db.ForeignKey('companies.id'), primary_key=True)
)

role_internships = db.Table('role_internships',
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True),
    db.Column('internship_id', db.Integer, db.ForeignKey('internships.id'), primary_key=True)
)
