from odoo import api, models, fields
from datetime import datetime
from odoo.exceptions import ValidationError

class StudentManagement(models.Model):
    _name = 'student.management'
    _description = 'Student Data Collection'
    _rec_name = 'StudentFirstName'

    StudentID = fields.Char('Registration NO', required=True)
    StudentTitle = fields.Selection([('0', 'Mr'), ('1', 'Sir'), ('2', 'Dr'), ('3', 'Mrs'), ('4', 'Ms'), ('5', 'Miss')],
                                    'Title', required=True)
    StudentFirstName = fields.Char('First Name', requirTeachered=True)
    StudentLastName = fields.Char('Last Name', required=True)
    StudentDateOfBirth = fields.Date('Date of Birth', required=True, default='1998-05-02')
    StudentAge = fields.Char(string="Age")
    StudentGender = fields.Selection([('0', 'Male'), ('1', 'Female'), ('2', 'Others')], 'Gender', required=True)
    StudentCountry = fields.Many2one('res.country','Country', required=True)
    StudentState = fields.Many2one("res.country.state",string='State')
    StudentCity = fields.Char(string='City')
    # TeacherZipCode = fields.Integer('Zip Code')
    StudentZipCode = fields.Char('Zip Code')
    StudentStreetAddress = fields.Char('Street Address', required=True)
    StudentPhoneNumber = fields.Char('Phone Number')
    StudentEmail = fields.Char('Email')
    StudentImage = fields.Binary('Image')
    StudentCourse_ID = fields.Many2one('course.management', string='Course')
    # StudentYear1 = fields.Many2one('subject.management.StudentYear_1',string="Year")
    StudentYear = fields.Selection([('0', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5')], 'Year')
    StudentSemester = fields.Selection(
        [('0', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'), ('8', '9'),
         ('9', '10')], 'Semester')

    UpdateRec = fields.Char('Update',compute='update_rec')

    SubjectLine_2 = fields.Many2one('subject.management', string="Subject")

    SubjectLine_id = fields.Many2many('subject.management.lines', string="Subjects",compute="update_subject_lines")
    # computed field
    StudentEnrolled = fields.Integer('Enrolled',compute='student_enrolled')
    @api.onchange('StudentCourse_ID','StudentYear','StudentSemester')
    def update_rec(self):
        course_year = dict(self._fields['StudentYear'].selection).get(self.StudentYear)
        course_sems = dict(self._fields['StudentSemester'].selection).get(self.StudentSemester)
        self.UpdateRec = '{}-{}-{}'.format(self.StudentCourse_ID.CourseID, course_year, course_sems)
    # semester enrolled

    def student_enrolled(self):
        for rec in self:
            temp = self.env['subject.management.lines'].search_count([('SubjectLine' ,'=', rec.SubjectLine_2.id)])
            rec.StudentEnrolled = temp

    def action_StudentEnrolled(self):

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'subject.management.lines',
            'view_type': 'tree,form',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': [('SubjectLine', '=', self.SubjectLine_2.id)]
        }

    def change_country(self):
        self.StudentCountry = "Pakistan"

    def change_state(self):
        self.StudentState ="Punjab"

    def sort_age(self):
        pass


    @api.onchange('StudentDateOfBirth')
    def onchange_age(self):
        dob = int(self.StudentDateOfBirth.strftime('%Y'))
        present_date = datetime.today()
        year = present_date.strftime('%Y')
        self.StudentAge = int(year) - dob

    @api.onchange('SubjectLine_2')
    def update_subject_lines(self):
        for rec in self:
            related_subject_lines = self.env['subject.management.lines'].search([('SubjectLine', '=', rec.SubjectLine_2.id)]).ids
            rec.SubjectLine_id = [(6, 0, related_subject_lines)]

    @api.onchange('StudentCourse_ID')
    def update_subject_lines(self):
        for rec in self:
            related_subject_lines = self.env['subject.management.lines'].search(
                [('SubjectLine','=',rec.UpdateRec)])
            print(related_subject_lines)
            # rec.SubjectLine_id = [(6, 0, related_subject_lines)]

    @api.constrains('StudentDateOfBirth')
    @api.onchange('StudentDateOfBirth')
    def check_dob(self):
        if self.StudentDateOfBirth > fields.Date.today():
            raise ValidationError('Date of Birth Should be in past')

    def action_validate(self):
        self.env['res.partner'].create({'name':self.StudentID,
                                        'image_1920':self.StudentImage,
                                        'email':self.StudentEmail,
                                        })


