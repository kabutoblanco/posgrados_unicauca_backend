from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from d_accounts_app.models import User

def send_email(student, professor):

    first_name = professor.user.first_name
    last_name = professor.user.last_name

    first_name_student = student.first_name
    last_name_student = student.last_name
    code_student = student.personal_code

    email_professor = professor.user.email
    email_student = student.email

    body = render_to_string('newActivity.html',
        {'first_name': first_name, 'last_name': last_name, 'first_name_student': first_name_student, 'last_name_student': last_name_student, 'code_student': code_student},)
    email_message = EmailMessage(
        subject='Actividad registrada',
        body=body,
        from_email=settings.EMAIL_HOST_USER,
        to=[email_professor],
    )
    email_message.content_subtype = 'html'
    email_message.send() 