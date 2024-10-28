# -*- coding: utf-8 -*-
{
    'name': "Optic Product Matrix",
    'summary': "Matrix implementation for selecting lens attributes.",
    'description': """
This module facilitates the management and selection of optic lenses by implementing a matrix 
for viewing and selecting lens attributes such as sphere and cylinder. 
The matrix displays lens attributes in three views:
1. Positive values for both sphere and cylinder.
2. Negative values for both sphere and cylinder.
3. A combination view with cylinders set at 0.25 more than the sphere.

This structured approach allows for easy selection and management of lens products, particularly those with complex specifications.
    """,

    'author': "Mohammad Saeid Karbaschian",
    'website': "mskarbaschian@gmail.com",

    'category': 'Optic',
    "license": "AGPL-3",
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['product_matrix'],

    'data': [
        'views/matrix_templates.xml',
        'data/product_attribute.xml',
        'data/product_template_attribute_value.xml',
    ],
    'demo': [
        # 'data/product_matrix_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            ('after', 'product_matrix/static/src/js/product_matrix_dialog.js',
             'optic_product_matrix/static/src/js/product_matrix_dialog.js'),
            'optic_product_matrix/static/src/js/product_matrix_dialog.js',
            ('replace', 'product_matrix/static/src/scss/product_matrix.scss',
             'optic_product_matrix/static/src/scss/product_matrix.scss'),
            ('replace', 'product_matrix/static/src/xml/**/*',
             'optic_product_matrix/static/src/xml/**/*'),
        ],
    },
}
