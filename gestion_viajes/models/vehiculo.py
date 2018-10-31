# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Vehiculo(models.Model):
    _name = "viajes.vehiculo"

    name = fields.Char(string="Nombre", help="Nombre")
    image = fields.Binary(string="Imagen", help="Imagen vehiculo")

    matricula = fields.Char(string="Matricula", help="Nº de placa", size=6)
    anio = fields.Char(string="Año", help="Edad del Camion")
    color = fields.Selection(
        selection=[
            ('negro', "Negro"),
            ('blanco', "Blanco"),
            ('azul', "Azul"),
            ('rojo', "Rojo"),
        ],
        string="Color",
        help="Escoja un color")
    conductor_id = fields.Many2one(
        comodel_name="viajes.conductor",
        string="Conductor",
        help="El conductor al que pertenece este vehiculo")
