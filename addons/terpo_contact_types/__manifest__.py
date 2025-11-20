{
    'name': 'Company Contact Relationship Types',
    'version': '18.0.1.0.0',
    'category': 'Contacts',
    'summary': 'Add relationship types to contacts',
    'description': 'Add many-to-many relationship types field to contacts',
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',  # Добавь эту строку
        'data/relationship_type_data.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}