from odoo import models,fields


class LibraryBooksWizard(models.TransientModel):
    _name = 'library.book.wizard'
    _description = 'Library Books Wizard'

    student_id = fields.Many2one('student.management',string="Student ID")
    books_ids = fields.Many2many('library.management',string="Books ID's")
    issue_date = fields.Date('Issue Date',default=fields.Date.today())
    to_date = fields.Date('Return Date')

    def add_book_rents(self):
        rentModel = self.env['library.book.management']
        for wiz in self:
            for book in wiz.books_ids:
                rentModel.create({
                    'borrower_id': wiz.student_id.id,
                    'book_id': book.id,
                    'rent_date': wiz.issue_date,
                    'return_date':wiz.to_date
                })

