"""
Role-specific content for career guidance output
"""

ROLE_CONTENT = {
    'Data Analyst': {
        'description': 'A Data Analyst transforms raw data into meaningful insights that help businesses make informed decisions. They collect, process, and analyze data to identify trends, patterns, and opportunities.',
        'responsibilities': [
            'Extract and clean data from various sources (databases, APIs, files)',
            'Perform statistical analysis to identify trends and patterns',
            'Create visualizations and dashboards using tools like Tableau or Power BI',
            'Present insights and recommendations to stakeholders',
            'Collaborate with teams to solve business problems',
            'Automate reporting processes using Python/SQL'
        ],
        'benefits': [
            {'title': 'High Demand', 'desc': 'Every company needs data analysts', 'icon': 'check-circle', 'color': 'success'},
            {'title': 'Growth', 'desc': 'Path to Data Scientist, ML Engineer', 'icon': 'chart-line', 'color': 'info'},
            {'title': 'Good Salary', 'desc': '₹3-6 LPA entry, ₹12-25 LPA senior', 'icon': 'rupee-sign', 'color': 'warning'},
            {'title': 'Remote Work', 'desc': 'Many companies offer WFH', 'icon': 'laptop-code', 'color': 'primary'}
        ],
        'stats': {
            'experience': '0-2 years to start',
            'work_type': 'Office/Hybrid/Remote',
            'industry': 'IT, Finance, E-commerce',
            'openings': '50,000+ annually',
            'avg_package': '₹4.5 LPA'
        },
        'skills': {
            'technical': [
                {'name': 'SQL', 'importance': 'Core', 'level': 95},
                {'name': 'Python/R', 'importance': 'Core', 'level': 90},
                {'name': 'Tableau / Power BI', 'importance': 'Important', 'level': 85},
                {'name': 'Excel (Advanced)', 'importance': 'Foundation', 'level': 90},
                {'name': 'Statistics & Math', 'importance': 'Core', 'level': 75},
                {'name': 'Git & Version Control', 'importance': 'Nice to Have', 'level': 60}
            ],
            'soft': [
                {'name': 'Problem Solving', 'stars': 5, 'desc': 'Ability to break down complex problems'},
                {'name': 'Communication', 'stars': 5, 'desc': 'Present insights to non-technical stakeholders'},
                {'name': 'Business Acumen', 'stars': 4, 'desc': 'Understand business context'},
                {'name': 'Attention to Detail', 'stars': 5, 'desc': 'Accuracy in data analysis'}
            ]
        },
        'companies': {
            'mass_recruiters': ['TCS', 'Wipro', 'Infosys', 'Cognizant', 'Accenture', 'Capgemini'],
            'product': ['Amazon', 'Flipkart', 'Swiggy', 'Zomato', 'PhonePe', 'Paytm'],
            'analytics': ['Mu Sigma', 'LatentView', 'Tiger Analytics', 'Fractal Analytics'],
            'consulting': ['Deloitte', 'PwC', 'EY', 'KPMG']
        },
        'certifications': [
            {'name': 'Google Data Analytics', 'provider': 'Coursera', 'cost': 'Free (Audit)', 'paid': '$49/month', 'duration': '6 months', 'rating': 'Highly Recommended'},
            {'name': 'Microsoft Power BI Data Analyst (PL-300)', 'provider': 'Microsoft', 'cost': '$165 exam fee', 'duration': '2-3 months prep', 'rating': 'Industry Standard'},
            {'name': 'Tableau Desktop Specialist', 'provider': 'Tableau', 'cost': '$100', 'duration': '1-2 months', 'rating': 'Good for Portfolio'},
            {'name': 'IBM Data Analyst Professional', 'provider': 'Coursera', 'cost': 'Free (Audit)', 'paid': '$49/month', 'duration': '8 months', 'rating': 'Comprehensive'}
        ]
    },
    
    'Data Scientist': {
        'description': 'A Data Scientist builds machine learning models, conducts advanced statistical analysis, and extracts valuable insights from complex, large-scale data sets to drive business decisions.',
        'responsibilities': [
            'Develop and deploy machine learning models',
            'Conduct statistical analysis and hypothesis testing',
            'Work with big data technologies (Hadoop, Spark)',
            'Build predictive models for business forecasting',
            'Research and implement cutting-edge ML algorithms',
            'Collaborate with engineers to productionize models'
        ],
        'benefits': [
            {'title': 'High Pay', 'desc': '₹6-12 LPA entry, ₹20-50 LPA senior', 'icon': 'rupee-sign', 'color': 'success'},
            {'title': 'Innovation', 'desc': 'Work on cutting-edge AI/ML projects', 'icon': 'robot', 'color': 'info'},
            {'title': 'High Demand', 'desc': 'One of the hottest careers globally', 'icon': 'fire', 'color': 'danger'},
            {'title': 'Impact', 'desc': 'Solve real-world problems with data', 'icon': 'chart-line', 'color': 'primary'}
        ],
        'stats': {
            'experience': '1-3 years to start',
            'work_type': 'Office/Hybrid/Remote',
            'industry': 'Tech, Finance, Healthcare, E-commerce',
            'openings': '40,000+ annually',
            'avg_package': '₹8 LPA'
        },
        'skills': {
            'technical': [
                {'name': 'Python', 'importance': 'Core', 'level': 95},
                {'name': 'Machine Learning', 'importance': 'Core', 'level': 90},
                {'name': 'Deep Learning', 'importance': 'Important', 'level': 80},
                {'name': 'Statistics & Probability', 'importance': 'Core', 'level': 85},
                {'name': 'SQL & Databases', 'importance': 'Important', 'level': 80},
                {'name': 'Big Data (Spark/Hadoop)', 'importance': 'Nice to Have', 'level': 65}
            ],
            'soft': [
                {'name': 'Research Skills', 'stars': 5, 'desc': 'Read and implement research papers'},
                {'name': 'Problem Solving', 'stars': 5, 'desc': 'Complex algorithmic thinking'},
                {'name': 'Communication', 'stars': 4, 'desc': 'Explain complex models simply'},
                {'name': 'Curiosity', 'stars': 5, 'desc': 'Continuous learning mindset'}
            ]
        },
        'companies': {
            'product': ['Google', 'Microsoft', 'Amazon', 'Meta', 'Netflix'],
            'indian_product': ['Flipkart', 'Swiggy', 'Ola', 'PhonePe', 'CRED'],
            'analytics': ['Mu Sigma', 'Tiger Analytics', 'Fractal Analytics', 'LatentView'],
            'consulting': ['McKinsey', 'BCG', 'Bain', 'Deloitte AI']
        },
        'certifications': [
            {'name': 'IBM Data Science Professional', 'provider': 'Coursera', 'cost': '$49/month', 'duration': '10 months', 'rating': 'Highly Recommended'},
            {'name': 'TensorFlow Developer Certificate', 'provider': 'Google', 'cost': '$100', 'duration': '3-4 months', 'rating': 'Industry Standard'},
            {'name': 'AWS ML Specialty', 'provider': 'Amazon', 'cost': '$300 exam', 'duration': '4-6 months', 'rating': 'Advanced'},
            {'name': 'Fast.ai Deep Learning', 'provider': 'Fast.ai', 'cost': 'Free', 'duration': '7 weeks', 'rating': 'Practical'}
        ]
    },
    
    'Software Engineer': {
        'description': 'A Software Engineer designs, develops, tests, and maintains software applications. They write code to solve problems and build products that millions of people use every day.',
        'responsibilities': [
            'Write clean, efficient, and maintainable code',
            'Design system architecture and databases',
            'Debug and fix software issues',
            'Collaborate using Git and Agile methodologies',
            'Participate in code reviews and testing',
            'Deploy and monitor applications in production'
        ],
        'benefits': [
            {'title': 'Best Salaries', 'desc': '₹4-8 LPA entry, ₹15-60 LPA senior', 'icon': 'rupee-sign', 'color': 'success'},
            {'title': 'High Demand', 'desc': 'Thousands of openings monthly', 'icon': 'briefcase', 'color': 'info'},
            {'title': 'Global Opportunities', 'desc': 'Work for companies worldwide', 'icon': 'globe', 'color': 'primary'},
            {'title': 'Remote Work', 'desc': 'Work from anywhere', 'icon': 'home', 'color': 'warning'}
        ],
        'stats': {
            'experience': '0-1 years to start',
            'work_type': 'Office/Hybrid/Remote',
            'industry': 'IT, Startups, Product Companies',
            'openings': '100,000+ annually',
            'avg_package': '₹5.5 LPA'
        },
        'skills': {
            'technical': [
                {'name': 'Programming (Java/Python/JavaScript)', 'importance': 'Core', 'level': 95},
                {'name': 'Data Structures & Algorithms', 'importance': 'Core', 'level': 90},
                {'name': 'System Design', 'importance': 'Important', 'level': 75},
                {'name': 'Databases (SQL/NoSQL)', 'importance': 'Important', 'level': 85},
                {'name': 'Git & Version Control', 'importance': 'Core', 'level': 80},
                {'name': 'Cloud (AWS/Azure/GCP)', 'importance': 'Nice to Have', 'level': 70}
            ],
            'soft': [
                {'name': 'Problem Solving', 'stars': 5, 'desc': 'Algorithmic thinking and debugging'},
                {'name': 'Collaboration', 'stars': 5, 'desc': 'Work effectively in teams'},
                {'name': 'Learning Agility', 'stars': 5, 'desc': 'Keep up with new technologies'},
                {'name': 'Communication', 'stars': 4, 'desc': 'Technical documentation and discussions'}
            ]
        },
        'companies': {
            'faang': ['Google', 'Amazon', 'Microsoft', 'Apple', 'Meta'],
            'indian_product': ['Flipkart', 'Zomato', 'Swiggy', 'Razorpay', 'CRED'],
            'service': ['TCS', 'Infosys', 'Wipro', 'HCL', 'Tech Mahindra'],
            'startups': ['Zerodha', 'PhonePe', 'Dream11', 'Meesho', 'UrbanCompany']
        },
        'certifications': [
            {'name': 'AWS Certified Developer', 'provider': 'Amazon', 'cost': '$150', 'duration': '3-4 months', 'rating': 'Industry Standard'},
            {'name': 'Oracle Java Certification', 'provider': 'Oracle', 'cost': '$245', 'duration': '2-3 months', 'rating': 'Good for Java Devs'},
            {'name': 'Meta React Certificate', 'provider': 'Coursera', 'cost': '$49/month', 'duration': '5 months', 'rating': 'For Frontend'},
            {'name': 'Google Cloud Developer', 'provider': 'Google', 'cost': '$200', 'duration': '3-4 months', 'rating': 'Cloud-focused'}
        ]
    },
    
    'Full Stack Developer': {
        'description': 'A Full Stack Developer works on both frontend (user interface) and backend (server, database) of web applications, handling the complete software development lifecycle.',
        'responsibilities': [
            'Build responsive user interfaces with React/Angular/Vue',
            'Develop RESTful APIs and backend services',
            'Design and manage databases',
            'Implement authentication and authorization',
            'Deploy applications to cloud platforms',
            'Optimize application performance and security'
        ],
        'benefits': [
            {'title': 'Versatility', 'desc': 'Work on complete products independently', 'icon': 'layer-group', 'color': 'success'},
            {'title': 'High Demand', 'desc': 'Startups love full-stack developers', 'icon': 'rocket', 'color': 'info'},
            {'title': 'Good Pay', 'desc': '₹4-9 LPA entry, ₹18-40 LPA senior', 'icon': 'rupee-sign', 'color': 'warning'},
            {'title': 'Entrepreneurship', 'desc': 'Build your own products/startups', 'icon': 'lightbulb', 'color': 'primary'}
        ],
        'stats': {
            'experience': '0-2 years to start',
            'work_type': 'Office/Hybrid/Remote',
            'industry': 'Startups, Product Companies, Agencies',
            'openings': '60,000+ annually',
            'avg_package': '₹6 LPA'
        },
        'skills': {
            'technical': [
                {'name': 'React/Angular/Vue', 'importance': 'Core', 'level': 90},
                {'name': 'Node.js/Express', 'importance': 'Core', 'level': 90},
                {'name': 'MongoDB/PostgreSQL', 'importance': 'Core', 'level': 85},
                {'name': 'HTML/CSS/JavaScript', 'importance': 'Core', 'level': 95},
                {'name': 'Git & Version Control', 'importance': 'Important', 'level': 80},
                {'name': 'Docker & Kubernetes', 'importance': 'Nice to Have', 'level': 65}
            ],
            'soft': [
                {'name': 'Multi-tasking', 'stars': 5, 'desc': 'Handle frontend and backend simultaneously'},
                {'name': 'Problem Solving', 'stars': 5, 'desc': 'Debug across the entire stack'},
                {'name': 'Time Management', 'stars': 4, 'desc': 'Balance multiple responsibilities'},
                {'name': 'Continuous Learning', 'stars': 5, 'desc': 'Keep up with both frontend and backend trends'}
            ]
        },
        'companies': {
            'startups': ['Razorpay', 'CRED', 'Meesho', 'UrbanCompany', 'Groww'],
            'product': ['Flipkart', 'Swiggy', 'Zomato', 'PhonePe', 'Paytm'],
            'agencies': ['Accenture', 'Thoughtworks', 'Nagarro', 'Publicis Sapient'],
            'service': ['TCS Digital', 'Infosys Digital', 'Wipro Digital', 'HCL Digital']
        },
        'certifications': [
            {'name': 'Meta Full-Stack Engineer', 'provider': 'Coursera', 'cost': '$49/month', 'duration': '7 months', 'rating': 'Highly Recommended'},
            {'name': 'MongoDB Developer Path', 'provider': 'MongoDB University', 'cost': 'Free', 'duration': '2-3 months', 'rating': 'Database-focused'},
            {'name': 'AWS Full Stack Development', 'provider': 'AWS', 'cost': '$150', 'duration': '4 months', 'rating': 'Cloud-focused'},
            {'name': 'FreeCodeCamp Certifications', 'provider': 'FreeCodeCamp', 'cost': 'Free', 'duration': '6-12 months', 'rating': 'Beginner-friendly'}
        ]
    }
}

