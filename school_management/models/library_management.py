from odoo import api,models,fields

class LibraryManagement(models.Model):
    _name = 'library.management'
    _description = 'Library Management'
    _rec_name = 'book_id'

    book_id = fields.Char('Book ID')
    book_name = fields.Char('Book Name')
    book_author = fields.Char('Author Name')
    book_release_date = fields.Date('Release Date')
    book_edition = fields.Integer('Book Edition')



