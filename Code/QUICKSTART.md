# PathGuide - Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### Step 1: Setup Environment

Open PowerShell in the project directory:

```powershell
cd "C:\Users\ASUS\Desktop\Projects\PathGuide\Code"
```

### Step 2: Create Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 4: Initialize Database

```powershell
python init_db.py
```

Expected output:
```
Creating database tables...
✓ Created 5 degrees
✓ Created 4 departments
✓ Created 3 domains
✓ Created 2 roles
✓ Created 4 exams
✓ Created 3 jobs
✓ Created fitness standards

✅ Database initialized successfully!
```

### Step 5: Run the Application

```powershell
python app.py
```

Expected output:
```
✅ Database initialized!
✅ PathGuide is ready!
🌐 Access the application at: http://127.0.0.1:5000
🔐 Admin login: http://127.0.0.1:5000/admin-login
   Username: Darkknignt
   Password: Suv001
```

### Step 6: Access the Application

**Student Interface:**
1. Open browser: http://127.0.0.1:5000
2. Select language (English/Tamil)
3. Choose path (Career/Govt Exam)
4. Fill the form and get guidance!

**Admin Panel:**
1. Open: http://127.0.0.1:5000/admin-login
2. Username: `Darkknignt` (case-sensitive!)
3. Password: `Suv001` (case-sensitive!)
4. Access full control panel

## 📋 Testing Checklist

### Module 1 - Dashboard
- [ ] Page loads successfully
- [ ] Language toggle works (English ↔ Tamil)
- [ ] Location toggle shows/hides fields
- [ ] Career path button redirects to /career/input
- [ ] Govt exam button redirects to /exam/input

### Module 2 - Career Path
- [ ] Input form displays correctly
- [ ] Dropdowns are populated
- [ ] Form submission works
- [ ] Output page shows recommendations
- [ ] Daily study plan displays
- [ ] Success rate prediction shows

### Module 3 - Government Exams
- [ ] Exam dropdown populated
- [ ] Job dropdown updates based on exam
- [ ] Fitness module appears for police jobs
- [ ] Output shows syllabus
- [ ] Daily study plan generated
- [ ] Coaching centers displayed

### Module 4 - Admin Panel
- [ ] Admin login page accessible
- [ ] Failed login shows error
- [ ] Successful login redirects to dashboard
- [ ] Dashboard shows analytics
- [ ] Logout works

## 🔧 Troubleshooting

### Database Issues

**Problem:** `OperationalError: no such table`
**Solution:**
```powershell
python init_db.py
```

### Port Already in Use

**Problem:** `Address already in use`
**Solution:** Change port in app.py:
```python
app.run(debug=True, port=5001)
```

### Module Not Found

**Problem:** `ModuleNotFoundError: No module named 'flask'`
**Solution:**
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Admin Login Not Working

**Problem:** Invalid credentials error
**Solution:** Ensure exact case-sensitive credentials:
- Username: `Darkknignt` (capital D, lowercase k)
- Password: `Suv001` (capital S, lowercase uv, zero-zero-one)

## 📊 Next Steps

### 1. Populate More Data

Edit `init_db.py` and add more:
- Degrees and departments
- Domains and roles
- Exams and jobs
- Courses and projects

### 2. Customize ML Models

Modify `ml/success_predictor.py` to:
- Use real training data
- Adjust prediction algorithm
- Fine-tune parameters

### 3. Add More Templates

Create HTML templates for:
- Career output (detailed)
- Exam output (detailed)
- Admin panels (content management)

### 4. Implement Additional Features

- Email notifications
- PDF download
- Social sharing
- User authentication
- Progress tracking

## 🎓 Project Submission

### Required Deliverables

1. **Source Code** ✅
   - Location: `C:\Users\ASUS\Desktop\Projects\PathGuide\Code`

2. **Documentation** 📄
   - README.md ✅
   - Quick Start Guide ✅
   - User Manual (create)
   - Admin Manual (create)

3. **Presentation** 🎤
   - Create PPT with screenshots
   - Demo video (optional)

4. **Report** 📊
   - Abstract
   - Introduction
   - Literature Review
   - Methodology
   - Implementation
   - Results
   - Conclusion

### Demo Preparation

**Live Demo Checklist:**
1. Start application before presentation
2. Prepare sample inputs
3. Show both English and Tamil
4. Demonstrate career and exam paths
5. Login to admin panel
6. Show ML predictions
7. Explain architecture

## 🆘 Support

For issues or questions:
1. Check this guide
2. Review README.md
3. Check code comments
4. Debug using Flask debug mode

## 🎉 Success!

If you see the PathGuide homepage with language toggle and path selection, you're all set!

**Happy Coding! 🚀**
