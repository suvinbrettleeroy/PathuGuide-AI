"""
PathGuide - Main Application
Career & Government Exam Guidance System
"""
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from datetime import datetime, timedelta
import os
import secrets
import webbrowser
import threading
from career_data import CAREER_HIERARCHY, TN_DISTRICTS, get_cities_for_district
from career_output_generator import build_career_output

# Initialize Flask app
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pathguide.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Global tracking lists
career_searches = []
exam_searches = []

# ==================== SUCCESS CALCULATION FUNCTIONS ====================

def calculate_career_success_rate(data):
    """Calculate success prediction for career path based on user inputs"""
    total_score = 0
    breakdown = {
        'education': 0,
        'commitment': 0,
        'timeline': 0,
        'market': 0
    }
    
    # Factor 1: Educational Background (0-30 points)
    degree = data.get('degree', '')
    department = data.get('department', '')
    domain = data.get('domain', '')
    role = data.get('role', '')
    
    # Tech roles with tech degrees get higher scores
    tech_degrees = ['B.E / B.Tech', 'B.Sc', 'BCA', 'MCA', 'M.E / M.Tech', 'M.Sc']
    tech_domains = ['Data Science', 'Software Development', 'Web Development', 'AI/ML', 'Cloud Computing']
    
    if degree in tech_degrees and domain in tech_domains:
        breakdown['education'] = 28
    elif degree in tech_degrees:
        breakdown['education'] = 24
    elif degree in ['B.Com', 'BBA', 'MBA'] and 'Business' in domain:
        breakdown['education'] = 26
    else:
        breakdown['education'] = 20
    
    # Factor 2: Learning Commitment (0-30 points)
    study_hours = data.get('study_hours', '2-4')
    try:
        if '-' in study_hours:
            avg_hours = sum(map(int, study_hours.split('-'))) / 2
        else:
            avg_hours = int(study_hours.split()[0]) if study_hours else 4
        
        if avg_hours >= 8:
            breakdown['commitment'] = 30
        elif avg_hours >= 6:
            breakdown['commitment'] = 28
        elif avg_hours >= 4:
            breakdown['commitment'] = 24
        elif avg_hours >= 2:
            breakdown['commitment'] = 18
        else:
            breakdown['commitment'] = 12
    except:
        breakdown['commitment'] = 20
    
    # Factor 3: Timeline Realism (0-25 points)
    roadmap_months = data.get('roadmap_months', data.get('roadmap_duration', '6'))
    try:
        months = int(roadmap_months)
        if months >= 12:
            breakdown['timeline'] = 25  # Most realistic
        elif months >= 6:
            breakdown['timeline'] = 23  # Good balance
        elif months >= 3:
            breakdown['timeline'] = 18  # Ambitious but doable
        else:
            breakdown['timeline'] = 12
    except:
        breakdown['timeline'] = 20
    
    # Factor 4: Market Demand (0-15 points) - Fixed based on role popularity
    high_demand_roles = ['Data Analyst', 'Software Engineer', 'Full Stack Developer', 
                         'Data Scientist', 'Cloud Engineer', 'DevOps Engineer']
    if any(hd_role in role for hd_role in high_demand_roles):
        breakdown['market'] = 15
    else:
        breakdown['market'] = 12
    
    total_score = sum(breakdown.values())
    
    return {
        'total': total_score,
        'education': breakdown['education'],
        'commitment': breakdown['commitment'],
        'timeline': breakdown['timeline'],
        'market': breakdown['market']
    }

