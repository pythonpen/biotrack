# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class amc_cmc_warranty(models.Model):
#     _name = 'amc_cmc_warranty.amc_cmc_warranty'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class amc_cmc(models.Model):
    _name = "amc.cmc"
    #***********Base Fields*******************
    name = fields.Char(string='Document Name')
    company_name = fields.Char(string="Company Name")
    street = fields.Char(placeholder="Address line 1", string="Address")
    street2 = fields.Char(placeholder="Address line 2")
    city = fields.Char(string="City")
    state_id = fields.Many2one('res.country.state', string='State', track_visibility='onchange', index=True,)
    phone = fields.Char(string="Phone")
    mail = fields.Char(string="E-mail")
    equipment_id = fields.Many2one('maintenance.equipment', string='Equipment', track_visibility='onchange',index=True,)
    start_date = fields.Datetime(string='Contract Start Date')
    end_date = fields.Datetime(string='Contract Expiring Date')
    contract = fields.Char(string='Contract Amount', help='Cost of the contract')
