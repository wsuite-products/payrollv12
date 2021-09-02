# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Payslip Compare',
    'version': '12.0.1.0.0',
    'summary': """
    Provides the ability to compare payslips of two different month of"""
    """ multiple employees at a time.""",
    'sequence': 15,
    'category': 'Human Resources',
    'author': 'Destiny',
    'license': 'LGPL-3',
    'maintainer': 'Destiny',
    'company': 'Destiny SAS',
    'website': 'https://destiny.ws/',
    'description': """
    Provides the ability to compare payslips of two different month of"""
    """multiple employees at a time.
    """,
    'depends': ['hr_payroll'],
    'data': [
        'security/payslip_compare_security.xml',
        'security/ir.model.access.csv',
        'views/payslip_compare_result_view.xml',
        'wizard/payslip_compare_view.xml',
    ],
    'installable': True,
    'application': True,
}
