"""
PathGuide Configuration
"""
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    FLASK_APP = os.getenv('FLASK_APP', 'app.py')
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///pathguide.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=int(os.getenv('SESSION_TIMEOUT', 3600)))
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Admin Credentials (CASE-SENSITIVE)
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'Darkknignt')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'Suv001')
    
    # Security
    MAX_LOGIN_ATTEMPTS = int(os.getenv('MAX_LOGIN_ATTEMPTS', 3))
    LOCKOUT_DURATION = int(os.getenv('LOCKOUT_DURATION', 1800))  # 30 minutes
    
    # ML Configuration
    ML_MODEL_PATH = os.getenv('ML_MODEL_PATH', 'models/')
    PREDICTION_THRESHOLD = float(os.getenv('PREDICTION_THRESHOLD', 0.75))
    
    # Feature Flags
    ENABLE_LOCATION = os.getenv('ENABLE_LOCATION', 'True').lower() == 'true'
    ENABLE_FITNESS_MODULE = os.getenv('ENABLE_FITNESS_MODULE', 'True').lower() == 'true'
    ENABLE_ML_PREDICTIONS = os.getenv('ENABLE_ML_PREDICTIONS', 'True').lower() == 'true'
    ENABLE_DAILY_STUDY_PLAN = os.getenv('ENABLE_DAILY_STUDY_PLAN', 'True').lower() == 'true'
    ENABLE_MOCK_TESTS = os.getenv('ENABLE_MOCK_TESTS', 'True').lower() == 'true'
    ENABLE_NOTIFICATIONS = os.getenv('ENABLE_NOTIFICATIONS', 'False').lower() == 'true'
    
    # Tamil Nadu Districts
    TN_DISTRICTS = [
        'Chennai', 'Coimbatore', 'Madurai', 'Tiruchirappalli', 'Salem',
        'Tirunelveli', 'Erode', 'Vellore', 'Thoothukudi', 'Dindigul',
        'Thanjavur', 'Ranipet', 'Sivaganga', 'Karur', 'Ramanathapuram',
        'Virudhunagar', 'Tiruvannamalai', 'Nagapattinam', 'Namakkal',
        'Cuddalore', 'Kanchipuram', 'Tiruppur', 'Villupuram', 'Pudukkottai',
        'Krishnagiri', 'Ariyalur', 'Perambalur', 'Nilgiris', 'Theni',
        'Kanyakumari', 'Kallakurichi', 'Chengalpattu', 'Tenkasi',
        'Tirupathur', 'Mayiladuthurai'
    ]
    
    # Supported Languages
    LANGUAGES = ['en', 'ta']
    DEFAULT_LANGUAGE = 'en'

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_pathguide.db'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
