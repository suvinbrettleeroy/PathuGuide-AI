"""
Success Rate Prediction Model
"""
import numpy as np  # type: ignore[reportMissingImports]
from sklearn.ensemble import RandomForestClassifier  # type: ignore[reportMissingImports,reportMissingModuleSource]
from sklearn.preprocessing import LabelEncoder  # type: ignore[reportMissingImports,reportMissingModuleSource]
import joblib  # type: ignore[reportMissingImports]
import os

class SuccessPredictor:
    """Predicts success rate based on user inputs"""
    
    def __init__(self, model_path='models/success_predictor.pkl'):
        self.model_path = model_path
        self.model = None
        self.encoders = {}
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize or load existing model"""
        if os.path.exists(self.model_path):
            try:
                self.model = joblib.load(self.model_path)
            except:
                self._create_new_model()
        else:
            self._create_new_model()
    
    def _create_new_model(self):
        """Create and train a new model"""
        # Create a random forest classifier
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        
        # Generate synthetic training data
        self._train_with_synthetic_data()
    
    def _train_with_synthetic_data(self):
        """Train with synthetic data"""
        # This would be replaced with real historical data
        np.random.seed(42)
        n_samples = 1000
        
        # Features: study_hours, roadmap_months, alignment_score
        X = np.random.rand(n_samples, 3)
        X[:, 0] = X[:, 0] * 10  # Study hours: 0-10
        X[:, 1] = X[:, 1] * 12 + 3  # Roadmap: 3-15 months
        X[:, 2] = X[:, 2] * 100  # Alignment: 0-100
        
        # Target: Success (1) or Not (0)
        # Higher study hours + longer roadmap + better alignment = higher success
        success_prob = (X[:, 0] / 10 * 0.4 + 
                       X[:, 1] / 15 * 0.3 + 
                       X[:, 2] / 100 * 0.3)
        y = (success_prob > 0.5).astype(int)
        
        # Train model
        self.model.fit(X, y)
        
        # Save model
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, self.model_path)
    
    def predict_success_rate(self, user_profile):
        """
        Predict success rate for a user
        
        Args:
            user_profile (dict): Contains study_hours, roadmap_duration, 
                                department, domain, role
        
        Returns:
            dict: Success rate, rating, and feedback
        """
        # Extract features
        study_hours = self._parse_study_hours(user_profile.get('study_hours_per_day', '2-4 hours'))
        roadmap_months = user_profile.get('roadmap_duration', 6)
        alignment_score = self._calculate_alignment_score(user_profile)
        
        # Prepare features
        features = np.array([[study_hours, roadmap_months, alignment_score]])
        
        # Get prediction probability
        if hasattr(self.model, 'predict_proba'):
            success_prob = self.model.predict_proba(features)[0][1]
        else:
            success_prob = self.model.predict(features)[0]
        
        # Convert to percentage
        success_rate = int(success_prob * 100)
        
        # Determine rating
        if success_rate >= 75:
            rating = 'High'
        elif success_rate >= 50:
            rating = 'Medium'
        else:
            rating = 'Low'
        
        # Generate feedback
        feedback = self._generate_feedback(success_rate, user_profile)
        
        # Improvement suggestions
        suggestions = self._generate_suggestions(success_rate, user_profile)
        
        return {
            'success_rate': success_rate,
            'rating': rating,
            'feedback': feedback,
            'suggestions': suggestions,
            'factors': {
                'study_hours': study_hours,
                'roadmap_duration': roadmap_months,
                'alignment_score': alignment_score
            }
        }
    
    def _parse_study_hours(self, hours_str):
        """Parse study hours string to average number"""
        mapping = {
            '1-2 hours': 1.5,
            '2-4 hours': 3,
            '4-6 hours': 5,
            '6-8 hours': 7,
            '8-10 hours': 9,
            'More than 10 hours': 11
        }
        return mapping.get(hours_str, 3)
    
    def _calculate_alignment_score(self, profile):
        """Calculate how well the role aligns with department"""
        # Simplified scoring - in real implementation, this would use
        # historical data and domain knowledge
        
        department = profile.get('department', '').lower()
        domain = profile.get('selected_domain', '').lower()
        
        # High alignment examples
        high_alignment = {
            'computer science': ['software', 'data science', 'ai', 'machine learning'],
            'electronics': ['embedded', 'vlsi', 'telecommunication'],
            'mechanical': ['cad', 'automobile', 'robotics'],
        }
        
        # Check alignment
        score = 50  # Base score
        
        for dept, domains in high_alignment.items():
            if dept in department:
                for dom in domains:
                    if dom in domain:
                        score = 90
                        break
        
        # Adjust for prerequisites
        if profile.get('year_of_study') in ['First Year', 'Second Year']:
            score -= 10
        
        return max(0, min(100, score))
    
    def _generate_feedback(self, success_rate, profile):
        """Generate personalized feedback"""
        if success_rate >= 75:
            return {
                'en': "Excellent! Your commitment and background are well-aligned with this role. Stay consistent with your study plan and you're likely to succeed.",
                'ta': "சிறப்பு! உங்கள் அர்ப்பணிப்பு மற்றும் பின்னணி இந்த பாத்திரத்துடன் நன்கு ஒத்துள்ளது. உங்கள் கற்றல் திட்டத்துடன் நிலையாக இருங்கள், நீங்கள் வெற்றி பெறுவீர்கள்."
            }
        elif success_rate >= 50:
            return {
                'en': "Good potential! You may need to increase study hours or extend your roadmap duration for better outcomes. Focus on building strong fundamentals.",
                'ta': "நல்ல திறன்! சிறந்த முடிவுகளுக்கு படிப்பு நேரத்தை அதிகரிக்க வேண்டும் அல்லது உங்கள் வழித்தட காலத்தை நீட்டிக்க வேண்டும். வலுவான அடிப்படைகளை உருவாக்குவதில் கவனம் செலுத்துங்கள்."
            }
        else:
            return {
                'en': "This path may require more time or preparation. Consider extending your roadmap to 12 months or increasing daily study hours. Don't be discouraged—many successful professionals started from scratch!",
                'ta': "இந்த பாதைக்கு அதிக நேரம் அல்லது தயாரிப்பு தேவைப்படலாம். உங்கள் வழித்தடத்தை 12 மாதங்களாக நீட்டிக்கவும் அல்லது தினசரி படிப்பு நேரத்தை அதிகரிக்கவும். ஊக்கம் இழக்காதீர்கள்—பல வெற்றிகரமான வல்லுநர்கள் புதிதாக தொடங்கினார்கள்!"
            }
    
    def _generate_suggestions(self, success_rate, profile):
        """Generate improvement suggestions"""
        suggestions = []
        
        study_hours = self._parse_study_hours(profile.get('study_hours_per_day', '2-4 hours'))
        roadmap = profile.get('roadmap_duration', 6)
        
        if study_hours < 4:
            suggestions.append({
                'en': 'Increase daily study hours to at least 4-6 hours for better results',
                'ta': 'சிறந்த முடிவுகளுக்கு தினசரி படிப்பு நேரத்தை குறைந்தது 4-6 மணி நேரமாக அதிகரிக்கவும்'
            })
        
        if roadmap < 6:
            suggestions.append({
                'en': 'Consider extending your roadmap to 6-12 months for comprehensive learning',
                'ta': 'விரிவான கற்றலுக்கு உங்கள் வழித்தடத்தை 6-12 மாதங்களாக நீட்டிக்க பரிந்துரைக்கப்படுகிறது'
            })
        
        if success_rate < 50:
            suggestions.append({
                'en': 'Focus on building strong fundamentals before diving into advanced topics',
                'ta': 'மேம்பட்ட தலைப்புகளுக்கு முன் வலுவான அடிப்படைகளை உருவாக்குவதில் கவனம் செலுத்துங்கள்'
            })
        
        return suggestions
