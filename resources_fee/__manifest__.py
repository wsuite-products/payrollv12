# -*- coding: utf-8 -*-
# Copyright 2019-TODAY WSuite Products <wsuite-products@destiny.ws>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Resources',
    'summary': 'Resource Fee',
    'version': '12.0.1.0.0',
    'category': 'base',
    'website': 'https://destiny.ws/',
    'author': 'Destiny',
    'application': False,
    'installable': True,
    'depends': [
        'account',
        'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/resources_fee_view.xml',
        'views/res_partner_view.xml',
    ],
}
