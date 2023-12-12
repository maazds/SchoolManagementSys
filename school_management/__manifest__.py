# -*- coding: utf-8 -*-
{
    'name': "School Management System",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/student_leave_view.xml',
        'wizards/library_book.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/teacher_view.xml',
        'views/teacher_template.xml',
        'views/student_view.xml',
        'views/student_template.xml',
        'views/course_view.xml',
        'views/subject_view.xml',
        'views/room_view.xml',
        'views/student_fee.xml',
        'views/fee_view.xml',
        'views/library.xml',
        'views/library_issue_books.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
