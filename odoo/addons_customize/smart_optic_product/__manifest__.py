# -*- coding: utf-8 -*-
{
    'name': "Smart Optic Product",

    'summary': "Import and manage PARS optic products and their attributes.",

    'description': """
This module is designed to import PARS optic products along with their related attributes and values. 
It enables users to efficiently manage product specifications and customize product offerings 
by utilizing detailed attribute data. This functionality ensures a comprehensive approach to 
handling optic products within the system, enhancing organization and retrieval of product information.
    """,

    'author': "Mohammad Saeid Karbaschian",
    'website': "mskarbaschian@gmail.com",

    'category': 'Optic',
    "license": "AGPL-3",
    'version': '17.0.1.0.0',

    'depends': ['product_matrix','purchase_product_matrix','sale_product_matrix','optic_product_matrix'],

    'data': [
        "data/product_template.xml",
        "data/product.template.attribute.line.csv",
        "data/product_attribute.xml",
    ],
    'demo': [
        # "data/product_template.xml",
    ],
}
