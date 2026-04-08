"""
Recommendation Engine
"""
from datetime import datetime

class RecommendationEngine:
    """Generates personalized recommendations"""
    
    def __init__(self):
        pass
    
    def generate_weekly_study_plan(self, user_profile, roadmap_data):
        """
        Generate weekly study plan
        
        Args:
            user_profile: User profile data
            roadmap_data: Role-specific roadmap
        
        Returns:
            dict: Week-by-week study plan
        """
        duration_months = user_profile.get('roadmap_duration', 6)
        total_weeks = duration_months * 4
        
        # Get study hours
        daily_hours = self._parse_study_hours(user_profile.get('study_hours_per_day', '2-4 hours'))
        weekly_hours = daily_hours * 7
        
        # Generate plan
        weekly_plan = []
        
        # Phase 1: Foundation (First 25% of time)
        foundation_weeks = total_weeks // 4
        for week in range(1, foundation_weeks + 1):
            weekly_plan.append({
                'week': week,
                'phase': 'Foundation Building',
                'focus': 'Core concepts and fundamentals',
                'topics': self._get_foundation_topics(roadmap_data),
                'study_goal': f'Complete basic concepts, dedicate {weekly_hours} hours',
                'tasks': [
                    {'day': '1-2', 'activity': 'Learn core concepts through videos/reading'},
                    {'day': '3-4', 'activity': 'Practice basic exercises and examples'},
                    {'day': '5-7', 'activity': 'Review and self-assessment'}
                ],
                'checkpoint': 'Basic concept quiz'
            })
        
        # Phase 2: Intermediate (Next 35% of time)
        intermediate_weeks = int(total_weeks * 0.35)
        for week in range(foundation_weeks + 1, foundation_weeks + intermediate_weeks + 1):
            weekly_plan.append({
                'week': week,
                'phase': 'Intermediate Skills',
                'focus': 'Advanced concepts and hands-on practice',
                'topics': self._get_intermediate_topics(roadmap_data),
                'study_goal': f'Deep dive into topics, {weekly_hours} hours',
                'tasks': [
                    {'day': '1-3', 'activity': 'Advanced topic study'},
                    {'day': '4-5', 'activity': 'Mini-project work'},
                    {'day': '6-7', 'activity': 'Code practice and debugging'}
                ],
                'checkpoint': 'Mini-project completion'
            })
        
        # Phase 3: Specialization (Next 25% of time)
        specialization_weeks = total_weeks // 4
        for week in range(foundation_weeks + intermediate_weeks + 1, 
                         foundation_weeks + intermediate_weeks + specialization_weeks + 1):
            weekly_plan.append({
                'week': week,
                'phase': 'Specialization & Projects',
                'focus': 'Role-specific skills and major project',
                'topics': self._get_specialization_topics(roadmap_data),
                'study_goal': f'Build portfolio project, {weekly_hours} hours',
                'tasks': [
                    {'day': '1-2', 'activity': 'Project planning and setup'},
                    {'day': '3-5', 'activity': 'Implementation and development'},
                    {'day': '6-7', 'activity': 'Testing and documentation'}
                ],
                'checkpoint': 'Major project milestone'
            })
        
        # Phase 4: Revision & Interview Prep (Final 15% of time)
        revision_weeks = total_weeks - (foundation_weeks + intermediate_weeks + specialization_weeks)
        for week in range(foundation_weeks + intermediate_weeks + specialization_weeks + 1, total_weeks + 1):
            weekly_plan.append({
                'week': week,
                'phase': 'Revision & Interview Preparation',
                'focus': 'Portfolio completion and interview skills',
                'topics': ['Resume building', 'Interview preparation', 'Mock interviews'],
                'study_goal': f'Interview ready, {weekly_hours} hours',
                'tasks': [
                    {'day': '1-2', 'activity': 'Revision of key concepts'},
                    {'day': '3-4', 'activity': 'Practice interview questions'},
                    {'day': '5-7', 'activity': 'Portfolio refinement and presentation'}
                ],
                'checkpoint': 'Mock interview assessment'
            })
        
        return weekly_plan
    
    def generate_exam_study_roadmap(self, user_profile, exam_data, syllabus_data):
        """
        Generate government exam study roadmap
        
        Args:
            user_profile: User profile
            exam_data: Exam information
            syllabus_data: Complete syllabus
        
        Returns:
            dict: Month-by-month study roadmap
        """
        duration_months = user_profile.get('roadmap_duration', 12)
        
        roadmap = []
        
        # Calculate months per phase
        foundation_months = max(2, duration_months // 3)
        core_months = max(2, duration_months // 3)
        revision_months = duration_months - foundation_months - core_months
        
        # Phase 1: Foundation
        for month in range(1, foundation_months + 1):
            roadmap.append({
                'month': month,
                'phase': 'Foundation Building',
                'subjects': ['General Tamil', 'General English', 'Basic Science'],
                'goal': 'Complete basics, build reading habit',
                'strategy': {
                    'morning': 'Language subjects (2 hours)',
                    'evening': 'Science (2 hours)',
                    'night': 'Current affairs (30 mins)'
                },
                'resources': ['NCERT textbooks', 'Language workbooks', 'Newspapers']
            })
        
        # Phase 2: Core Subjects
        for month in range(foundation_months + 1, foundation_months + core_months + 1):
            roadmap.append({
                'month': month,
                'phase': 'Core Subjects',
                'subjects': ['History', 'Geography', 'Polity', 'Economics'],
                'goal': 'Complete syllabus, make notes',
                'strategy': {
                    'morning': 'In-depth reading (3 hours)',
                    'evening': 'Note-making and mind maps (2 hours)',
                    'night': 'Daily revision (1 hour)'
                },
                'resources': ['Reference books', 'Online materials', 'TNPSC guides']
            })
        
        # Phase 3: Aptitude & Revision
        for month in range(foundation_months + core_months + 1, duration_months + 1):
            roadmap.append({
                'month': month,
                'phase': 'Aptitude & Final Revision',
                'subjects': ['Aptitude', 'Mental Ability', 'Full Revision'],
                'goal': 'Speed, accuracy, and exam readiness',
                'strategy': {
                    'morning': 'Mock tests (3 hours)',
                    'evening': 'Analysis and improvement (2 hours)',
                    'night': 'Quick revision notes (1 hour)'
                },
                'resources': ['Previous year papers', 'Mock test series', 'Quick revision notes']
            })
        
        return roadmap
    
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
        return mapping.get(hours_str, 3)
    
    def _get_foundation_topics(self, roadmap_data):
        """Get foundation topics"""
        return [
            'Programming basics',
            'Data structures fundamentals',
            'Problem-solving techniques',
            'Development tools setup'
        ]
    
    def _get_intermediate_topics(self, roadmap_data):
        """Get intermediate topics"""
        return [
            'Advanced algorithms',
            'Framework introduction',
            'Database management',
            'API development'
        ]
    
    def _get_specialization_topics(self, roadmap_data):
        """Get specialization topics"""
        return [
            'Role-specific frameworks',
            'Industry best practices',
            'System design',
            'Portfolio projects'
        ]
