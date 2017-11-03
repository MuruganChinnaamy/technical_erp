
# -*- coding: utf-8 -*-
{
    'name': "Create User Wizard",
    'summary': """Demo for Create User wizard""",
    'author': "Murugan C",
    'company': 'Demo ',
    'website': "http://www.demo.com",
    'category': 'Tool',
    'description': """
This is easy user creation wizard
========================================

It supports:
------------
    - to see user settings
    - creating user

If you need to verify the user kindly go settings -> Users -> Users
    """, 
    'version': '1.0',
    'depends': ['base', 'point_of_sale'],
    'data': [
	     'views/templates.xml',
             'wizard/user_groups.xml',
             'wizard/view_create_new_user_wizard.xml',
             ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
