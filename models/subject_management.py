from odoo import fields, api, models


class SubjectManagement(models.Model):
    _name = 'subject.management'
    _description = 'Subject Management'
    _rec_name = 'RecName'

    RecName = fields.Char('Subject ID',compute='update_rec_name')
    StudentCourse_id = fields.Many2one('course.management', 'Course ID')
    StudentYear_1 = fields.Selection([('0', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5')], 'Year')
    StudentSemester_1 = fields.Selection(
        [('0', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'), ('8', '9'),
         ('9', '10')], 'Semester')
    FileName = fields.Char(compute='file_name')
    StudentSubject = fields.One2many('subject.management.lines', 'SubjectLine', string=" ")
    subject_inverse = fields.Many2one('student.management','subjects')

    def file_name(self):
        self.FileName = "{}-{}-{}".format(self.StudentCourse_id, self.StudentYear_1, self.StudentSemester_1)
    def update_rec_name(self):
        course_year = dict(self._fields['StudentYear_1'].selection).get(self.StudentYear_1)
        course_sems = dict(self._fields['StudentSemester_1'].selection).get(self.StudentSemester_1)
        self.RecName = '{}-{}-{}'.format(self.StudentCourse_id.CourseID,course_year,course_sems)

class SubjectManagementLines(models.Model):
    _name = "subject.management.lines"
    _description = "SUBJECT MANAGEMENT PER SEMESTER"
    _rec_name = "SubjectCode"

    SubjectLine = fields.Many2one('subject.management', string='Subject Line')
    SubjectCode = fields.Char('Subject Code')
    SubjectName = fields.Char('Subject Name')
    SubjectCreditHour = fields.Integer('Subject Credit Hour')
    SubjectTheory = fields.Integer('Theory')
    SubjectPractical = fields.Integer('Practical')
    SubjectSessional = fields.Integer('Sessional Marks')
    SubjectHourMarks = fields.Integer('Subject Marks')
    SubjectTotal = fields.Integer('Subject Total')






    @api.onchange('SubjectCreditHour')
    def sessional(self):
        self.SubjectSessional = self.SubjectCreditHour * 2
        self.SubjectHourMarks = self.SubjectCreditHour * 18
        self.SubjectTotal = self.SubjectSessional + self.SubjectHourMarks




