# -*- coding: utf-8 -*-
# Copyright 2019-TODAY WSuite Products <wsuite-products@destiny.ws>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Hr Recruitment Extended Destiny',
    'version': '12.0.1.0.0',
    'summary': 'Extends the Hr Recruitment Functionality for Destiny',
    'category': 'Human Resources',
    'author': 'Destiny',
    'license': 'AGPL-3',
    'maintainer': 'Destiny',
    'company': 'Destiny SAS',
    'website': 'https://destiny.ws/',
    'depends': [
               'hr_recruitment', 'contacts', 'postulants',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/jca_details_code_data.xml',
        'data/evaluation_template_data.xml',
        'data/hr_recruitment_data.xml',
        'data/types_of_charges_data.xml',
        'views/hr_stage_perc_view.xml',
        'views/jca_codes_view.xml',
        'views/hr_recruitment_stage_view.xml',
        'views/inherited_hr_applicant_view.xml',
        'views/inherited_res_partner_view.xml',
        'views/hr_evaluation_view.xml',
        'views/reason_disqualification_view.xml',
        'views/hr_job_view.xml',
        'views/types_of_charges.xml',
        'views/inherited_hr_employee_view.xml',
        'views/function_executed_view.xml',
        'views/work_group_view.xml',
        'views/macro_area_view.xml',
        'views/hr_employee_work_group_view.xml',
        'wizard/partner_state_selection_wizard_view.xml',
        'wizard/create_employee_wizard_view.xml',
        'wizard/wiz_hr_job_import_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}