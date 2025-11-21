from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    relationship_type_ids = fields.Many2many(
        'relationship.type',
        string='Типы отношений',
        #help='Types of relationships with this contact'
    )

class RelationshipType(models.Model):
    _name = 'relationship.type'
    _description = 'Relationship Type'
    _order = 'name'

    name = fields.Char(string='Type Name', required=True)
    active = fields.Boolean(string='Active', default=True)