# Default content for roles not in the dictionary
DEFAULT_ROLE_CONTENT = {
    'description': 'A professional who applies specialized skills and domain knowledge to solve real-world problems and create value for organizations.',
    'responsibilities': [
        'Apply domain-specific knowledge to solve complex problems',
        'Collaborate with cross-functional teams effectively',
        'Continuously learn new technologies and methodologies',
        'Deliver high-quality work within project deadlines',
        'Communicate effectively with stakeholders',
        'Stay updated with industry trends and best practices'
    ],
    'benefits': [
        {'title': 'Good Demand', 'desc': 'Growing job market in this domain', 'icon': 'briefcase', 'color': 'success'},
        {'title': 'Career Growth', 'desc': 'Multiple advancement opportunities', 'icon': 'chart-line', 'color': 'info'},
        {'title': 'Good Salary', 'desc': 'Competitive compensation packages', 'icon': 'rupee-sign', 'color': 'warning'},
        {'title': 'Work-Life Balance', 'desc': 'Flexible work arrangements', 'icon': 'clock', 'color': 'primary'}
    ],
    'stats': {
        'experience': '0-2 years to start',
        'work_type': 'Office/Hybrid',
        'industry': 'Various sectors',
        'openings': '20,000+ annually',
        'avg_package': '₹4 LPA'
    },
    'skills': {
        'technical': [
            {'name': 'Core Domain Skills', 'importance': 'Core', 'level': 85},
            {'name': 'Software Tools', 'importance': 'Important', 'level': 75},
            {'name': 'Technical Communication', 'importance': 'Important', 'level': 70},
            {'name': 'Problem Solving', 'importance': 'Core', 'level': 80}
        ],
        'soft': [
            {'name': 'Communication', 'stars': 5, 'desc': 'Effective stakeholder communication'},
            {'name': 'Teamwork', 'stars': 5, 'desc': 'Collaborate with diverse teams'},
            {'name': 'Adaptability', 'stars': 4, 'desc': 'Learn and adapt quickly'},
            {'name': 'Time Management', 'stars': 4, 'desc': 'Meet deadlines consistently'}
        ]
    },
    'companies': {
        'major': ['Leading companies in the domain'],
        'mid_size': ['Growing mid-sized firms'],
        'startups': ['Innovative startups'],
        'consulting': ['Consulting firms']
    },
    'certifications': [
        {'name': 'Domain-specific Certification', 'provider': 'Industry Standard', 'cost': 'Varies', 'duration': '3-6 months', 'rating': 'Recommended'}
    ]
}

def get_role_content(role_name):
    """Get content for a specific role, with fallback to default"""
    return ROLE_CONTENT.get(role_name, DEFAULT_ROLE_CONTENT)


if __name__ == "__main__":
    print("\n" + "="*70)
    print("⚠️  This is a data module file, not the main application!")
    print("="*70)
    print("\n📌 To run the PathGuide application:")
    print("   1. Open 'app.py' in the editor")
    print("   2. Click the 'Run Python File' button")
    print("   3. Or run: python app.py")
    print("\n" + "="*70 + "\n")
