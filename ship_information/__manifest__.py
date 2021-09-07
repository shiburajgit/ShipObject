# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Ship Information',
    'version' : '1.1',
    'summary': 'Ship Information details',
    'sequence': 10,
    'description': """Ship Information details""",
    'category': 'Productivity',
    'website': '',
    'depends': ['sale', 'mail', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/ship_information_view.xml',
        'views/user_ship.xml',
        'views/sale_ship_info.xml',
        'views/so_line.xml',
        'views/related_purchase.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
