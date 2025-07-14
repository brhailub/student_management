from odoo import models, fields, api
from odoo.exceptions import UserError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    is_teacher = fields.Boolean(string='Is Teacher')
    students_ids = fields.One2many(
        'student.student', 
        'teacher_id', 
        string='Students',
        domain=lambda self: [('teacher_id', '=', self._origin.id)]
    )

    def show_student_count(self):
        self.ensure_one()
        if not self.is_teacher:
            raise UserError("Only teachers can have students!")
        
        student_count = self.env['student.student'].search_count([
            ('teacher_id', '=', self.id)
        ])  
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Student Count',
                'message': f'This teacher has {student_count} students',
                'sticky': False,
                'type': 'info',
            }
        }