# -*- coding: utf-8 -*-
from odoo import http

# class Menu(http.Controller):
#     @http.route('/menu/menu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/menu/menu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('menu.listing', {
#             'root': '/menu/menu',
#             'objects': http.request.env['menu.menu'].search([]),
#         })

#     @http.route('/menu/menu/objects/<model("menu.menu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('menu.object', {
#             'object': obj
#         })