"""
Analytics Tracker
"""
from datetime import datetime, timedelta
from models import db
from models.admin import AnalyticsData
from models.user import User

class AnalyticsTracker:
    """Tracks system analytics"""
    
    def __init__(self):
        pass
    
    def track_event(self, metric_type, data):
        """Track an analytics event"""
        # Determine category
        if 'career' in metric_type or 'domain' in metric_type or 'role' in metric_type:
            category = 'career'
        elif 'exam' in metric_type or 'job' in metric_type:
            category = 'exam'
        else:
            category = 'system'
        
        # Extract value
        value = data.get('path') or data.get('domain') or data.get('exam') or 'general'
        
        # Check if event exists today
        today = datetime.utcnow().date()
        existing = AnalyticsData.query.filter_by(
            metric_type=metric_type,
            metric_category=category,
            metric_value=value,
            date=today
        ).first()
        
        if existing:
            existing.count += 1
        else:
            event = AnalyticsData(
                metric_type=metric_type,
                metric_category=category,
                metric_value=value,
                count=1,
                date=today
            )
            db.session.add(event)
        
        db.session.commit()
    
    def get_dashboard_stats(self):
        """Get dashboard statistics"""
        today = datetime.utcnow().date()
        week_ago = today - timedelta(days=7)
        
        stats = {
            'total_users': User.query.count(),
            'active_today': User.query.filter(
                User.last_activity >= datetime.combine(today, datetime.min.time())
            ).count(),
            'new_this_week': User.query.filter(
                User.created_at >= datetime.combine(week_ago, datetime.min.time())
            ).count(),
            'career_users': User.query.filter_by(selected_path='career').count(),
            'exam_users': User.query.filter_by(selected_path='govt_exam').count(),
            'top_domains': self._get_top_metrics('career', 'domain', 10),
            'top_exams': self._get_top_metrics('exam', 'exam', 10),
            'language_distribution': self._get_language_stats()
        }
        
        return stats
    
    def _get_top_metrics(self, category, metric_type, limit=10):
        """Get top metrics by category"""
        results = db.session.query(
            AnalyticsData.metric_value,
            db.func.sum(AnalyticsData.count).label('total')
        ).filter(
            AnalyticsData.metric_category == category
        ).group_by(
            AnalyticsData.metric_value
        ).order_by(
            db.desc('total')
        ).limit(limit).all()
        
        return [{'name': r[0], 'count': r[1]} for r in results]
    
    def _get_language_stats(self):
        """Get language usage statistics"""
        total = User.query.count()
        if total == 0:
            return {'en': 0, 'ta': 0}
        
        en_count = User.query.filter_by(language='en').count()
        ta_count = User.query.filter_by(language='ta').count()
        
        return {
            'en': {'count': en_count, 'percentage': round(en_count / total * 100, 1)},
            'ta': {'count': ta_count, 'percentage': round(ta_count / total * 100, 1)}
        }
