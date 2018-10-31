# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Viaje(models.Model):
    _name = "viajes.viaje"

    # conductor_id
    # truck_id
    fecha = fields.Datetime(string="Fecha")
    origen = fields.Char("Ciudad Origen")
    destino = fields.Char("Ciudad Destino")
    kms = fields.Integer("Kilometros")
    coste = fields.Float("Precio")
    ida_vuelta = fields.Boolean("Ida y Vuelta?")

