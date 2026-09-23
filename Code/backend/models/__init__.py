"""
Database Models Package
"""
from .database import db, init_db
from .user import User, UserProfile, SavedProfile
from .career import (
    Degree, Department, Domain, Role, 
    Course, Project, Tool, Company, Internship
)
from .exam import (
    Exam, Job, Syllabus, CoachingCenter,
    FitnessStandard, MockTest
)
from .admin import (
    AdminLog, ContentVersion, SystemSettings,
    FeatureToggle, AnalyticsData
)

__all__ = [
    'db', 'init_db',
    'User', 'UserProfile', 'SavedProfile',
    'Degree', 'Department', 'Domain', 'Role',
    'Course', 'Project', 'Tool', 'Company', 'Internship',
    'Exam', 'Job', 'Syllabus', 'CoachingCenter',
    'FitnessStandard', 'MockTest',
    'AdminLog', 'ContentVersion', 'SystemSettings',
    'FeatureToggle', 'AnalyticsData'
]
