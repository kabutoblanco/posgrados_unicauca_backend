from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from d_accounts_app.models import User

def send_email(professor, test_director):

    first_name = professor.user.first_name
    last_name = professor.user.last_name
    full_name = "{} {}".format(first_name, last_name)

    first_name_director = test_director.director.user.first_name
    last_name_director = test_director.director.user.last_name
    full_name_director = "{} {}".format(first_name_director, last_name_director)

    id = test_director.activity.pk
    title = test_director.activity.title

    email_professor = professor.user.email

    body = render_to_string('newActivityCoordinator.html',
        {'full_name': full_name, 'full_name_director': full_name_director, 'id': id, 'title': title},)
    email_message = EmailMessage(
        subject='Nueva actividad asignada para calificar',
        body=body,
        from_email=settings.EMAIL_HOST_USER,
        to=[email_professor],
    )
    email_message.content_subtype = 'html'
    email_message.send() 


def send_email1(professor, student, test_coordinator):

    first_name = student.user.first_name
    last_name = student.user.last_name
    full_name = "{} {}".format(first_name, last_name)

    first_name_coordinator = professor.user.first_name
    last_name_coordinator = professor.user.last_name
    full_name_coordinator = "{} {}".format(first_name_coordinator, last_name_coordinator)

    id = test_coordinator.activity.pk
    title = test_coordinator.activity.title

    email_student = student.user.email

    body = render_to_string('activityFull.html',
        {'full_name': full_name, 'full_name_coordinator': full_name_coordinator, 'id': id, 'title': title},)
    email_message = EmailMessage(
        subject='Actividad calificada',
        body=body,
        from_email=settings.EMAIL_HOST_USER,
        to=[email_student],
    )
    email_message.content_subtype = 'html'
    email_message.send() 