# -*- coding: utf-8 -*-
{
    'name': 'Data approval',
    'version': '1.0',
    'category': 'Hidden',
    'author': 'Bima Wijaya',
    'summary': 'Module to setting users who will approve model',
    'description': """
    """,
    'depends': ['base_setup', 'mail'],
    'data': [
        'security/model_approval_security.xml',
        'security/ir.model.access.csv',
        'views/model_approval_view.xml',
        'views/ir_model_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
