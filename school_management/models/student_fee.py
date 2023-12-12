from odoo import api,models,fields

class StudentFee(models.Model):
    _name = 'student.fee'
    _description = 'Student Fee Details'

    course = fields.Many2one('subject.management',string="Course")
    name = fields.Char('Name')