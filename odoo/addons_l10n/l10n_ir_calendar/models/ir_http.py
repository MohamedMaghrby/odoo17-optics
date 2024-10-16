from odoo import models


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        session = super(Http, self).session_info()
        user = self.env['res.users'].search([('id', '=', session.get('uid'))])
        session['calendar'] = user.calendar
        return session
