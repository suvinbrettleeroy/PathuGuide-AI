"""
PathGuide - Career Hierarchy Data
Complete mapping of Degree → Department → Domain → Role
"""

# Comprehensive hierarchical career data structure
CAREER_HIERARCHY = {
    "B.E / B.Tech": {
        "Computer Science & Engineering (CSE)": {
            "Software Development": [
                "Frontend Developer",
                "Backend Developer",
                "Full Stack Developer",
                "Software Engineer",
                "DevOps Engineer",
                "Mobile App Developer (Android)",
                "Mobile App Developer (iOS)",
                "Desktop Application Developer",
                "Software Architect",
                "Python Developer",
                "Java Developer",
                ".NET Developer"
            ],
            "Data Science & Analytics": [
                "Data Analyst",
                "Data Scientist",
                "Business Intelligence Analyst",
                "Data Engineer",
                "Big Data Engineer",
                "Analytics Manager",
                "Quantitative Analyst",
                "Market Research Analyst",
                "Business Analyst"
            ],
            "Artificial Intelligence & Machine Learning": [
                "Machine Learning Engineer",
                "AI Research Scientist",
                "Deep Learning Engineer",
                "Computer Vision Engineer",
                "Natural Language Processing Engineer",
                "AI/ML Consultant",
                "Robotics Engineer",
                "AI Engineer"
            ],
            "Cybersecurity": [
                "Security Analyst",
                "Ethical Hacker / Penetration Tester",
                "Security Engineer",
                "Security Architect",
                "SOC Analyst",
                "Cybersecurity Consultant",
                "Information Security Manager"
            ],
            "Cloud Computing": [
                "Cloud Engineer",
                "Cloud Architect",
                "AWS Solutions Architect",
                "Azure Cloud Engineer",
                "Google Cloud Engineer",
                "Cloud DevOps Engineer",
                "Site Reliability Engineer (SRE)"
            ],
            "Web Development": [
                "Frontend Web Developer",
                "Backend Web Developer",
                "Full Stack Web Developer",
                "WordPress Developer",
                "E-commerce Developer",
                "Web Designer"
            ],
            "Mobile App Development": [
                "Android Developer",
                "iOS Developer",
                "React Native Developer",
                "Flutter Developer",
                "Mobile App Designer"
            ],
            "Database Administration": [
                "Database Administrator (DBA)",
                "Database Developer",
                "SQL Developer",
                "NoSQL Specialist",
                "Data Warehouse Engineer"
            ],
            "UI/UX Design": [
                "UI Designer",
                "UX Designer",
                "UI/UX Designer",
                "Product Designer",
                "Interaction Designer",
                "UX Researcher"
            ],
            "Quality Assurance & Testing": [
                "QA Engineer",
                "Manual Tester",
                "Automation Test Engineer",
                "Performance Test Engineer",
                "Security Tester",
                "Test Lead"
            ],
            "Game Development": [
                "Game Developer",
                "Unity Developer",
                "Unreal Engine Developer",
                "Game Designer",
                "Graphics Programmer"
            ],
            "Blockchain Development": [
                "Blockchain Developer",
                "Smart Contract Developer",
                "Cryptocurrency Developer",
                "Blockchain Architect"
            ],
            "IoT Development": [
                "IoT Developer",
                "IoT Solutions Architect",
                "Embedded IoT Engineer"
            ]
        },
        "Electronics & Communication Engineering (ECE)": {
            "Embedded Systems": [
                "Embedded Software Engineer",
                "Embedded Systems Developer",
                "Firmware Engineer",
                "Embedded Hardware Engineer",
                "Automotive Embedded Engineer"
            ],
            "VLSI Design": [
                "VLSI Design Engineer",
                "Physical Design Engineer",
                "Verification Engineer",
                "ASIC Design Engineer",
                "FPGA Developer"
            ],
            "Telecommunications": [
                "Telecommunications Engineer",
                "Network Engineer",
                "RF Engineer",
                "Wireless Communications Engineer"
            ],
            "Signal Processing": [
                "Signal Processing Engineer",
                "DSP Engineer",
                "Image Processing Engineer"
            ],
            "Electronics Design": [
                "Electronics Design Engineer",
                "PCB Design Engineer",
                "Hardware Engineer"
            ],
            "Automation & Robotics": [
                "Automation Engineer",
                "Robotics Engineer",
                "Control Systems Engineer"
            ],
            "IoT & Embedded Systems": [
                "IoT Engineer",
                "Embedded IoT Developer",
                "IoT Solutions Engineer"
            ]
        },
        "Mechanical Engineering": {
            "CAD/CAM": [
                "CAD Engineer",
                "CAM Programmer",
                "Design Engineer",
                "3D Modeling Specialist",
                "Product Design Engineer"
            ],
            "Production Engineering": [
                "Production Engineer",
                "Manufacturing Engineer",
                "Process Engineer",
                "Quality Engineer"
            ],
            "Automobile Engineering": [
                "Automobile Design Engineer",
                "Automotive Engineer",
                "Vehicle Dynamics Engineer",
                "Automotive Testing Engineer",
                "EV (Electric Vehicle) Engineer"
            ],
            "Robotics & Automation": [
                "Robotics Engineer",
                "Industrial Automation Engineer",
                "Mechatronics Engineer"
            ],
            "Thermal Engineering": [
                "Thermal Engineer",
                "HVAC Engineer",
                "Energy Engineer"
            ],
            "Maintenance Engineering": [
                "Maintenance Engineer",
                "Reliability Engineer",
                "Asset Management Engineer"
            ]
        },
        "Civil Engineering": {
            "Structural Engineering": [
                "Structural Engineer",
                "Structural Design Engineer",
                "Bridge Engineer",
                "Earthquake Engineer"
            ],
            "Construction Management": [
                "Construction Manager",
                "Site Engineer",
                "Project Manager",
                "Construction Supervisor"
            ],
            "Transportation Engineering": [
                "Transportation Engineer",
                "Highway Engineer",
                "Traffic Engineer"
            ],
            "Water Resources Engineering": [
                "Water Resources Engineer",
                "Hydraulic Engineer",
                "Irrigation Engineer"
            ],
            "Environmental Engineering": [
                "Environmental Engineer",
                "Waste Management Engineer",
                "Pollution Control Engineer"
            ],
            "Geotechnical Engineering": [
                "Geotechnical Engineer",
                "Foundation Engineer",
                "Soil Mechanics Engineer"
            ]
        },
        "Electrical & Electronics Engineering (EEE)": {
            "Power Systems": [
                "Power Systems Engineer",
                "Electrical Design Engineer",
                "Transmission Engineer",
                "Substation Engineer"
            ],
            "Control Systems": [
                "Control Systems Engineer",
                "Automation Engineer",
                "PLC Programmer"
            ],
            "Electrical Design": [
                "Electrical Design Engineer",
                "Lighting Design Engineer",
                "Panel Design Engineer"
            ],
            "Renewable Energy": [
                "Solar Energy Engineer",
                "Wind Energy Engineer",
                "Renewable Energy Consultant"
            ],
            "Automation": [
                "Industrial Automation Engineer",
                "SCADA Engineer",
                "Instrumentation Engineer"
            ]
        },
        "Information Technology (IT)": {
            "Software Development": [
                "Software Developer",
                "Application Developer",
                "Web Developer",
                "Mobile Developer"
            ],
            "Network & Systems Administration": [
                "Network Administrator",
                "System Administrator",
                "IT Support Engineer",
                "Network Engineer"
            ],
            "Cybersecurity": [
                "Security Analyst",
                "Network Security Engineer",
                "Cybersecurity Specialist"
            ],
            "Data Science": [
                "Data Analyst",
                "Data Scientist",
                "Business Analyst"
            ],
            "Cloud Computing": [
                "Cloud Engineer",
                "Cloud Administrator",
                "DevOps Engineer"
            ]
        },
        "Artificial Intelligence & Data Science (AI&DS)": {
            "Artificial Intelligence": [
                "AI Engineer",
                "AI Research Scientist",
                "AI Consultant",
                "AI Solutions Architect"
            ],
            "Machine Learning": [
                "Machine Learning Engineer",
                "ML Research Scientist",
                "Deep Learning Engineer",
                "Computer Vision Engineer"
            ],
            "Data Science": [
                "Data Scientist",
                "Senior Data Scientist",
                "Data Science Manager",
                "Applied Scientist"
            ],
            "Data Engineering": [
                "Data Engineer",
                "Big Data Engineer",
                "Data Architect",
                "ETL Developer"
            ]
        }
    },
    "B.Sc": {
        "Computer Science": {
            "Software Development": [
                "Junior Software Developer",
                "Web Developer",
                "Application Developer",
                "Software Programmer"
            ],
            "Data Analytics": [
                "Data Analyst",
                "Junior Data Scientist",
                "Business Analyst",
                "Analytics Associate"
            ],
            "Web Development": [
                "Frontend Developer",
                "Backend Developer",
                "Full Stack Developer",
                "Web Designer"
            ],
            "Database Management": [
                "Database Administrator",
                "SQL Developer",
                "Database Analyst"
            ]
        },
        "Mathematics": {
            "Data Science & Analytics": [
                "Data Analyst",
                "Statistical Analyst",
                "Quantitative Analyst",
                "Data Scientist"
            ],
            "Financial Analytics": [
                "Financial Analyst",
                "Risk Analyst",
                "Quantitative Analyst",
                "Actuarial Analyst"
            ],
            "Research & Academia": [
                "Research Analyst",
                "Mathematics Teacher",
                "Academic Researcher"
            ]
        },
        "Physics": {
            "Research & Development": [
                "Research Scientist",
                "R&D Engineer",
                "Laboratory Technician"
            ],
            "Data Science": [
                "Data Analyst",
                "Research Analyst",
                "Scientific Programmer"
            ],
            "Technical Writing": [
                "Technical Writer",
                "Science Communicator",
                "Content Writer"
            ]
        },
        "Chemistry": {
            "Pharmaceutical Industry": [
                "Quality Control Analyst",
                "Research Associate",
                "Production Chemist",
                "Analytical Chemist"
            ],
            "Laboratory Services": [
                "Laboratory Analyst",
                "Laboratory Manager",
                "Quality Assurance Analyst"
            ],
            "Research & Development": [
                "Research Scientist",
                "R&D Chemist",
                "Research Associate"
            ]
        },
        "Biology": {
            "Biotechnology": [
                "Biotechnology Analyst",
                "Research Associate",
                "Quality Control Analyst"
            ],
            "Pharmaceutical": [
                "Pharmaceutical Analyst",
                "Clinical Research Associate",
                "Drug Safety Associate"
            ],
            "Healthcare": [
                "Medical Laboratory Technician",
                "Clinical Research Coordinator",
                "Healthcare Analyst"
            ]
        },
        "Biotechnology": {
            "Biotechnology": [
                "Biotechnology Engineer",
                "Bioprocess Engineer",
                "Research Scientist"
            ],
            "Pharmaceutical": [
                "Pharmaceutical Researcher",
                "Quality Assurance Specialist",
                "Regulatory Affairs Associate"
            ],
            "Healthcare": [
                "Clinical Research Associate",
                "Medical Technologist",
                "Biomedical Analyst"
            ]
        },
        "Statistics": {
            "Data Science & Analytics": [
                "Data Analyst",
                "Statistical Analyst",
                "Business Intelligence Analyst",
                "Data Scientist"
            ],
            "Financial Analytics": [
                "Risk Analyst",
                "Quantitative Analyst",
                "Financial Analyst"
            ],
            "Research & Academia": [
                "Research Analyst",
                "Statistical Consultant",
                "Biostatistician"
            ]
        },
        "Data Science": {
            "Data Science": [
                "Data Scientist",
                "Junior Data Scientist",
                "Data Analyst",
                "Machine Learning Engineer"
            ],
            "Data Analytics": [
                "Data Analyst",
                "Business Intelligence Analyst",
                "Analytics Consultant"
            ],
            "Data Engineering": [
                "Data Engineer",
                "ETL Developer",
                "Big Data Engineer"
            ]
        },
        "Information Technology": {
            "Software Development": [
                "Software Developer",
                "Web Developer",
                "Application Developer"
            ],
            "Network Administration": [
                "Network Administrator",
                "System Administrator",
                "IT Support Specialist"
            ],
            "Data Analytics": [
                "Data Analyst",
                "Business Analyst",
                "IT Analyst"
            ]
        }
    },
    "B.Com": {
        "Accounting & Finance": {
            "Accounting": [
                "Junior Accountant",
                "Accounts Executive",
                "Tax Consultant",
                "Audit Associate",
                "Payroll Specialist",
                "Cost Accountant"
            ],
            "Financial Analysis": [
                "Financial Analyst",
                "Investment Analyst",
                "Credit Analyst",
                "Risk Analyst",
                "Equity Research Analyst"
            ],
            "Banking & Finance": [
                "Bank Officer",
                "Relationship Manager",
                "Credit Officer",
                "Loan Officer",
                "Treasury Analyst"
            ],
            "Auditing": [
                "Internal Auditor",
                "External Auditor",
                "Tax Auditor",
                "Compliance Auditor"
            ]
        },
        "Business Administration": {
            "Marketing": [
                "Marketing Executive",
                "Digital Marketing Specialist",
                "Brand Executive",
                "Market Research Analyst"
            ],
            "Human Resources": [
                "HR Executive",
                "Recruitment Specialist",
                "Training Coordinator",
                "HR Analyst"
            ],
            "Operations Management": [
                "Operations Executive",
                "Business Analyst",
                "Process Analyst"
            ],
            "Sales & Business Development": [
                "Sales Executive",
                "Business Development Associate",
                "Account Manager"
            ]
        },
        "Banking & Insurance": {
            "Banking": [
                "Bank Officer",
                "Credit Analyst",
                "Loan Officer",
                "Banking Associate"
            ],
            "Insurance": [
                "Insurance Advisor",
                "Claims Analyst",
                "Underwriter",
                "Risk Analyst"
            ]
        },
        "E-Commerce": {
            "E-Commerce Management": [
                "E-Commerce Executive",
                "Digital Marketing Specialist",
                "Online Sales Manager",
                "E-Commerce Analyst"
            ]
        },
        "Computer Applications": {
            "Data Analytics": [
                "Data Analyst",
                "Business Analyst",
                "Financial Analyst"
            ],
            "Software Development": [
                "Junior Developer",
                "Web Developer",
                "Application Developer"
            ]
        },
        "General Commerce": {
            "Finance": [
                "Accounts Executive",
                "Financial Analyst",
                "Tax Consultant"
            ],
            "Business Administration": [
                "Business Analyst",
                "Operations Executive",
                "Administrative Officer"
            ]
        }
    },
    "B.A": {
        "English Literature": {
            "Content Writing": [
                "Content Writer",
                "Copywriter",
                "Technical Writer",
                "Blog Writer",
                "SEO Content Writer",
                "Creative Writer"
            ],
            "Editing & Publishing": [
                "Editor",
                "Copy Editor",
                "Proofreader",
                "Publishing Assistant"
            ],
            "Digital Marketing": [
                "Content Marketing Specialist",
                "Social Media Manager",
                "Digital Marketing Executive"
            ]
        },
        "Economics": {
            "Data Analytics": [
                "Data Analyst",
                "Economic Analyst",
                "Research Analyst",
                "Business Analyst"
            ],
            "Financial Services": [
                "Financial Analyst",
                "Investment Analyst",
                "Economic Researcher"
            ]
        },
        "Psychology": {
            "Human Resources": [
                "HR Executive",
                "Recruitment Specialist",
                "Training & Development Specialist",
                "Organizational Psychologist"
            ],
            "Counseling & Therapy": [
                "Counselor",
                "Clinical Psychologist",
                "Therapist",
                "Mental Health Specialist"
            ]
        },
        "History": {
            "Content Writing": [
                "Content Writer",
                "Historical Researcher",
                "Museum Curator"
            ],
            "Research & Academia": [
                "Research Associate",
                "Historian",
                "Academic Researcher"
            ]
        },
        "Sociology": {
            "Social Research": [
                "Social Researcher",
                "Survey Analyst",
                "Community Analyst"
            ],
            "Human Resources": [
                "HR Executive",
                "Employee Relations Specialist"
            ]
        },
        "Political Science": {
            "Public Administration": [
                "Administrative Officer",
                "Policy Analyst",
                "Public Relations Officer"
            ],
            "Research & Analysis": [
                "Political Analyst",
                "Research Associate",
                "Policy Researcher"
            ]
        },
        "Journalism & Mass Communication": {
            "Journalism": [
                "Journalist",
                "Reporter",
                "News Editor",
                "Broadcast Journalist"
            ],
            "Digital Marketing": [
                "Social Media Manager",
                "Content Strategist",
                "Digital Marketing Specialist"
            ],
            "Public Relations": [
                "PR Executive",
                "Communications Manager",
                "Media Relations Specialist"
            ]
        }
    },
    "BCA": {
        "Computer Applications": {
            "Software Development": [
                "Software Developer",
                "Web Developer",
                "Application Developer",
                "Mobile Developer"
            ],
            "Database Management": [
                "Database Administrator",
                "Database Developer",
                "SQL Developer"
            ],
            "Web Development": [
                "Frontend Developer",
                "Backend Developer",
                "Full Stack Developer"
            ],
            "Network Administration": [
                "Network Administrator",
                "System Administrator",
                "IT Support Engineer"
            ]
        }
    },
    "BBA": {
        "Business Administration": {
            "Marketing": [
                "Marketing Executive",
                "Digital Marketing Specialist",
                "Brand Manager",
                "Market Research Analyst",
                "SEO Specialist",
                "Social Media Manager"
            ],
            "Human Resources": [
                "HR Executive",
                "Recruitment Specialist",
                "Training Coordinator",
                "HR Analyst",
                "Employee Relations Executive"
            ],
            "Operations Management": [
                "Operations Manager",
                "Business Analyst",
                "Process Manager",
                "Supply Chain Analyst"
            ],
            "Sales & Business Development": [
                "Sales Executive",
                "Business Development Manager",
                "Account Manager",
                "Client Relations Manager"
            ],
            "Finance": [
                "Financial Analyst",
                "Accounts Executive",
                "Business Analyst"
            ]
        }
    },
    "MCA": {
        "Computer Applications": {
            "Software Development": [
                "Software Engineer",
                "Senior Software Developer",
                "Full Stack Developer",
                "Application Architect"
            ],
            "Database Management": [
                "Database Administrator",
                "Database Architect",
                "Data Warehouse Engineer"
            ],
            "Web Development": [
                "Senior Web Developer",
                "Web Application Architect",
                "Frontend Architect"
            ],
            "Network Administration": [
                "Network Architect",
                "System Engineer",
                "IT Manager"
            ],
            "Data Science": [
                "Data Scientist",
                "Data Analyst",
                "Machine Learning Engineer"
            ]
        }
    },
    "MBA": {
        "Business Administration": {
            "Marketing Management": [
                "Marketing Manager",
                "Brand Manager",
                "Product Manager",
                "Digital Marketing Manager",
                "Growth Manager"
            ],
            "Human Resources Management": [
                "HR Manager",
                "Talent Acquisition Manager",
                "Training Manager",
                "HRBP (HR Business Partner)",
                "Compensation & Benefits Manager"
            ],
            "Finance Management": [
                "Finance Manager",
                "Financial Analyst",
                "Investment Manager",
                "Risk Manager",
                "Treasury Manager"
            ],
            "Operations Management": [
                "Operations Manager",
                "Supply Chain Manager",
                "Process Excellence Manager",
                "Project Manager"
            ],
            "Business Analytics": [
                "Business Analyst",
                "Analytics Manager",
                "Strategy Analyst",
                "Consulting Associate"
            ]
        }
    },
    "M.E / M.Tech": {
        "Computer Science & Engineering": {
            "Software Development": [
                "Senior Software Engineer",
                "Software Architect",
                "Technical Lead",
                "Engineering Manager"
            ],
            "Data Science & Analytics": [
                "Senior Data Scientist",
                "Data Science Manager",
                "ML Architect"
            ],
            "Artificial Intelligence": [
                "AI Research Scientist",
                "ML Engineer",
                "AI Architect"
            ]
        },
        "VLSI & Embedded Systems": {
            "VLSI Design": [
                "VLSI Design Engineer",
                "Physical Design Engineer",
                "Verification Engineer"
            ],
            "Embedded Systems": [
                "Senior Embedded Engineer",
                "Embedded Architect",
                "Firmware Lead"
            ]
        },
        "Data Science": {
            "Data Science": [
                "Data Scientist",
                "Senior Data Scientist",
                "ML Engineer"
            ],
            "Data Engineering": [
                "Senior Data Engineer",
                "Data Architect",
                "Big Data Engineer"
            ]
        },
        "Artificial Intelligence": {
            "AI Research": [
                "AI Research Scientist",
                "AI Engineer",
                "ML Research Scientist"
            ],
            "Machine Learning": [
                "Senior ML Engineer",
                "Deep Learning Engineer",
                "AI/ML Architect"
            ]
        },
        "Cybersecurity": {
            "Cybersecurity": [
                "Security Architect",
                "Senior Security Engineer",
                "Cybersecurity Consultant"
            ]
        }
    },
    "M.Sc": {
        "Computer Science": {
            "Software Development": [
                "Software Engineer",
                "Senior Developer",
                "Research Engineer"
            ],
            "Data Science": [
                "Data Scientist",
                "Senior Data Analyst",
                "Research Scientist"
            ]
        },
        "Mathematics": {
            "Data Science": [
                "Data Scientist",
                "Quantitative Analyst",
                "Research Scientist"
            ],
            "Financial Analytics": [
                "Quantitative Analyst",
                "Risk Analyst",
                "Financial Modeler"
            ]
        },
        "Statistics": {
            "Data Science": [
                "Data Scientist",
                "Statistical Analyst",
                "Biostatistician"
            ],
            "Research": [
                "Research Scientist",
                "Statistical Consultant",
                "Analytics Manager"
            ]
        },
        "Data Science": {
            "Data Science": [
                "Data Scientist",
                "Senior Data Scientist",
                "ML Engineer"
            ],
            "Data Analytics": [
                "Senior Data Analyst",
                "Analytics Manager",
                "Business Intelligence Manager"
            ]
        },
        "Physics": {
            "Research & Development": [
                "Research Scientist",
                "R&D Engineer",
                "Scientific Researcher"
            ],
            "Data Science": [
                "Data Scientist",
                "Computational Physicist",
                "Research Analyst"
            ]
        },
        "Chemistry": {
            "Research & Development": [
                "Research Scientist",
                "R&D Chemist",
                "Senior Research Associate"
            ]
        },
        "Biotechnology": {
            "Biotechnology": [
                "Biotechnology Researcher",
                "Senior Research Scientist",
                "Bioprocess Engineer"
            ]
        }
    },
    "M.Com": {
        "Finance & Accounting": {
            "Financial Analysis": [
                "Senior Financial Analyst",
                "Investment Analyst",
                "Financial Manager"
            ],
            "Accounting": [
                "Senior Accountant",
                "Finance Manager",
                "Audit Manager"
            ]
        },
        "Banking & Finance": {
            "Banking": [
                "Branch Manager",
                "Credit Manager",
                "Relationship Manager"
            ],
            "Finance": [
                "Finance Manager",
                "Treasury Manager",
                "Risk Manager"
            ]
        }
    },
    "Other": {
        "General / Custom Department": {
            "General Career Paths": [
                "Professional",
                "Consultant",
                "Analyst",
                "Manager",
                "Executive"
            ]
        }
    }
}

