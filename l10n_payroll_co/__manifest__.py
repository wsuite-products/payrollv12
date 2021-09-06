# Copyright 2020-TODAY WSuite Products <wsuite-products@wsuite.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Payroll Localization Colombia',
    'version': '12.0.1.0.0',
    'summary': 'Payroll Localization Colombia',
    'category': 'Human Resources',
    'author': 'WSuite',
    'license': 'LGPL-3',
    'maintainer': 'WSuite',
    'company': 'WSuite SAS',
    'website': 'https://wsuite.com/',
    'depends': [
        'hr_payroll_income_withholding', 'hr_payroll_extended_werp'
    ],
    'data': [
        'data/hr_salary_rule_category.xml',
        'data/hr_salary_rule_data.xml',
        'data/hr_payroll_structure_data.xml',
        'data/hr_value_uvt_rf_data.xml',
        'data/hr_value_uvt_range_rf_data.xml',
        'data/hr_value_uvt_input_not_rf_data.xml',
        'data/hr_value_uvt_input_rf_data.xml',
    ],
    'installable': True,
}
