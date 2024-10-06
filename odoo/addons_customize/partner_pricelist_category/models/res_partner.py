from odoo import models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    category_pricelist_id = fields.Many2one('partner.pricelist.association')
