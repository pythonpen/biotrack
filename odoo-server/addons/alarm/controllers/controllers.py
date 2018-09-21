# -*- coding: utf-8 -*-
from odoo import http

# class Alarm(http.Controller):
#     @http.route('/alarm/alarm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alarm/alarm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alarm.listing', {
#             'root': '/alarm/alarm',
#             'objects': http.request.env['alarm.alarm'].search([]),
#         })

#     @http.route('/alarm/alarm/objects/<model("alarm.alarm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alarm.object', {
#             'object': obj
#         })