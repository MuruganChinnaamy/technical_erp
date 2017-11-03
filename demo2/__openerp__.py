# -*- coding: utf-8 -*-
##############################################################################
#
#   Leaves Mail Trigger and one2many modification
#   Copyright 2015 RGB Consulting, SL
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Leaves Mail Trigger",
    'version': '1.0',
    'depends': ['point_of_sale'],
    'license': '',
    'author': "Murugan Chinnasamy",
    'website': "",
    'category': 'HR, Leave Management',
    'summary': """HR, Leave Management """,
    'description': """
Customizing the HR, Leave Management 
===========================================================
* If an Employee applies leave twice in a month with the same leave type, trigger an email alert to the employee's manager (create qweb email template).
* 

TODO
----
* Customizing the HR Holidays 
    """,
    
    'depends': [
        'mail',
        'hr',
        'hr_contract',
        'hr_holidays',
        'decimal_precision',
        'report',
        
    ],

    'data': [
            
            'views/hr_holidays.xml',
            #'views/sale.xml',
	       'views/user_groups.xml',
           #'views/mail_template.xml',
           'views/leave_report_employee.xml',
           'views/demo2_report.xml',
           'mail/template_mail.xml',
        	    ],

    'qweb': [],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,

}
