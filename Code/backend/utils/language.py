"""
Language Management
"""

class LanguageManager:
    """Manages bilingual content"""
    
    def __init__(self):
        self.translations = {
            # Dashboard
            'welcome_title': {
                'en': 'Welcome to PathGuide',
                'ta': 'பாத்கைடுக்கு வரவேற்கிறோம்'
            },
            'welcome_desc': {
                'en': 'Choose your path: Career Guidance or Tamil Nadu Government Exams',
                'ta': 'உங்கள் பாதையைத் தேர்ந்தெடுக்கவும்: தொழில் வழிகாட்டுதல் அல்லது தமிழ்நாடு அரசு தேர்வுகள்'
            },
            'career_path': {
                'en': 'College Career Path',
                'ta': 'கல்லூரி தொழில் பாதை'
            },
            'govt_exams': {
                'en': 'Tamil Nadu Government Exams',
                'ta': 'தமிழ்நாடு அரசு தேர்வுகள்'
            },
            'language': {
                'en': 'Language',
                'ta': 'மொழி'
            },
            'english': {
                'en': 'English',
                'ta': 'ஆங்கிலம்'
            },
            'tamil': {
                'en': 'Tamil',
                'ta': 'தமிழ்'
            },
            'location': {
                'en': 'Location',
                'ta': 'இடம்'
            },
            'privacy_notice': {
                'en': 'Your personal data and location are optional and used only for guidance. You can delete your data at any time.',
                'ta': 'உங்கள் தனிப்பட்ட தரவு மற்றும் இடம் விருப்பமானது மற்றும் வழிகாட்டுதலுக்கு மட்டுமே பயன்படுத்தப்படுகிறது. எந்த நேரத்திலும் உங்கள் தரவை நீக்கலாம்.'
            },
            
            # Common buttons
            'submit': {
                'en': 'Submit',
                'ta': 'சமர்ப்பி'
            },
            'next': {
                'en': 'Next',
                'ta': 'அடுத்து'
            },
            'back': {
                'en': 'Back',
                'ta': 'பின்செல்'
            },
            'save': {
                'en': 'Save',
                'ta': 'சேமி'
            },
            'cancel': {
                'en': 'Cancel',
                'ta': 'ரத்து செய்'
            },
            
            # Form labels
            'name': {
                'en': 'Name',
                'ta': 'பெயர்'
            },
            'degree': {
                'en': 'Degree',
                'ta': 'பட்டம்'
            },
            'department': {
                'en': 'Department',
                'ta': 'துறை'
            },
            'college': {
                'en': 'College',
                'ta': 'கல்லூரி'
            },
            'district': {
                'en': 'District',
                'ta': 'மாவட்டம்'
            },
            'city': {
                'en': 'City',
                'ta': 'நகரம்'
            }
        }
    
    def get(self, key, lang='en', default=''):
        """Get translation for key"""
        return self.translations.get(key, {}).get(lang, default)
    
    def get_all(self, lang='en'):
        """Get all translations for a language"""
        return {key: value.get(lang, '') for key, value in self.translations.items()}