# Tamil Nadu Districts
TN_DISTRICTS = [
    "Ariyalur", "Chengalpattu", "Chennai", "Coimbatore", "Cuddalore",
    "Dharmapuri", "Dindigul", "Erode", "Kallakurichi", "Kanchipuram",
    "Kanyakumari", "Karur", "Krishnagiri", "Madurai", "Mayiladuthurai",
    "Nagapattinam", "Namakkal", "Nilgiris", "Perambalur", "Pudukkottai",
    "Ramanathapuram", "Ranipet", "Salem", "Sivaganga", "Tenkasi",
    "Thanjavur", "Theni", "Thoothukudi", "Tiruchirappalli", "Tirunelveli",
    "Tirupathur", "Tiruppur", "Tiruvannamalai", "Tiruvarur", "Vellore",
    "Viluppuram", "Virudhunagar"
]

# Cities by District (sample major cities)
DISTRICT_CITIES = {
    "Chennai": ["Chennai", "Tambaram", "Avadi", "Ambattur", "Madhavaram"],
    "Coimbatore": ["Coimbatore", "Pollachi", "Mettupalayam", "Valparai"],
    "Madurai": ["Madurai", "Melur", "Usilampatti", "Vadipatti"],
    "Salem": ["Salem", "Mettur", "Attur", "Edappadi"],
    "Tiruchirappalli": ["Tiruchirappalli", "Lalgudi", "Srirangam", "Thuraiyur"],
    # Add more as needed - using district name as default for others
}

def get_cities_for_district(district):
    """Get cities for a given district"""
    return DISTRICT_CITIES.get(district, [district])
