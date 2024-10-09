from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_open_matrix(self):
        self.ensure_one()
        return {
            'name': 'Matrix Input',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [[self.env.ref('matrix_module.matrix_input_view_form').id, 'form']],
            'res_model': 'matrix.input',
            'target': 'new',
        }
