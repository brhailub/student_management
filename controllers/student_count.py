from odoo import http
from odoo.http import request

class StudentCountController(http.Controller):
    @http.route('/student_management/get_student_count', type='json', auth='user')
    def get_student_count(self, employee_id, **kwargs):
        student_count = request.env['student.student'].search_count([
            ('teacher_id', '=', employee_id)
        ])
        return student_count