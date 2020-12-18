from django.db import models
from a_students_app.models import Student
from d_information_management_app.models import InvestigationLine, Professor

class Project(models.Model):
    
    provisional_title = models.CharField(max_length=256, blank=False, null=False)
    objetive_topic = models.CharField(max_length=256, blank=False, null=False)
    
    

    investigation_line =  models.ForeignKey(InvestigationLine, on_delete=models.SET_NULL, blank=False, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    #todos los campos relacionados con proyecto en un json y al final los campos general capturar el json de crear proyecto sacar el json ponerlo en el json de los objetivos genereal y luego especifico.
    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'

class Objetive(models.Model):

    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Objetivo'
        verbose_name_plural='Objetivos'

class General(Objetive):

    objetive_general = models.CharField(max_length=500, blank=False, null=False)

  
    class Meta:
        verbose_name='Objetivo general'
        verbose_name_plural='Objetivos generales'

class Specific(Objetive):
    objetive_specifico = models.CharField(max_length=500, blank=False, null=False)
    #Revisar

    class Meta:
        verbose_name='Objetivo especifico'
        verbose_name_plural='Objetivos especificos' 

class DirectorControl(models.Model):

    academic_period = models.CharField(max_length=20, blank=False, null=False)

    director = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=False, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Control de director'
        verbose_name_plural='Controles de director'

class CoDirectorControl(models.Model):

    academic_period = models.CharField(max_length=20, blank=False, null=False)

    codirector = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=False, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Control de codirector'
        verbose_name_plural='Controles de codirector'
