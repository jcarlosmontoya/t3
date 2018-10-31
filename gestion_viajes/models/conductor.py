# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Conductor(models.Model):
    _name = "viajes.conductor"

    name = fields.Char(string="Nombre", help="Nombre del conductor")
    pais = fields.Many2one(
        comodel_name="res.country",
        string="Pais",
        help="Seleccione el pais del conductor")
    truck_ids = fields.One2many(
        comodel_name="viajes.vehiculo",
        inverse_name="conductor_id",
        string="Camiones",
        help="Lista de camiones")

    total_trucks = fields.Integer(
        compute="_get_truck_count",
        string="Cuantos vehiculos",
    )

    def _get_truck_count(self):
        for conductor in self:
            conductor.total_trucks = len(conductor.truck_ids)
