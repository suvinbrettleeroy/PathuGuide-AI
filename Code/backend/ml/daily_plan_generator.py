"""
Daily Study Plan Generator
"""
from datetime import datetime, timedelta
import random

class DailyPlanGenerator:
    """Generates daily study tasks"""
    
    def __init__(self):
        self.career_topics = {
            'Software Development': [
                'Python basics', 'JavaScript fundamentals', 'Git version control',
                'HTML/CSS', 'React.js', 'Node.js', 'Database SQL', 'REST APIs',
                'Testing', 'Deployment', 'Code review', 'Documentation'
            ],
            'Data Science': [
                'Python for data science', 'Statistics basics', 'Pandas library',
                'Data visualization', 'Machine learning intro', 'NumPy arrays',
                'Data cleaning', 'EDA techniques', 'Model evaluation', 'SQL queries'
            ],
            'Web Development': [
                'HTML structure', 'CSS styling', 'JavaScript DOM', 'Responsive design',
                'Frontend frameworks', 'Backend basics', 'Database integration',
                'Authentication', 'Deployment', 'Performance optimization'
            ]
        }
        
        self.exam_topics = {
            'General Tamil': [
                'இலக்கணம்', 'பெயர்ச்சொல்', 'வினைச்சொல்', 'பழமொழிகள்',
                'திருக்குறள்', 'இலக்கியம்', 'புரிதல் திறன்'
            ],
            'General English': [
                'Grammar rules', 'Vocabulary', 'Tenses', 'Comprehension',
                'Synonyms/Antonyms', 'Sentence correction', 'Reading comprehension'
            ],
            'General Science': [
                'Physics basics', 'Chemistry concepts', 'Biology fundamentals',
                'Scientific developments', 'Environmental science'
            ],
            'History': [
                'Indian history', 'Tamil Nadu history', 'Ancient civilization',
                'Freedom movement', 'Cultural heritage'
            ],
            'Geography': [
                'World geography', 'Indian geography', 'Tamil Nadu geography',
                'Rivers and mountains', 'Climate and seasons'
            ],
            'Polity': [
                'Indian Constitution', 'Fundamental rights', 'Directive principles',
                'Political system', 'Governance structure'
            ],
            'Economics': [
                'Indian economy', 'Tamil Nadu economy', 'Economic development',
                'Banking and finance', 'Budget and taxation'
            ],
            'Aptitude': [
                'Logical reasoning', 'Numerical ability', 'Problem solving',
                'Data interpretation', 'Verbal reasoning'
            ]
        }
    
    def generate_daily_task_career(self, user_profile, weekly_plan, current_date=None):
        """
        Generate today's task for career path
        
        Args:
            user_profile: User profile data
            weekly_plan: Weekly study plan
            current_date: Current date (default: today)
        
        Returns:
            dict: Today's study task
        """
        if current_date is None:
            current_date = datetime.now()
        
        # Get current week
        start_date = datetime.strptime(user_profile.get('start_date', datetime.now().strftime('%Y-%m-%d')), '%Y-%m-%d')
        weeks_elapsed = ((current_date - start_date).days // 7) + 1
        
        # Get domain for topics
        domain = user_profile.get('selected_domain', 'Software Development')
        
        # Get this week's plan
        if weeks_elapsed <= len(weekly_plan):
            current_week = weekly_plan[weeks_elapsed - 1]
        else:
            current_week = weekly_plan[-1]
        
        # Get study hours
        daily_hours = self._parse_study_hours(user_profile.get('study_hours_per_day', '2-4 hours'))
        
        # Select topic based on domain
        topics = self.career_topics.get(domain, self.career_topics['Software Development'])
        today_topic = random.choice(topics)
        
        # Generate task
        task = {
            'date': current_date.strftime('%A, %d %B %Y'),
            'subject': current_week.get('focus', 'Programming'),
            'topics': [today_topic],
            'duration': {
                'total_hours': daily_hours,
                'morning': f'{int(daily_hours * 0.5)} hours',
                'evening': f'{int(daily_hours * 0.3)} hours',
                'night': f'{int(daily_hours * 0.2)} hours (revision)'
            },
            'goal': f'Complete {today_topic} fundamentals',
            'resources': [
                'Online tutorials',
                'Documentation',
                'Practice exercises'
            ],
            'checklist': [
                {'task': f'Learn {today_topic} basics', 'completed': False},
                {'task': 'Practice 5 exercises', 'completed': False},
                {'task': 'Make short notes', 'completed': False},
                {'task': 'Review yesterday\'s topic', 'completed': False}
            ],
            'yesterday': self._get_yesterday_task(),
            'tomorrow': self._get_tomorrow_task(topics, today_topic),
            'weekly_progress': {
                'current_day': current_date.weekday() + 1,
                'total_days': 7,
                'this_week_focus': current_week.get('focus', 'Programming')
            }
        }
        
        return task
    
    def generate_daily_task_exam(self, user_profile, roadmap, current_date=None):
        """
        Generate today's task for government exam
        
        Args:
            user_profile: User profile data
            roadmap: Monthly roadmap
            current_date: Current date (default: today)
        
        Returns:
            dict: Today's study task
        """
        if current_date is None:
            current_date = datetime.now()
        
        # Get current month
        start_date = datetime.strptime(user_profile.get('start_date', datetime.now().strftime('%Y-%m-%d')), '%Y-%m-%d')
        months_elapsed = ((current_date.year - start_date.year) * 12 + current_date.month - start_date.month) + 1
        
        # Get this month's plan
        if months_elapsed <= len(roadmap):
            current_month = roadmap[months_elapsed - 1]
        else:
            current_month = roadmap[-1]
        
        # Get study hours
        daily_hours = self._parse_study_hours(user_profile.get('study_hours_per_day', '4-6 hours'))
        
        # Select subjects for today
        subjects = current_month.get('subjects', ['General Studies'])
        today_subject = random.choice(subjects)
        
        # Get topics for subject
        topics = self.exam_topics.get(today_subject, ['General knowledge'])
        today_topics = random.sample(topics, min(3, len(topics)))
        
        # Current affairs
        current_affairs = self._get_current_affairs()
        
        # Generate task
        task = {
            'date': current_date.strftime('%A, %d %B %Y'),
            'subject': today_subject,
            'topics': today_topics,
            'duration': {
                'total_hours': daily_hours,
                'morning': f'{int(daily_hours * 0.4)} hours',
                'evening': f'{int(daily_hours * 0.4)} hours',
                'night': f'{int(daily_hours * 0.2)} hours (revision)'
            },
            'goal': f'Complete {today_subject} - {", ".join(today_topics[:2])}',
            'resources': [
                'TNPSC guide books',
                'Reference materials',
                'Previous year questions'
            ],
            'checklist': [
                {'task': f'Study {today_topics[0]}', 'completed': False},
                {'task': f'Practice questions on {today_topics[1] if len(today_topics) > 1 else today_topics[0]}', 'completed': False},
                {'task': 'Make notes and mind maps', 'completed': False},
                {'task': 'Solve 20 practice questions', 'completed': False},
                {'task': 'Read current affairs', 'completed': False}
            ],
            'current_affairs': current_affairs,
            'yesterday': self._get_yesterday_task_exam(),
            'tomorrow': self._get_tomorrow_task_exam(subjects, today_subject),
            'weekly_progress': {
                'current_day': current_date.weekday() + 1,
                'total_days': 7,
                'this_month_focus': current_month.get('phase', 'Preparation')
            },
            'study_tip': self._get_study_tip()
        }
        
        return task
    
    def _parse_study_hours(self, hours_str):
        """Parse study hours"""
        mapping = {
            '1-2 hours': 1.5,
            '2-4 hours': 3,
            '4-6 hours': 5,
            '6-8 hours': 7,
            '8-10 hours': 9,
            'More than 10 hours': 11
        }
        return mapping.get(hours_str, 5)
    
    def _get_yesterday_task(self):
        """Get yesterday's task summary"""
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        return {
            'date': yesterday,
            'subject': 'Programming Basics',
            'completion_status': 'Completed'
        }
    
    def _get_tomorrow_task(self, topics, current_topic):
        """Get tomorrow's preview"""
        remaining_topics = [t for t in topics if t != current_topic]
        next_topic = random.choice(remaining_topics) if remaining_topics else 'Revision'
        
        return {
            'subject': 'Programming',
            'topics': [next_topic]
        }
    
    def _get_yesterday_task_exam(self):
        """Get yesterday's exam task"""
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        return {
            'date': yesterday,
            'subject': 'General Studies',
            'completion_status': 'Completed'
        }
    
    def _get_tomorrow_task_exam(self, subjects, current_subject):
        """Get tomorrow's exam preview"""
        remaining = [s for s in subjects if s != current_subject]
        next_subject = random.choice(remaining) if remaining else 'Revision'
        
        return {
            'subject': next_subject,
            'topics': ['Continuation of syllabus']
        }
    
    def _get_current_affairs(self):
        """Get current affairs headlines"""
        return [
            'Government schemes and policies',
            'Important national/state events',
            'Sports and awards updates',
            'Scientific developments'
        ]
    
    def _get_study_tip(self):
        """Get random study tip"""
        tips = [
            'Take 5-minute breaks every hour to stay fresh',
            'Make mind maps for better retention',
            'Revise previous day\'s topics before starting new ones',
            'Practice questions daily to improve speed',
            'Stay hydrated and maintain good posture while studying'
        ]
        return random.choice(tips)
