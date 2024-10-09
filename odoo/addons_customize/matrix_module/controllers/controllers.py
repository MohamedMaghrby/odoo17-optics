# -*- coding: utf-8 -*-
# from odoo import http


# class MatrixModule(http.Controller):
#     @http.route('/matrix_module/matrix_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/matrix_module/matrix_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('matrix_module.listing', {
#             'root': '/matrix_module/matrix_module',
#             'objects': http.request.env['matrix_module.matrix_module'].search([]),
#         })

#     @http.route('/matrix_module/matrix_module/objects/<model("matrix_module.matrix_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('matrix_module.object', {
#             'object': obj
#         })

