# -*- coding: utf-8 -*-
{
    'name': "Gestion viajes",

    'summary': """
        Modulo gestion Viajes en Odoo 11""",

    'description': """
        Modulo gestion Viajes en Odoo 11
    """,

    'author': "OEC",
    'website': "http://www.odooerpcloud.com",
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/conductor_view.xml',
        'views/vehiculo_view.xml',
    ],
    'application': True,

}
