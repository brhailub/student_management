{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Manage students and teachers',
    'description': """
        Comprehensive student management system with teacher relationships
    """,
    'author': 'Biruk Hailu',
    'category': 'Education',
    'depends': ['base', 'hr', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'security/security_rules.xml',
        'data/sequence.xml',
        'views/person_views.xml',
        'views/student_views.xml',
        'views/employee_views.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'student_management/static/src/js/student_management.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}