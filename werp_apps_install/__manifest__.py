# Copyright 2020-TODAY WSuite Products <wsuite-products@wsuite.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Werp Apps Install',
    'version': '12.0.1.0.0',
    'summary': 'Werp Apps Install',
    'category': 'Administration',
    'author': 'WSuite',
    'license': 'LGPL-3',
    'maintainer': 'WSuite',
    'company': 'WSuite SAS',
    'website': 'https://wsuite.com/',
    'depends': [
        'hr_payroll',
    ],
    'data': [
        'views/inherited_res_config_settings_view.xml',
    ],
    'installable': True,
    'application': True,
}
