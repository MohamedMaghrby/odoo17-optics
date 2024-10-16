from odoo import _, api, fields, models
import logging

_logger = logging.getLogger(__name__)


class ResUser(models.Model):
    _inherit = "res.users"

    calendar = fields.Selection(
        [("gregorian", "Gregorian Calendar"), ("jalali", "Shamsi Calendar")],
        default="jalali",
    )
