from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        self.pricelist_id = self.partner_id.category_pricelist_id.pricelist_id.id
        self._recompute_prices()
