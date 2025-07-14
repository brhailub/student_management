from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student Information'
    _inherit = 'person.person'
    _order = 'name asc'

    # Student-specific fields
    grade = fields.Char(string='Grade', required=True)
    section = fields.Char(string='Section')
    mark = fields.Float(string='Mark', digits=(3, 2))
    teacher_id = fields.Many2one('hr.employee', string='Teacher', domain=[('is_teacher', '=', True)])
    registration_year = fields.Char(string='Registration Year', default=lambda self: str(fields.Date.today().year), readonly=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)

    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for student in self:
            if student.birth_date:
                delta = today - student.birth_date
                student.age = delta.days // 365
            else:
                student.age = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'id_no' not in vals or not vals['id_no']:
                seq = self.env['ir.sequence'].next_by_code('student.id.sequence')
                vals['id_no'] = f"STU/{vals.get('registration_year', str(fields.Date.today().year))}/{seq.zfill(5)}"
        return super().create(vals_list)

    @api.constrains('mark')
    def _check_mark(self):
        for student in self:
            if student.mark < 0 or student.mark > 100:
                raise ValidationError("Mark must be between 0 and 100!")