# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Vehiculo(models.Model):
    _inherit = "viajes.vehiculo"

    description = fields.Html(
        string="Descripcion"
    )


