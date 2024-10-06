from odoo import models, fields


class PriceList(models.Model):
    _inherit = 'product.pricelist'

    category_pricelist_ids = fields.One2many('partner.pricelist.association', inverse_name='pricelist_id')
