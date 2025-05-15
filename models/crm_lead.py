from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    location = fields.Char(string="Location")