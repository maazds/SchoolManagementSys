from odoo import fields, api, models


class SubjectManagement(models.Model):
    _name = 'subject.management'
    _description = 'Subject Management'
    _rec_name = 'RecName'

    RecName = fields.Char('Subject ID')
    StudentCourse_id = fields.Many2one('course.management', 'Course ID')
    StudentYear_1 = fields.Selection([('0', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5')], 'Year')
    StudentSemester_1 = fields.Selection(
        [('0', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '7'), ('7', '8'), ('8', '9'),
         ('9', '10')], 'Semester')
    FileName = fields.Char(compute='file_name')
    StudentSubject = fields.One2many('subject.management.lines', 'SubjectLine', string=" ")

    def file_name(self):
        self.FileName = "{}-{}-{}".format(self.StudentCourse_id, self.StudentYear_1, self.StudentSemester_1)


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
    # SubjectFee = fields.Integer('Subject Fee')

    @api.onchange('SubjectCreditHour')
    def sessional(self):
        self.SubjectSessional = self.SubjectCreditHour * 2
        self.SubjectHourMarks = self.SubjectCreditHour * 18
        self.SubjectTotal = self.SubjectSessional + self.SubjectHourMarks

    # @api.onchange('SubjectCreditHour')
    # def subjfee(self):
    #     self.SubjectFee = self.SubjectCreditHour * 2000



