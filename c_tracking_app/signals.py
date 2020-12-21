from django.contrib.auth.models import AbstractUser, BaseUserManager

from rest_framework import status

from a_students_app.models import Enrrollment
from d_information_management_app.models import Professor, CoordinatorProgram

from .email import send_email_to_coordinator, send_email_to_student
from .models import *
from util.exception import CustomException


def save_or_send_testdirector(sender, instance, created, **kwargs):
    try:
        if not instance.is_save:
            # save activity to coordinator
            program = instance.activity.student.program            
            coordinator = CoordinatorProgram.objects.filter(program=program).order_by('-academic_period')[0]
            professor = Professor.objects.get(id=coordinator.professor.id)
            professor_activity = ActivityProfessor(activity=instance.activity, professor=professor, rol=3)
            professor_activity.save()
            # change status activity
            activity = instance.activity
            activity.state = 3
            activity.save()
            # send email to coordinator
            send_email_to_coordinator(professor, instance.activity.student, instance)
        else:
            # change status activity
            activity = instance.activity
            activity.state = 2
            activity.save()
    except:
        if created:
            raise CustomException('No se pudo asignar actividad al coordinador', 'detail', status.HTTP_204_NO_CONTENT)
        raise CustomException('No se pudo notificar al coordinador', 'detail', status.HTTP_204_NO_CONTENT)


def save_or_send_testcoordinator(sender, instance, created, **kwargs):
    try:
        if not instance.is_save:
            # get director
            director = ActivityProfessor.objects.get(activity=instance.activity, rol=1).professor
            # change status activity
            activity = instance.activity
            activity.state = 4
            activity.save()
            # send email to student
            professor = instance.coordinator
            student = instance.activity.student
            send_email_to_student(professor, director, student, instance)
        else:
            # change status activity
            activity = instance.activity
            activity.state = 3
            activity.save()
    except:
        raise CustomException('No se pudo notificar al estudiante', 'detail', status.HTTP_204_NO_CONTENT)


def update_tracking(sender, instance, created, **kwargs):
    try:
        enrrollment = Enrrollment.objects.filter(student=instance.student).order_by('-period')[0]
        if instance.status == 1 and instance.enrrollment_date is not None:
            enrrollment.enrrollment_date = instance.enrrollment_date    
        enrrollment.state = instance.status
        enrrollment.save()
    except Enrrollment.DoesNotExist:
        raise CustomException('No se pudo modificar matricula', 'detail', status.HTTP_204_NO_CONTENT)    