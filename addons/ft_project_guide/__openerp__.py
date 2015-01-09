# -*- coding: utf-8 -*-
{
    'name': 'Project Guide Module',
    'version': '0.2',
    'category': 'updis',
    'complexity': "easy",
    'description': """
Project Guide Module""",
    'author': 'Matt Cai',
    'website': 'http://odoosoft.com',
    'depends': ['base', 'ft_project'],
    'data': [
        'views/create_guide_view.xml',
        'views/menu.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    'application': True,
}
