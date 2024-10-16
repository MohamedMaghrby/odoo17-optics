# -*- coding: utf-8 -*-
{
    'name': "product_variant",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "MAX-ERP",
    'website': "https://www.MAX-ERP.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'MAXERP',
    "license": "AGPL-3",
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_product_matrix'],

    # always loaded
    'data': [
        "data/product_template.xml",
        "data/product_attribute.xml",
        "data/product_template_attribute_value.xml",
        # "data/product_template_attribute_line.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        "data/product_template.xml",
    ],
}
