"""
Admin Models
"""
from datetime import datetime
from .database import db

class AdminLog(db.Model):
    """Admin activity logging"""
    __tablename__ = 'admin_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    admin_username = db.Column(db.String(100))
    action = db.Column(db.String(100), nullable=False)
    entity_type = db.Column(db.String(50))  # Role, Exam, Job, etc.
    entity_id = db.Column(db.Integer)
    old_value = db.Column(db.Text)
    new_value = db.Column(db.Text)
    ip_address = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<AdminLog {self.action} at {self.timestamp}>'

class ContentVersion(db.Model):
    """Content version control"""
    __tablename__ = 'content_versions'
    
    id = db.Column(db.Integer, primary_key=True)
    entity_type = db.Column(db.String(50), nullable=False)
    entity_id = db.Column(db.Integer, nullable=False)
    version_number = db.Column(db.Integer, nullable=False)
    content_snapshot = db.Column(db.Text)  # JSON
    changed_by = db.Column(db.String(100))
    change_notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Version {self.entity_type} v{self.version_number}>'

class SystemSettings(db.Model):
    """System-wide settings"""
    __tablename__ = 'system_settings'
    
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.Text)
    data_type = db.Column(db.String(20))  # string, boolean, integer, json
    category = db.Column(db.String(50))  # ui, security, features, etc.
    description_en = db.Column(db.Text)
    description_ta = db.Column(db.Text)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_by = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<SystemSettings {self.key}>'

class FeatureToggle(db.Model):
    """Feature flags management"""
    __tablename__ = 'feature_toggles'
    
    id = db.Column(db.Integer, primary_key=True)
    feature_name = db.Column(db.String(100), unique=True, nullable=False)
    is_enabled = db.Column(db.Boolean, default=True)
    description_en = db.Column(db.Text)
    description_ta = db.Column(db.Text)
    affected_modules = db.Column(db.Text)  # JSON array
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_by = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<FeatureToggle {self.feature_name}: {self.is_enabled}>'

class AnalyticsData(db.Model):
    """Analytics and usage tracking"""
    __tablename__ = 'analytics_data'
    
    id = db.Column(db.Integer, primary_key=True)
    metric_type = db.Column(db.String(50), nullable=False)  # user_count, path_selection, etc.
    metric_category = db.Column(db.String(50))  # career, exam, feature
    metric_value = db.Column(db.String(100))
    count = db.Column(db.Integer, default=1)
    date = db.Column(db.Date, default=datetime.utcnow)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Analytics {self.metric_type}: {self.count}>'
