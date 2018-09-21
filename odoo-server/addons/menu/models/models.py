# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class menu(models.Model):
#     _name = 'menu.menu'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class menu_drawer(models.Model):
    _name = "menu.drawer"

    @api.multi
    def action_contact_service(self):
        view_id = self.env.ref('hr.hr_kanban_view_employees').id
        return {
            'name': 'Contact Service',
            'view_type': 'kanban',
            'view_mode': 'kanban',
            'views': [(view_id, 'kanban')],
            'res_model': 'hr.employee',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

    @api.multi
    def action_search_equipment(self):
        view_id = self.env.ref('maintenance.hr_equipment_view_kanban').id
        return {
            'name': 'search equipment',
            'view_type': 'kanban',
            'view_mode': 'kanban',
            'views': [(view_id, 'kanban')],
            'res_model': 'maintenance.equipment',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
    @api.multi
    def action_add_equipment(self):
        view_id = self.env.ref('maintenance.hr_equipment_view_kanban').id
        return {
            'name': 'add_equipment',
            'view_type': 'kanban',
            'view_mode': 'kanban',
            'views': [(view_id, 'kanban')],
            'res_model': 'maintenance.equipment',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'current',
            }
    @api.multi
    def action_spare(self):
        view_id = self.env.ref('maintenance.hr_equipment_view_kanban').id
        return {
            'name': 'spare',
            'view_type': 'kanban',
            'view_mode': 'kanban',
            'views': [(view_id, 'kanban')],
            'res_model': 'maintenance.equipment',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
    @api.multi
    def action_rental(self):
        view_id = self.env.ref('maintenance.hr_equipment_view_kanban').id
        return {
            'name': 'rental',
            'view_type': 'kanban',
            'view_mode': 'kanban',
            'views': [(view_id, 'kanban')],
            'res_model': 'maintenance.equipment',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
    @api.multi
    def action_inoperative(self):
        view_id = self.env.ref('maintenance.hr_equipment_view_kanban').id
        return {
            'name': 'inoperative',
            'view_type': 'kanban',
            'view_mode': 'kanban',
            'views': [(view_id, 'kanban')],
            'res_model': 'maintenance.equipment',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
    @api.multi
    def action_warranty(self):
        view_id = self.env.ref('maintenance.hr_equipment_view_kanban').id
        return {
            'name': 'warranty',
            'view_type': 'kanban',
            'view_mode': 'kanban',
            'views': [(view_id, 'kanban')],
            'res_model': 'maintenance.equipment',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
    @api.multi
    def action_maintenance(self):
        view_id = self.env.ref('maintenance.hr_equipment_request_view_kanban').id
        return {
            'name': 'maintenance',
            'view_type': 'kanban',
            'view_mode': 'kanban',
            'views': [(view_id, 'kanban')],
            'res_model': 'maintenance.equipment',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
    @api.multi
    def action_vendor(self):
        view_id = self.env.ref('maintenance.hr_equipment_request_view_kanban').id
        return {
            'name': 'vendor',
            'view_type': 'kanban',
            'view_mode': 'kanban',
            'views': [(view_id, 'kanban')],
            'res_model': 'maintenance.equipment',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
    @api.multi
    def action_alarm(self):
        view_id = self.env.ref('maintenance.maintenance_team_kanban').id
        return {
            'name': 'alarm',
            'view_type': 'kanban',
            'view_mode': 'kanban',
            'views': [(view_id, 'kanban')],
            'res_model': 'maintenance.team',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
