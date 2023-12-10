from odoo import api,models,fields

class RoomManagement(models.Model):
    _name = 'room.management'
    _description = 'Room Management'
    _rec_name = 'RoomCourseCode'

    RoomID = fields.Char('Room ID', required=True)
    RoomDay = fields.Selection([('0','Monday'),('1','Tuesday'),('2','Wednesday'),('3','Thursday'),('4','Friday')],required=True,string="Day")
    RoomCourse = fields.Many2one('course.management',string="Course")
    RoomSemester = fields.Many2one('subject.management',string="Semester")
    RoomCourseCode = fields.Char('Course Code')
    RoomInTime = fields.Datetime('Start Time')
    RoomOutTime = fields.Datetime('End Time')