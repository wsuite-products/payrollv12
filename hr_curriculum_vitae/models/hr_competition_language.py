# -*- coding: utf-8 -*-
# Copyright 2019-TODAY WSuite Products <wsuite-products@destiny.ws>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class HRCompetitionLanguage(models.Model):
    """This Class is used to define fields
    and methods for HR Competition Language."""

    _name = "hr.competition.language"
    _description = "HR Competition Language"

    name = fields.Char()
    description = fields.Text()
    active = fields.Boolean(default=True)