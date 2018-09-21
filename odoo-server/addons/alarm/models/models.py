# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class alarm(models.Model):
#     _name = 'alarm.alarm'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class alarm_flag(models.Model):
    _name =  "alarm.flag"

    #********************* Base Fields ******************
    name = fields.Char(string="Alarm Name")
    start_date = fields.Datetime(string="Alarm Start Date")
    end_date = fields.Datetime(string="Alarm Expiring Date")
    status = fields.Char(string="Status", help="State of the Alarm ,ie. Action pending or done")