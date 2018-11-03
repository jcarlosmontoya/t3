# -*- coding: utf-8 -*-
{
    'name': "Product Tipology",

    'summary': """
       Agrega el campo tipologia al producto template""",

    'description': """
         Agrega el campo tipologia al producto template
    """,

    'author': "BulldogSoft",
    'website': "http://www.yourcompany.com",


    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_view.xml',
    ],
    "application": True,
}
