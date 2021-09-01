# -*- coding: utf-8 -*-
# Copyright 2019-TODAY WSuite Products <wsuite-products@destiny.ws>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class HRHolding(models.Model):
    """This Class is used to define fields and methods for HR Holding."""

    _name = "hr.holding"
    _description = "HR Holding"

    name = fields.Char()
    description = fields.Text()
    land_type = fields.Selection([
        ('property', 'Property'),
        ('realstate', 'Realstate'),
    ], string="Holding Type", default='property')
    active = fields.Boolean(default=True)
