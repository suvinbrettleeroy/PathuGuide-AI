"""
Fitness Eligibility Checker
"""

class FitnessChecker:
    """Checks physical fitness eligibility for government jobs"""
    
    def __init__(self):
        pass
    
    def check_fitness_eligibility(self, user_data, fitness_standards):
        """
        Check if user meets fitness requirements
        
        Args:
            user_data: User's physical data (gender, age, height, weight, running)
            fitness_standards: Job's fitness standards
        
        Returns:
            dict: Eligibility status, comparison, and improvement plan
        """
        gender = user_data.get('gender', 'Male')
        age = user_data.get('age', 25)
        height = user_data.get('height', 170)  # cm
        weight = user_data.get('weight', 65)  # kg
        running_ability = user_data.get('running_ability', 'I don\'t know my running ability')
        
        # Calculate BMI
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        
        # Get standards for gender
        standard = next((s for s in fitness_standards if s['gender'] == gender), None)
        
        if not standard:
            return {'error': 'No fitness standards found for this gender'}
        
        # Check each criterion
        checks = {
            'height': self._check_height(height, standard),
            'weight': self._check_weight(weight, height, standard),
            'bmi': self._check_bmi(bmi, standard),
            'running': self._check_running(running_ability, standard),
            'age': self._check_age(age, standard)
        }
        
        # Overall eligibility
        all_passed = all(check['passed'] for check in checks.values())
        
        # Generate result
        result = {
            'eligible': all_passed,
            'status': 'Eligible' if all_passed else 'Not Eligible',
            'bmi_calculated': round(bmi, 2),
            'checks': checks,
            'comparison': self._generate_comparison(user_data, bmi, standard),
            'improvement_plan': None if all_passed else self._generate_improvement_plan(checks, user_data, standard)
        }
        
        return result
    
    def _check_height(self, height, standard):
        """Check height requirement"""
        height_min = standard.get('height_min', 0)
        height_max = standard.get('height_max', 300)
        
        passed = height_min <= height <= height_max
        
        return {
            'passed': passed,
            'your_value': f'{height} cm',
            'required': f'{height_min} - {height_max} cm',
            'status': '✅' if passed else '❌'
        }
    
    def _check_weight(self, weight, height, standard):
        """Check weight requirement"""
        weight_min = standard.get('weight_min', 0)
        weight_max = standard.get('weight_max', 200)
        
        passed = weight_min <= weight <= weight_max
        
        return {
            'passed': passed,
            'your_value': f'{weight} kg',
            'required': f'{weight_min} - {weight_max} kg',
            'status': '✅' if passed else '❌'
        }
    
    def _check_bmi(self, bmi, standard):
        """Check BMI requirement"""
        bmi_min = standard.get('bmi_min', 18.5)
        bmi_max = standard.get('bmi_max', 25.0)
        
        passed = bmi_min <= bmi <= bmi_max
        
        return {
            'passed': passed,
            'your_value': f'{round(bmi, 2)}',
            'required': f'{bmi_min} - {bmi_max}',
            'status': '✅' if passed else '❌'
        }
    
    def _check_running(self, ability, standard):
        """Check running requirement"""
        required_distance = standard.get('running_distance_km', 5)
        required_time = standard.get('running_time_minutes', 30)
        
        # Parse user's ability
        ability_map = {
            'I can run 5 km in under 30 minutes': 'Excellent',
            'I can run 5 km in 30-40 minutes': 'Good',
            'I can run 5 km in 40-50 minutes': 'Average',
            'I cannot run 5 km continuously': 'Needs Improvement',
            'I don\'t know my running ability': 'Unknown'
        }
        
        ability_level = ability_map.get(ability, 'Unknown')
        
        passed = ability_level in ['Excellent', 'Good']
        
        return {
            'passed': passed,
            'your_value': ability_level,
            'required': f'{required_distance} km in {required_time} minutes',
            'status': '✅' if passed else '❌'
        }
    
    def _check_age(self, age, standard):
        """Check age requirement"""
        # Most jobs don't have strict age for fitness, but general eligibility
        passed = 18 <= age <= 35
        
        return {
            'passed': passed,
            'your_value': f'{age} years',
            'required': '18 - 35 years',
            'status': '✅' if passed else '❌'
        }
    
    def _generate_comparison(self, user_data, bmi, standard):
        """Generate comparison table"""
        return {
            'height': {
                'yours': f"{user_data.get('height')} cm",
                'required': f"{standard.get('height_min')} - {standard.get('height_max', 'N/A')} cm"
            },
            'weight': {
                'yours': f"{user_data.get('weight')} kg",
                'required': f"{standard.get('weight_min')} - {standard.get('weight_max', 'N/A')} kg"
            },
            'bmi': {
                'yours': f"{round(bmi, 2)}",
                'required': f"{standard.get('bmi_min')} - {standard.get('bmi_max')}"
            },
            'running': {
                'yours': user_data.get('running_ability'),
                'required': f"{standard.get('running_distance_km')} km in {standard.get('running_time_minutes')} min"
            }
        }
    
    def _generate_improvement_plan(self, checks, user_data, standard):
        """Generate improvement plan"""
        plan = {
            'current_status': {},
            'areas_to_improve': [],
            'weekly_plan': {},
            'diet_plan': {},
            'exercise_routine': {},
            'timeline': ''
        }
        
        # Identify areas needing improvement
        for criterion, check in checks.items():
            if not check['passed']:
                plan['areas_to_improve'].append(criterion)
                plan['current_status'][criterion] = check
        
        # Generate plans based on what needs improvement
        if 'weight' in plan['areas_to_improve'] or 'bmi' in plan['areas_to_improve']:
            plan['diet_plan'] = self._get_diet_plan(user_data)
        
        if 'running' in plan['areas_to_improve']:
            plan['exercise_routine'] = self._get_running_plan()
        
        # Weekly plan
        plan['weekly_plan'] = self._get_weekly_fitness_plan(plan['areas_to_improve'])
        
        # Estimate timeline
        plan['timeline'] = '3-6 months with consistent effort'
        
        return plan
    
    def _get_diet_plan(self, user_data):
        """Get diet recommendations"""
        return {
            'en': {
                'breakfast': 'Oats with fruits, boiled eggs, milk',
                'lunch': 'Brown rice, dal, vegetables, salad',
                'dinner': 'Roti, grilled chicken/fish, vegetables',
                'avoid': 'Junk food, sugary drinks, fried items, excessive oil'
            },
            'ta': {
                'breakfast': 'பழங்கள் உடன் ஓட்ஸ், வேகவைத்த முட்டை, பால்',
                'lunch': 'பழுப்பு அரிசி, பருப்பு, காய்கறிகள், சாலட்',
                'dinner': 'ரொட்டி, கிரில் செய்த கோழி/மீன், காய்கறிகள்',
                'avoid': 'துரித உணவு, சர்க்கரை பானங்கள், பொரித்த பொருட்கள், அதிக எண்ணெய்'
            }
        }
    
    def _get_running_plan(self):
        """Get running improvement plan"""
        return {
            'en': {
                'week_1_4': 'Start with 15 minutes daily jogging, gradually increase',
                'week_5_8': '30 minutes running, 5 times per week',
                'week_9_12': 'Achieve required standard: 5 km in target time'
            },
            'ta': {
                'week_1_4': 'தினமும் 15 நிமிட ஜாகிங்குடன் தொடங்கவும், படிப்படியாக அதிகரிக்கவும்',
                'week_5_8': 'வாரத்தில் 5 முறை 30 நிமிட ஓட்டம்',
                'week_9_12': 'தேவையான தரத்தை அடையவும்: 5 கி.மீ இலக்கு நேரத்தில்'
            }
        }
    
    def _get_weekly_fitness_plan(self, areas):
        """Get weekly fitness routine"""
        return {
            'monday': 'Running practice + Basic exercises',
            'tuesday': 'Strength training + Flexibility',
            'wednesday': 'Running practice + Core workout',
            'thursday': 'Rest or light yoga',
            'friday': 'Running practice + Upper body',
            'saturday': 'Full fitness test simulation',
            'sunday': 'Rest and recovery'
        }
