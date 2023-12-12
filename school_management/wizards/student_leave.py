from odoo import api, models, fields

class StudentLeaveWizard(models.TransientModel):
    _name = 'student.leave.wizard'
    _description = 'Student Leave Wizard'

    student_id = fields.Many2one('student.management',string="Student ID",readonly=True)
    leave_date = fields.Date('Date')
    leave_reason = fields.Text('Reason')

