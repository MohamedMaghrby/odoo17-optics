# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = "res.users"
    calendar_type = fields.Selection([('shamsi', 'Shamsi'), ('gregorian', 'Gregorian')], string='Calendar Type')