def calculate_exam_success_rate(data):
    """Calculate success prediction for government exam based on user inputs"""
    total_score = 0
    breakdown = {
        'education': 0,
        'commitment': 0,
        'timeline': 0,
        'competition': 0
    }
    
    # Factor 1: Educational Qualification (0-25 points)
    qualification = data.get('qualification', '')
    exam_type = data.get('exam_type', '')
    
    # Match qualification to exam requirements
    ug_degrees = ['B.E', 'B.Tech', 'B.Sc', 'B.Com', 'B.A', 'BBA', 'BCA']
    pg_degrees = ['M.E', 'M.Tech', 'M.Sc', 'M.Com', 'M.A', 'MBA', 'MCA']
    
    if any(deg in qualification for deg in pg_degrees):
        breakdown['education'] = 25  # PG qualification
    elif any(deg in qualification for deg in ug_degrees):
        breakdown['education'] = 22  # UG qualification
    else:
        breakdown['education'] = 18
    
    # Factor 2: Study Commitment (0-30 points)
    study_hours = data.get('study_hours', '4-6')
    try:
        if '-' in study_hours:
            avg_hours = sum(map(int, study_hours.split('-'))) / 2
        else:
            avg_hours = int(study_hours.split()[0]) if study_hours else 4
        
        if avg_hours >= 10:
            breakdown['commitment'] = 30
        elif avg_hours >= 8:
            breakdown['commitment'] = 28
        elif avg_hours >= 6:
            breakdown['commitment'] = 25
        elif avg_hours >= 4:
            breakdown['commitment'] = 20
        else:
            breakdown['commitment'] = 15
    except:
        breakdown['commitment'] = 22
    
    # Factor 3: Preparation Duration (0-25 points)
    duration = data.get('preparation_duration', '6-12')
    try:
        if '-' in duration:
            avg_months = sum(map(int, duration.split('-'))) / 2
        else:
            avg_months = int(duration.split()[0]) if duration else 6
        
        if avg_months >= 12:
            breakdown['timeline'] = 25
        elif avg_months >= 8:
            breakdown['timeline'] = 23
        elif avg_months >= 6:
            breakdown['timeline'] = 20
        elif avg_months >= 3:
            breakdown['timeline'] = 16
        else:
            breakdown['timeline'] = 12
    except:
        breakdown['timeline'] = 20
    
    # Factor 4: Competition Level (0-20 points) - Based on exam difficulty
    group1_exams = ['Group I', 'Group IA', 'IAS', 'IPS']
    group2_exams = ['Group II', 'Group IIA', 'TNPSC']
    
    if any(g1 in exam_type for g1 in group1_exams):
        breakdown['competition'] = 15  # Highly competitive
    elif any(g2 in exam_type for g2 in group2_exams):
        breakdown['competition'] = 18  # Moderately competitive
    else:
        breakdown['competition'] = 17
    
    total_score = sum(breakdown.values())
    
    return {
        'total': total_score,
        'education': breakdown['education'],
        'commitment': breakdown['commitment'],
        'timeline': breakdown['timeline'],
        'competition': breakdown['competition']
    }

# Language support
LANGUAGES = {
    'en': {
        'title': 'PathGuide - Career & Exam Guidance',
        'career': 'Career Path',
        'exam': 'Government Exams',
        'admin': 'Admin Panel',
        'select_path': 'Select Your Path'
    },
    'ta': {
        'title': 'பாதை வழிகாட்டி - தொழில் & தேர்வு வழிகாட்டுதல்',
        'career': 'தொழில் பாதை',
        'exam': 'அரசு தேர்வுகள்',
        'admin': 'நிர்வாக பலகம்',
        'select_path': 'உங்கள் பாதையை தேர்ந்தெடுக்கவும்'
    }
}

# ==================== DASHBOARD ROUTES ====================

@app.route('/')
def index():
    """Homepage/Dashboard"""
    # Set default language if not set
    if 'language' not in session:
        session['language'] = 'en'
    
    # Mock data for demonstration - replace with actual database queries
    saved_profiles = []  # Get from database
    last_activity = None  # Get from session/database
    
    return render_template('index.html',
                         language=session['language'],
                         current_time=datetime.now().strftime('%B %d, %Y - %I:%M %p'),
                         saved_profiles=saved_profiles,
                         last_activity=last_activity)

@app.route('/set-language', methods=['POST'])
def set_language():
    """Set user language preference"""
    data = request.get_json()
    language = data.get('language', 'en')
    
    if language in ['en', 'ta']:
        session['language'] = language
        return jsonify({'success': True, 'language': language})
    
    return jsonify({'success': False, 'message': 'Invalid language'}), 400

