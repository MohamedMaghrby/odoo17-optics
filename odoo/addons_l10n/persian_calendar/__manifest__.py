# -*- coding: utf-8 -*-
{
    'name': "persian_calendar",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'persian_calendar/static/src/js/main.js',
            'persian_calendar/static/src/js/persian-date.js',
            'persian_calendar/static/src/js/farvardin.js',
            'persian_calendar/static/src/js/datetimepicker_service.js',
            'persian_calendar/static/src/js/loader.js',
        ],
        'persian_calendar.calendar_persian': [
            'persian_calendar/static/src/js/format_utils.js',
            'persian_calendar/static/src/js/list.js',
            'persian_calendar/static/src/js/datetime_field.js',
            'persian_calendar/static/src/js/jdatetime.js',
            'persian_calendar/static/src/js/calendar_hook.js',
            'persian_calendar/static/src/js/jfullcalendar.js',
        ]
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
