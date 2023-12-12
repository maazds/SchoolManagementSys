from odoo import api, models, fields

class StudentLeaveWizard(models.TransientModel):
    _name = 'student.leave.wizard'
    _description = 'Student Leave Wizard'

    student_id = fields.Many2one('student.management',string="Student ID",readonly=True)
    date = fields.Date('Date')
    reason = fields.Text('Reason')