@app.route('/set-location', methods=['POST'])
def set_location():
    """Save user location"""
    data = request.get_json()
    session['location_enabled'] = data.get('enabled', False)
    session['district'] = data.get('district', '')
    session['city'] = data.get('city', '')
    return jsonify({'success': True})

@app.route('/reverse-geocode')
def reverse_geocode():
    """Convert GPS coordinates to district/city (Mock - implement with actual geocoding API)"""
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    
    # Mock geocoding - replace with actual API call (Google Maps, OpenStreetMap, etc.)
    # This is a simplified example - you would call an actual geocoding service
    mock_locations = {
        'default': {'district': 'Chennai', 'city': 'Chennai', 'success': True}
    }
    
    return jsonify(mock_locations['default'])

@app.route('/profile/resume/<profile_id>')
def resume_profile(profile_id):
    """Resume a saved profile"""
    # Load profile data from database and restore to session
    return redirect(url_for('index'))

@app.route('/profile/view/<profile_id>')
def view_profile(profile_id):
    """View profile details"""
    # Get profile details from database
    return jsonify({'success': True, 'profile': {}})

@app.route('/profile/rename/<profile_id>', methods=['POST'])
def rename_profile(profile_id):
    """Rename a profile"""
    data = request.get_json()
    new_name = data.get('name')
    # Update profile name in database
    return jsonify({'success': True})

@app.route('/profile/delete/<profile_id>', methods=['DELETE'])
def delete_profile(profile_id):
    """Delete a profile"""
    # Delete profile from database
    return jsonify({'success': True})

@app.route('/resume-last-activity')
def resume_last_activity():
    """Resume last unfinished activity"""
    # Load last activity data from session/database
    return redirect(url_for('index'))

@app.route('/data-deletion-request', methods=['POST'])
def data_deletion_request():
    """Handle user data deletion request"""
    # Clear all user data from database and session
    session.clear()
    return jsonify({
        'success': True,
        'message': 'All your data has been deleted successfully.' if session.get('language', 'en') == 'en' 
                  else 'உங்கள் அனைத்து தரவும் வெற்றிகரமாக நீக்கப்பட்டது.'
    })

@app.route('/select-path/<path_type>')
def select_path(path_type):
    """Redirect to appropriate path"""
    if path_type == 'career':
        return redirect(url_for('career_input'))
    elif path_type == 'govt_exam':
        return redirect(url_for('exam_input'))
    return redirect(url_for('index'))

# ==================== CAREER PATH ROUTES ====================

@app.route('/career/input')
def career_input():
    """Career path input form"""
    lang = session.get('language', 'en')
    return render_template('career_input.html', language=lang)

@app.route('/career/output', methods=['GET', 'POST'])
def career_output():
    """Generate career path recommendations"""
    lang = session.get('language', 'en')
    
    if request.method == 'POST':
        # Get form data
        data = request.get_json() if request.is_json else request.form
        # Store in session for GET request
        session['career_data'] = dict(data) if data else {}
        
        # Track career search
        career_searches.append({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'degree': data.get('degree', 'N/A'),
            'department': data.get('department', 'N/A'),
            'domain': data.get('domain', 'N/A'),
            'role': data.get('role', 'N/A'),
            'study_hours': data.get('study_hours', 'N/A'),
            'roadmap_duration': data.get('roadmap_duration', 'N/A')
        })
        
        return jsonify({'status': 'success'})
    
    # Get career data from session
    career_data = session.get('career_data', {})

    # Build deterministic output structure for Module 2 career output.
    career_data['current_date'] = datetime.now().strftime('%Y-%m-%d')
    output_data = build_career_output(
        user_data=career_data,
        selection={
            'domain': career_data.get('domain', ''),
            'role': career_data.get('role', ''),
        },
        language=lang,
    )

    # Render career output using structured data.
    return render_template('career_output.html', 
                         language=lang,
                         career_data=career_data,
                         career_output_data=output_data)

# ==================== MODULE 2: CAREER PATH API ENDPOINTS ====================

