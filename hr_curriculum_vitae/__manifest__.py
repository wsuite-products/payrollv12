# -*- coding: utf-8 -*-
# Copyright 2019-TODAY WSuite Products <wsuite-products@wsuite.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'HR Curriculum Vitae WSuite',
    'version': '12.0.1.0.0',
    'summary': 'HR Curriculum Vitae Functionality for WSuite',
    'category': 'Human Resources',
    'author': 'WSuite',
    'license': 'LGPL-3',
    'maintainer': 'WSuite',
    'company': 'WSuite SAS',
    'website': 'https://wsuite.com/',
    'depends': [
               'product',
               'ir_attachment_s3_werp',
               'base_address_city',
               'hr_recruitment',
               'hr_employee_extended_werp',
    ],
    'data': [
        'views/hr_academic_area.xml',
        'views/hr_cv_pets.xml',
        'views/hr_cv_employee.xml',
        'views/hr_category_hobbies.xml',
        'views/hr_hobbies.xml',
        'views/hr_cv_hobbies_employee.xml',
        'views/hr_sports.xml',
        'views/hr_cv_sports_employee.xml',
        'views/hr_experience_time_view.xml',
        'views/hr_language.xml',
        'views/hr_cv_language_employee.xml',
        'views/hr_holding.xml',
        'views/hr_cv_holding_employee.xml',
        'views/hr_family_group_category_view.xml',
        'views/hr_family_relationship.xml',
        'views/hr_occupations.xml',
        'views/hr_cv_family_group_employee.xml',
        'views/hr_experience_area.xml',
        'views/hr_external_job_position.xml',
        'views/hr_type_contract.xml',
        'views/hr_cv_laboral_experience.xml',
        'views/hr_academic_institution.xml',
        'views/hr_academic_level.xml',
        'views/hr_cv_academic_studies.xml',
        'views/hr_competition_language.xml',
        'views/hr_competition_level_language.xml',
        'views/hr_cv_personal_reference_employee.xml',
        'views/hr_cv_personal_employee_type.xml',
        'views/hr_employee_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
