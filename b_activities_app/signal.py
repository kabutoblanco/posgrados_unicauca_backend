from django.db.models.signals import post_save
from rest_framework import status
from util.exception import CustomException
from .models import *
from a_students_app.models import StudentProfessor
from c_tracking_app.models import ActivityProfessor

def save_or_send_activity(sender, instance, created, **kwargs):
    if instance.state == 2:
        query = StudentProfessor.objects.filter(student=instance.student.id, rol=1).order_by('-id')[0]
        query = ActivityProfessor(rol=1, activity=instance, professor=query.professor)
        query.save()

def save_or_send_activity1(sender, instance, **kwargs):
    try:
        if instance.state == 2:
            query = StudentProfessor.objects.filter(student=instance.student.id, rol=1).order_by('-id')[0]
    except:
        raise CustomException("No tiene director a cargo", "message", status_code = status.HTTP_204_NO_CONTENT)