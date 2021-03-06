# -*- coding: utf-8 -*-
# Copyright 2015-2017 Quartile Limted
# Copyright 2017 eHanse
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Stock View Adjust OAW',
    'summary': '',
    'version': '8.0.1.1.1',
    'category': 'Stock',
    'author': 'Quartile Limited',
    'website': 'https://www.odoo-asia.com',
    'description': """
    """,
    "license": "AGPL-3",
    'application': False,
    'installable': True,
    'auto_install': False,
    'images' : [],
    'depends': [
        'sale_line_quant_extended',
        'stock_picking_menu',
    ],
    'data': [
        'views/stock_move_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_quant_views.xml',
    ],
}
