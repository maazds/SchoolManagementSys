# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class TeacherManagement(models.Model):
    _name = 'teacher.management'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Management of Teachers'
    _rec_name = 'TeacherFirstName'

    TeacherID = fields.Char('Teacher ID', required=True)
    TeacherTitle = fields.Selection([('0','Mr'),('1','Sir'),('2','Dr'),('3','Mrs'),('4','Ms'),('5','Miss')],'Title',required=True)
    TeacherFirstName = fields.Char('First Name', required=True)
    TeacherLastName = fields.Char('Last Name', required=True)
    TeacherDateOfBirth = fields.Date('Date of Birth',required=True,default='1998-05-02')
    TeacherAge = fields.Char(string="Age")
    # TeacherAge1 = fields.Char(string="Age", compute='onchange_age')
    TeacherGender = fields.Selection([('0','Male'),('1','Female'),('2','Others')],'Gender',required=True)
    TeacherCountry = fields.Char('Country',required=True)
    TeacherState = fields.Char('State')
    TeacherCity = fields.Char('City')
    # TeacherZipCode = fields.Integer('Zip Code')
    TeacherZipCode = fields.Char('Zip Code')
    TeacherStreetAddress = fields.Char('Street Address',required=True)
    TeacherPhoneNumber = fields.Char('Phone Number',tracking=True)
    TeacherEmail = fields.Char('Email')
    TeacherImage = fields.Binary('Image')
    TeacherLecture = fields.Many2many('room.management',string="Lecture")



    @api.onchange('TeacherDateOfBirth')
    def onchange_age(self):
        dob = int(self.TeacherDateOfBirth.strftime('%Y'))
        present_date = datetime.today()
        year = present_date.strftime('%Y')
        self.TeacherAge = int(year) - dob
