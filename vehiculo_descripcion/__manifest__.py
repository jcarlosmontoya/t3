# -*- coding: utf-8 -*-
{
    'name': "Vehiculo Descripcion",

    'summary': """
        Agrega un campo descripcion al modelo 
        vehiculo de la gestion de viajes""",

    'description': """
        Agrega un campo descripcion al modelo 
        vehiculo de la gestion de viajes
    """,

    'author': "OEC",
    'website': "http://www.odooerpcloud.com",
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['gestion_viajes'],

    # always loaded
    'data': [
        'views/vehiculo_view.xml',
    ],
    'application': True,

}
