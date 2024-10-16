# -*- coding: utf-8 -*-
# from odoo import http


# class PersianCalendar(http.Controller):
#     @http.route('/persian_calendar/persian_calendar', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/persian_calendar/persian_calendar/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('persian_calendar.listing', {
#             'root': '/persian_calendar/persian_calendar',
#             'objects': http.request.env['persian_calendar.persian_calendar'].search([]),
#         })

#     @http.route('/persian_calendar/persian_calendar/objects/<model("persian_calendar.persian_calendar"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('persian_calendar.object', {
#             'object': obj
#         })

