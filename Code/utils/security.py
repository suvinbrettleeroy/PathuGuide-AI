"""
Security Manager
"""
from datetime import datetime, timedelta
from models import db
from models.admin import AdminLog

class SecurityManager:
    """Manages security features"""
    
    def __init__(self):
        self.failed_attempts = {}  # IP -> (count, timestamp)
        self.lockout_duration = 1800  # 30 minutes in seconds
        self.max_attempts = 3
    
    def check_login_attempts(self, ip_address):
        """Check if IP is allowed to login"""
        if ip_address in self.failed_attempts:
            count, timestamp = self.failed_attempts[ip_address]
            
            # Check if lockout period has passed
            if (datetime.now() - timestamp).seconds < self.lockout_duration:
                if count >= self.max_attempts:
                    return False
            else:
                # Reset after lockout period
                del self.failed_attempts[ip_address]
        
        return True
    
    def record_failed_login(self, ip_address):
        """Record a failed login attempt"""
        if ip_address in self.failed_attempts:
            count, _ = self.failed_attempts[ip_address]
            self.failed_attempts[ip_address] = (count + 1, datetime.now())
        else:
            self.failed_attempts[ip_address] = (1, datetime.now())
    
    def get_failed_attempts(self, ip_address):
        """Get number of failed attempts"""
        if ip_address in self.failed_attempts:
            return self.failed_attempts[ip_address][0]
        return 0
    
    def clear_failed_attempts(self, ip_address):
        """Clear failed attempts for IP"""
        if ip_address in self.failed_attempts:
            del self.failed_attempts[ip_address]
    
    def log_admin_action(self, action, username, ip_address, details=None):
        """Log admin activity"""
        log = AdminLog(
            admin_username=username,
            action=action,
            ip_address=ip_address,
            old_value=details.get('old_value') if details else None,
            new_value=details.get('new_value') if details else None
        )
        db.session.add(log)
        db.session.commit()
    
    def check_admin_session(self, session):
        """Check if admin session is valid"""
        if not session.get('admin_logged_in'):
            return False
        
        login_time_str = session.get('admin_login_time')
        if not login_time_str:
            return False
        
        login_time = datetime.fromisoformat(login_time_str)
        
        # Check session timeout (60 minutes)
        if (datetime.utcnow() - login_time).seconds > 3600:
            return False
        
        return True
