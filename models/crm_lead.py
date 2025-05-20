from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    incident_date = fields.Date(string="Date")
    relationship = fields.Char(string="Relationship")
    id_number = fields.Char(string="ID Number")
    description = fields.Text(string="Description of Incident")