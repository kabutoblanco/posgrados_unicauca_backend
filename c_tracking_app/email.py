from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from d_accounts_app.models import User


def send_email_to_coordinator(professor, student, test_director):
    first_name = professor.user.first_name
    last_name = professor.user.last_name
    full_name = "{} {}".format(first_name, last_name)

    first_name = student.user.first_name
    last_name = student.user.last_name
    full_name_student = "{} {}".format(first_name, last_name)

    first_name = test_director.director.user.first_name
    last_name = test_director.director.user.last_name
    full_name_director = "{} {}".format(first_name, last_name)

    id = test_director.activity.pk
    title = test_director.activity.title

    parameters_1 = {
        'full_name': full_name,
        'full_name_director': full_name_director,
        'id': id,
        'title': title
    }

    parameters_2 = {
        'full_name': full_name,
        'full_name_student': full_name_student,
        'id': id,
        'title': title,
        'type': 'director'
    }

    email_professor = professor.user.email
    email_student = student.user.email

    body = render_to_string('NotifyCoordinatorActivity.html', parameters_1)
    email_message = EmailMessage(
        subject='Notificación asignación de actividad Sistema de Posgrados',
        body=body,
        from_email=settings.EMAIL_HOST_USER,
        to=[email_professor],
    )
    email_message.content_subtype = 'html'
    email_message.send()

    body = render_to_string('NotifyStudentActivity.html', parameters_2)
    email_message = EmailMessage(
        subject='Notificación registro calificación de actividad Sistema de Posgrados',
        body=body,
        from_email=settings.EMAIL_HOST_USER,
        to=[email_student],
    )
    email_message.content_subtype = 'html'
    email_message.send()


def send_email_to_student(professor, director, student, test_coordinator):
    first_name = student.user.first_name
    last_name = student.user.last_name
    full_name = "{} {}".format(first_name, last_name)

    first_name = professor.user.first_name
    last_name = professor.user.last_name
    full_name_coordinator = "{} {}".format(first_name, last_name)

    first_name = director.user.first_name
    last_name = director.user.last_name
    full_name_director = "{} {}".format(first_name, last_name)

    id = test_coordinator.activity.pk
    title = test_coordinator.activity.title

    parameters_1 = {
        'full_name': full_name,
        'full_name_coordinator': full_name_coordinator,
        'id': id,
        'title': title,
        'type': 'coordinator'
    }

    parameters_2 = {
        'full_name': full_name_director,
        'full_name_coordinator': full_name_coordinator,
        'id': id,
        'title': title,
    }

    email_student = student.user.email
    email_director = director.user.email

    body = render_to_string('NotifyStudentActivity.html', parameters_1)
    email_message = EmailMessage(
        subject='Notificación registro calificación de actividad Sistema de Posgrados',
        body=body,
        from_email=settings.EMAIL_HOST_USER,
        to=[email_student],
    )
    email_message.content_subtype = 'html'
    email_message.send()

    body = render_to_string('NotifyDirectorActivity.html', parameters_2)
    email_message = EmailMessage(
        subject='Notificación registro calificación de actividad Sistema de Posgrados',
        body=body,
        from_email=settings.EMAIL_HOST_USER,
        to=[email_director],
    )
    email_message.content_subtype = 'html'
    email_message.send()
