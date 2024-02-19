from odoo import api, models, fields

class CourseManagement(models.Model):
    _name = 'course.management'
    _description = 'Course Management'
    _rec_name = 'CourseID'

    CourseID = fields.Char('Course ID',required=True)
    CourseName = fields.Char('Course Name',required=True)
    CourseDesc = fields.Char('Description')