# -*- coding: utf-8 -*-
# Copyright 2019-TODAY WSuite Products <wsuite-products@destiny.ws>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class ContentConfig(models.Model):
    _name = "content.config"
    _description = 'Content Config'

    name = fields.Char('Name', required=True)
    user_id = fields.Many2one('res.users', string='User', required=False, default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string='Partner')
    brand_id = fields.Many2one('multi.brand', string='Brand')
    json_data = fields.Text('Json Data')
