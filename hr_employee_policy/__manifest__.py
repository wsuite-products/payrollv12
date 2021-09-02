# -*- coding: utf-8 -*-
# Copyright 2019-TODAY WSuite Products <wsuite-products@destiny.ws>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'HR Employee Policy',
    'version': '12.0.1.0.0',
    'category': 'Human Resources',
    'author': 'Destiny',
    'maintainer': 'Destiny',
    'company': 'Destiny SAS',
    'website': 'https://destiny.ws/',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/employee_policy_data.xml',
        'wizard/hr_employee_policy_wizard_view.xml',
        'wizard/hr_policy_wizard_view.xml',
        'views/hr_policy_view.xml',
        'views/hr_employee_policy_view.xml',
        'views/contact_reference_view.xml',
        'views/hr_employee_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
