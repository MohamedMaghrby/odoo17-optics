from odoo import models, fields


class PartnerPriceListAssociation(models.Model):
    """
    Model to mage the relationship between partners and price lists,
    """

    _name = 'partner.pricelist.association'
    _description = """
    Handles the relation between partners and product pricelists.
    """
    name = fields.Char(required=True)
    description = fields.Char()
    partner_ids = fields.One2many('res.partner', inverse_name='category_pricelist_id')
    pricelist_id = fields.Many2one('product.pricelist')
