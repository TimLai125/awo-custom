# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Supplier Location Ext',
    'category': 'Stock',
    'version': '8.0.1.0.0',
    'author': 'Quartile Limited',
    'website': 'https://www.quartile.co',
    'depends': [
        'supplier_stock',
        'product_offer',
        'product_listprice_list_view',
    ],
    'summary': """""",
    'description': """
- Add "HK Location" field to classify the supplier location.
- Overwrite/hook methods that are related to qty_overseas and qty_local_stock
    """,
    'data': [
        'data/ir_actions.xml',
        'views/product_product_views.xml',
        'views/product_template_views.xml',
        'views/supplier_location_views.xml',
    ],
    'installable': True,
}