@app.route('/api/career/departments', methods=['POST'])
def get_departments():
    """Get departments for selected degree"""
    data = request.get_json()
    degree = data.get('degree', '')
    
    if degree in CAREER_HIERARCHY:
        departments = list(CAREER_HIERARCHY[degree].keys())
        return jsonify({'success': True, 'departments': departments})
    
    return jsonify({'success': False, 'departments': []})

@app.route('/api/career/domains', methods=['POST'])
def get_domains():
    """Get domains for selected department"""
    data = request.get_json()
    degree = data.get('degree', '')
    department = data.get('department', '')
    
    if degree in CAREER_HIERARCHY and department in CAREER_HIERARCHY[degree]:
        domains = list(CAREER_HIERARCHY[degree][department].keys())
        return jsonify({'success': True, 'domains': domains})
    
    return jsonify({'success': False, 'domains': []})

@app.route('/api/career/roles', methods=['POST'])
def get_roles():
    """Get roles for selected domain"""
    data = request.get_json()
    degree = data.get('degree', '')
    department = data.get('department', '')
    domain = data.get('domain', '')
    
    if (degree in CAREER_HIERARCHY and 
        department in CAREER_HIERARCHY[degree] and 
        domain in CAREER_HIERARCHY[degree][department]):
        roles = CAREER_HIERARCHY[degree][department][domain]
        return jsonify({'success': True, 'roles': roles})
    
    return jsonify({'success': False, 'roles': []})

@app.route('/api/career/cities', methods=['POST'])
def get_cities():
    """Get cities for selected district"""
    data = request.get_json()
    district = data.get('district', '')
    
    cities = get_cities_for_district(district)
    return jsonify({'success': True, 'cities': cities})

