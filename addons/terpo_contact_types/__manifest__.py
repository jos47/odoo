{
    'name': 'Company Contact Relationship Types',
    'version': '16.0.1.0.0',
    'category': 'Contacts',
    'summary': 'Add relationship types to contacts',
    'description': 'Add many-to-many relationship types field to contacts',
    'depends': ['contacts'],
    'data': [
        'data/relationship_type_data.xml',  # Добавляем данные справочника
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}