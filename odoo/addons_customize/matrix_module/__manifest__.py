# -*- coding: utf-8 -*-
{
    'name': "Matrix module",

    'summary': "A helper module to add product in Quotation, Price list matrix data",

    'description': """
Long description of module's purpose
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
        'views/matrix_input.xml',
        'views/sale_order_form.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