@app.route('/api/career/save-progress', methods=['POST'])
def save_career_progress():
    """Save user's progress on career roadmap"""
    data = request.get_json()
    
    if 'career_progress' not in session:
        session['career_progress'] = {}
    
    session['career_progress'].update({
        'role': data.get('role'),
        'completed_weeks': data.get('completed_weeks', []),
        'completed_tasks': data.get('completed_tasks', []),
        'streak_days': data.get('streak_days', 0),
        'last_activity': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    
    session.modified = True
    return jsonify({'success': True, 'message': 'Progress saved'})

@app.route('/api/career/get-progress', methods=['GET'])
def get_career_progress():
    """Get user's saved career progress"""
    progress = session.get('career_progress', {})
    return jsonify({'success': True, 'progress': progress})

# ==================== GOVERNMENT EXAM ROUTES ====================

@app.route('/exam/input')
def exam_input():
    """Government exam input form"""
    lang = session.get('language', 'en')
    return render_template('exam_input.html', language=lang)

@app.route('/exam/output', methods=['GET', 'POST'])
def exam_output():
    """Generate exam preparation plan"""
    lang = session.get('language', 'en')
    
    if request.method == 'POST':
        # Get form data
        data = request.get_json() if request.is_json else request.form
        # Store in session for GET request
        session['exam_data'] = dict(data) if data else {}
        return jsonify({'status': 'success'})
    
    # Get exam data from session
    exam_data = session.get('exam_data', {})
    
    # Calculate success rate based on inputs
    success_prediction = calculate_exam_success_rate(exam_data)
    
    # Render results page
    return render_template('exam_output.html', 
                         language=lang,
                         exam_data=exam_data,
                         success_prediction=success_prediction)

# ==================== ADMIN ROUTES ====================

# Admin login attempt tracking
login_attempts = {}

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page with security features"""
    if request.method == 'GET':
        # Check if account is locked
        client_ip = request.remote_addr
        if client_ip in login_attempts:
            attempt_data = login_attempts[client_ip]
            if attempt_data['locked_until'] and datetime.now() < attempt_data['locked_until']:
                remaining_time = (attempt_data['locked_until'] - datetime.now()).seconds // 60
                return render_template('admin_login.html', 
                                     locked=True, 
                                     remaining_minutes=remaining_time)
        
        return render_template('admin_login.html', locked=False)
    
    # Handle login
    client_ip = request.remote_addr
    data = request.get_json() if request.is_json else request.form
    username = data.get('username', '')
    password = data.get('password', '')
    
    # Initialize attempt tracking for this IP
    if client_ip not in login_attempts:
        login_attempts[client_ip] = {
            'attempts': 0,
            'locked_until': None,
            'last_attempt': None
        }
    
    attempt_data = login_attempts[client_ip]
    
    # Check if account is locked
    if attempt_data['locked_until'] and datetime.now() < attempt_data['locked_until']:
        remaining_time = (attempt_data['locked_until'] - datetime.now()).seconds // 60
        return jsonify({
            'success': False,
            'locked': True,
            'message': f'Account locked. Try again in {remaining_time} minutes.',
            'remaining_minutes': remaining_time
        }), 403
    
    # Reset lock if time has passed
    if attempt_data['locked_until'] and datetime.now() >= attempt_data['locked_until']:
        attempt_data['attempts'] = 0
        attempt_data['locked_until'] = None
    
    # Validate credentials (case-sensitive)
    # Username: Darkknight, Password: Suv001
    if username == 'Darkknight' and password == 'Suv001':
        # Reset attempts on successful login
        login_attempts[client_ip] = {
            'attempts': 0,
            'locked_until': None,
            'last_attempt': None
        }
        
        session['admin_logged_in'] = True
        session['admin_username'] = username
        session['admin_login_time'] = datetime.now().isoformat()
        session['admin_last_activity'] = datetime.now().isoformat()
        
        return jsonify({
            'success': True,
            'message': 'Login successful!',
            'redirect': url_for('admin_panel')
        })
    else:
        # Increment failed attempts
        attempt_data['attempts'] += 1
        attempt_data['last_attempt'] = datetime.now()
        
        # Lock account after 3 failed attempts
        if attempt_data['attempts'] >= 3:
            attempt_data['locked_until'] = datetime.now() + timedelta(minutes=15)
            return jsonify({
                'success': False,
                'locked': True,
                'message': 'Too many failed attempts! Account locked for 15 minutes.',
                'remaining_minutes': 15
            }), 403
        
        remaining_attempts = 3 - attempt_data['attempts']
        return jsonify({
            'success': False,
            'locked': False,
            'message': f'Invalid credentials! {remaining_attempts} attempt(s) remaining. Username and password are case-sensitive.',
            'remaining_attempts': remaining_attempts
        }), 401

@app.route('/admin')
def admin_panel():
    """Admin panel dashboard with auto-logout"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    # Check session timeout (30 minutes of inactivity)
    last_activity = session.get('admin_last_activity')
    if last_activity:
        last_dt = datetime.fromisoformat(last_activity)
        if datetime.now() - last_dt > timedelta(minutes=30):
            session.pop('admin_logged_in', None)
            session.pop('admin_username', None)
            session.pop('admin_login_time', None)
            session.pop('admin_last_activity', None)
            return redirect(url_for('admin_login'))
    
    # Update last activity time
    session['admin_last_activity'] = datetime.now().isoformat()
    
    # Mock statistics - replace with actual database queries
    stats = {
        'total_users': 1234,
        'active_today': 87,
        'new_this_week': 156,
        'career_users': 678,
        'career_percentage': 55,
        'exam_users': 556,
        'exam_percentage': 45,
        'total_career_roles': 150,
        'total_govt_jobs': 70,
        'coaching_centers': 45,
        'last_backup': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'pending_updates': 3
    }
    
    # Mock configuration - replace with database
    config = {
        'welcome_title_en': 'Welcome to PathGuide',
        'welcome_title_ta': 'PathGuide க்கு வரவேற்கிறோம்',
        'welcome_desc_en': 'Choose your path: Career Guidance or Tamil Nadu Government Exams',
        'welcome_desc_ta': 'உங்கள் பாதையைத் தேர்வு செய்யவும்: தொழில் வழிகாட்டுதல் அல்லது தமிழ்நாடு அரசு தேர்வுகள்'
    }
    
    return render_template('admin_dashboard.html',
                         stats=stats,
                         config=config,
                         session=session)

@app.route('/admin/logout')
def admin_logout():
    """Admin logout"""
    session.pop('admin_logged_in', None)
    session.pop('admin_username', None)
    session.pop('admin_login_time', None)
    session.pop('admin_last_activity', None)
    return redirect(url_for('index'))

# ==================== ADMIN API ROUTES ====================

@app.route('/admin/toggle-feature', methods=['POST'])
def admin_toggle_feature():
    """Toggle dashboard feature on/off"""
    if not session.get('admin_logged_in'):
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    
    data = request.get_json()
    feature = data.get('feature')
    enabled = data.get('enabled')
    
    # TODO: Save to database
    # For now, just return success
    return jsonify({
        'success': True,
        'message': f'Feature {feature} {"enabled" if enabled else "disabled"}'
    })

@app.route('/admin/save-welcome-banner', methods=['POST'])
def admin_save_welcome_banner():
    """Save welcome banner content"""
    if not session.get('admin_logged_in'):
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    
    data = request.get_json()
    # TODO: Save to database
    # config.welcome_title_en = data.get('title_en')
    # config.welcome_title_ta = data.get('title_ta')
    # config.welcome_desc_en = data.get('desc_en')
    # config.welcome_desc_ta = data.get('desc_ta')
    
    return jsonify({
        'success': True,
        'message': 'Welcome banner updated successfully'
    })

@app.route('/admin/export-report')
def admin_export_report():
    """Export analytics report"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    # TODO: Generate actual report
    report_data = {
        'generated_at': datetime.now().isoformat(),
        'total_users': 1234,
        'career_path_users': 678,
        'govt_exam_users': 556,
        'most_popular_career': 'Data Science',
        'most_popular_exam': 'TNPSC Group IV'
    }
    
    return jsonify(report_data)

@app.route('/admin/export-audit-logs')
def admin_export_audit_logs():
    """Export audit logs"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    # TODO: Generate actual audit logs
    logs = [
        {
            'timestamp': datetime.now().isoformat(),
            'admin': session.get('admin_username'),
            'action': 'Updated welcome banner',
            'ip': request.remote_addr
        }
    ]
    
    return jsonify(logs)

@app.route('/admin/trigger-backup', methods=['POST'])
def admin_trigger_backup():
    """Manually trigger database backup"""
    if not session.get('admin_logged_in'):
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    
    # TODO: Implement actual backup logic
    return jsonify({
        'success': True,
        'message': 'Backup completed successfully',
        'timestamp': datetime.now().isoformat()
    })

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': '404 Not Found',
        'message': 'The requested resource was not found.',
        'available_routes': [
            '/',
            '/set-language (POST)',
            '/set-location (POST)',
            '/select-path/career',
            '/select-path/govt_exam',
            '/career/input',
            '/career/output (POST)',
            '/exam/input',
            '/exam/output (POST)',
            '/admin-login',
            '/admin',
            '/admin/logout'
        ]
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': '500 Internal Server Error',
        'message': str(error)
    }), 500

# ==================== MAIN ====================

if __name__ == '__main__':
    print("=" * 70)
    print("   PathGuide - Career & Government Exam Guidance System")
    print("=" * 70)
    print(">> Server starting...")
    print(">> URL: http://127.0.0.1:5000")
    print(">> Admin Login: http://127.0.0.1:5000/admin-login")
    print("")
    print(">> Admin Credentials (case-sensitive):")
    print("   Username: Darkknight")
    print("   Password: Suv001")
    print("")
    print(">> Note: ML features require Python 3.8-3.13")
    print("   Currently running: Python 3.14")
    print("   Basic routing and templates are fully functional!")
    print("=" * 70)
    print("")
    
    # Auto-open browser after a short delay
    def open_browser():
        import time
        time.sleep(1.5)  # Wait for server to start
        webbrowser.open('http://127.0.0.1:5000')
    
    threading.Thread(target=open_browser, daemon=True).start()
    
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
