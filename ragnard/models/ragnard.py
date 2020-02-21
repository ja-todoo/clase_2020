# -*- coding: utf-8 -*-

from odoo import models, fields, api


 class ragnard(models.Model):
     _name = 'ragnard.ragnard'
     _description = ´'Esta clase almacena los usuarios ragnard.ragnard'

     Nombre = fields.Char()
     Cedula= fields.Integer()
     Años = fields.Float(compute="_value_pc", store=True)
     memo = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
