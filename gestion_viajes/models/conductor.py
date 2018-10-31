# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Conductor(models.Model):
    _name = "viajes.conductor"

    name = fields.Char(string="Nombre", help="Nombre del conductor")
    pais = fields.Char(string="Pais", help="Seleccione el pais del conductor")
    # truck_ids = fields.Char(string="Camiones", help="Lista de camiones")
