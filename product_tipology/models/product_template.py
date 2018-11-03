# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    tipology = fields.Selection(
        selection=[
            ('plastico', 'Plastico'),
            ('metal', 'Metal'),
            ('organico', 'Organico'),
        ],
        string="Tipology"
    )

