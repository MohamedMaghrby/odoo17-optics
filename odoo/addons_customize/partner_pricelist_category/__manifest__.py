# -*- coding: utf-8 -*-
{
    'name': "partner pricelist category",

    'summary': "Adds relation between res.partner and product.pricelist by adding a category to res.partner",

    'description': """
This module adds a mew 'category' fields to res.partner model,
allowing users to assign categories to partners."
    """,

    'author': "Saeid Karbaschian",
    'website': "mskarbaschian@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/partner_pricelist_association.xml',
        'views/product_pricelist.xml',
        'views/sale_order.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
