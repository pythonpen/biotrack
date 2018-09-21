# -*- coding: utf-8 -*-
from odoo import http

# class AmcCmcWarranty(http.Controller):
#     @http.route('/amc_cmc_warranty/amc_cmc_warranty/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/amc_cmc_warranty/amc_cmc_warranty/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('amc_cmc_warranty.listing', {
#             'root': '/amc_cmc_warranty/amc_cmc_warranty',
#             'objects': http.request.env['amc_cmc_warranty.amc_cmc_warranty'].search([]),
#         })

#     @http.route('/amc_cmc_warranty/amc_cmc_warranty/objects/<model("amc_cmc_warranty.amc_cmc_warranty"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('amc_cmc_warranty.object', {
#             'object': obj
#         })