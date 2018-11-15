# -*- coding: utf-8 -*-

from odoo import api, fields, exceptions, models


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

    licencia = fields.Char("Licencia conducir", size=8)

    fecha_caducidad = fields.Date("Fecha caducidad licencia")

    @api.model
    def default_get(self, values):
        res = super(Conductor, self).default_get(values)
        # por defecto un nuevo conductor es de El Salvador
        # search, search_read, browse
        domain = [['code', '=', 'SV']]
        country_search = self.env['res.country'].search(domain, limit=1)
        country_browse = self.env['res.country'].browse([209])
        country_search_read = self.env['res.country'].search_read(
            domain, ['name', 'code'])
        if country_search:
            res['pais'] = country_search.id

        return res

    @api.onchange("pais")
    def onchange_pais(self):
        if self.fecha_caducidad:
            if self.fecha_caducidad < fields.Date.today():
                raise exceptions.Warning("Ojo la licencia esta caducada")
        stop = True

    def _get_truck_count(self):
        for conductor in self:
            conductor.total_trucks = len(conductor.truck_ids)
