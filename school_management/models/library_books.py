from odoo import api, models, fields

class LibraryBooks(models.Model):
    _name = 'library.book.management'
    _description = 'Library Books Management'

    book_id = fields.Many2one('library.management',string="Book ID")
    borrower_id = fields.Many2one('student.management',string="Borrower ID")
    rent_date = fields.Date('Starting Date',default=fields.Date.today())
    return_date = fields.Date('Return Date')
