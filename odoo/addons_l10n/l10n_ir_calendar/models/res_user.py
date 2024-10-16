from odoo import _, api, fields, models
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class ResUser(models.Model):
    _inherit = "res.users"

    calendar = fields.Selection(
        [("gregorian", "Gregorian Calendar"), ("jalali", "Jalali (Persian) Calendar")],
        default="jalali",
    )

    def write(self, vals):
        res = super().write(vals)
        if 'calendar' in vals:
            request.session['calendar'] = vals['calendar']
            session_info = self.env['ir.http'].session_info()

            session_info.update(
                calendar=vals['calendar']
            )
        return res

    def create(self, vals):
        res = super().create(vals)
        if 'calendar' in vals:
            request.session['calendar'] = vals['calendar']
            session_info = self.env['ir.http'].session_info()
            session_info.update(
                calendar=vals['calendar']
            )
        return res
