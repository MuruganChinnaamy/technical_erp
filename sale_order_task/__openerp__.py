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
    'name': "Task3 ",
    'version': '1.0',
    'license': '',
    'author': "Murugan Chinnasamy",
    'website': "",
    'category': 'sales ',
    'summary': """Customizing the  sales Oreder Line""",
    'description': """
Customizing the  sales Oreder Line
===========================================================

* dd new one2many field after the existing sale order line and update its values whenever the new data is updated in the SO line.

TODO
----
* Customizing the sale Order Lines
    """,
    
    'depends' : ['base', 'account', 'sale', 'sale_crm', 'purchase', 'maintenance', 'stock', 'crm', 'hr', 'project_issue', 'project'],
        
   

    'data': [
            
           
            'views/sale.xml',
	  
        	    ],

    'qweb': [],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,

}
