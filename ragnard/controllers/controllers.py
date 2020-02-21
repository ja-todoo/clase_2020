# -*- coding: utf-8 -*-
# from odoo import http


# class Ragnard(http.Controller):
#     @http.route('/ragnard/ragnard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ragnard/ragnard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ragnard.listing', {
#             'root': '/ragnard/ragnard',
#             'objects': http.request.env['ragnard.ragnard'].search([]),
#         })

#     @http.route('/ragnard/ragnard/objects/<model("ragnard.ragnard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ragnard.object', {
#             'object': obj
#         })
