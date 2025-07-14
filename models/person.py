from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class Person(models.Model):
    _name = 'person.person'
    _description = 'Person Information'
    _order = 'name asc'

    name = fields.Char(string='Full Name', required=True)
    id_no = fields.Char(string='ID Number', readonly=True, copy=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')
    birth_date = fields.Date(string='Birth Date', required=True)
    active = fields.Boolean(string='Active', default=True)

    @api.constrains('birth_date')
    def _check_birth_date(self):
        today = date.today()
        for person in self:
            if person.birth_date and person.birth_date > date.today():
                raise ValidationError("Birth date cannot be in the future!")
            if person.birth_date:
                delta = today - person.birth_date
                age = delta.days // 365
                if age < 5:
                    raise ValidationError("Person must be at least 5 years old!")