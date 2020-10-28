from django.db import models
from django.contrib.auth.models import BaseUserManager
from d_accounts_app.models import User

import datetime

# Create your models here.
# --------------------------------------------------Arias

class Country(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name

class State(models.Model):
    """
    Clase usada para gestionar la informacion de un departamento de un pais
    - - - - -
    Attributes
    - - - - -
    name : string[50]
        Nombre del departamento
    country : int
        Referencia a un pais
    """
    name = models.CharField(max_length=30, blank=False, null=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=False, null=True)
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
    
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
    
    def __str__(self):
        return self.name

class Institution(models.Model):
    name_inst = models.CharField(max_length=30, blank=False, null=False)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'
    
    def __str__(self):
        return self.name_inst

class Professor(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, blank=False, null=True)
    is_director_student = models.BooleanField(default=False)
    is_director_gi = models.BooleanField(default=False)
    is_internal = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
    
    def __str__(self):
        return self.user

class Faculty(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        verbose_name = 'Departamento de la universidad'
        verbose_name_plural = 'Departamentos de la universidad'
    
    def __str__(self):
        return self.name

# class FormacionAcademica(models.Model):
#     id = models.AutoField(primary_key=True)
#     titulo = models.CharField(max_length=30, blank=False, null=False)
#     institucion = models.CharField(max_length=30, blank=False, null=False)
#     fecha = models.DateField()

#     class Meta:
#         verbose_name = 'FormacionAcademica'
#         verbose_name_plural = 'FormacionesAcademicas'
    
#     def __str__(self):
#         return self.nombre

# Create your models here.
# -------------------------------------------Jeison

# modelos
class InvestigationGroup(models.Model):
    """
    Clase usada para gestionar la informacion de un grupo de investigacion
    - - - - -
    Attributes
    - - - - -
    departamentU : int
        Referencia a un departamento de la universidad
    name : string[50]
        Nombre del grupo de investigacion
    category : string[50]
        Categoria del grupo de investigacion
    email : string
        Email del grupo de investigacion
    foundation_date : date
        Fecha de fundacion del grupo de investigacion
    """
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    email = models.EmailField()
    foundation_date = models.DateField()

    class Meta:
        verbose_name = 'Grupo de investigación'
        verbose_name_plural = 'Grupos de investigación'

    def __str__(self):
        return self.name

class KnowledgeArea(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Area del conocimiento'
        verbose_name_plural = 'Areas del conocimiento'

    def __str__(self):
        return self.name

class InvestigationLine(models.Model):
    know_area = models.ForeignKey(KnowledgeArea, on_delete=models.SET_NULL, blank=False, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Linea de investigación'
        verbose_name_plural = 'Lineas de investigación'

    def __str__(self):
        return self.name

class WorksInvestGroup(models.Model):
    inv_group = models.ForeignKey(InvestigationGroup, on_delete=models.SET_NULL, blank=False, null=True)
    know_area = models.ForeignKey(KnowledgeArea, on_delete=models.SET_NULL, blank=False, null=True)
    study_status = models.BooleanField()

    class Meta:
        verbose_name = 'Trabaja'
        verbose_name_plural = 'Trabaja'

class ManageInvestLine(models.Model):
    inv_line = models.ForeignKey(InvestigationLine, on_delete=models.SET_NULL, blank=False, null=True, default=1)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=False, null=True, default=1)
    analysis_state = models.BooleanField()

    class Meta:
        verbose_name = 'Maneja'
        verbose_name_plural = 'Maneja'

class ManageInvestGroup(models.Model):
    inv_group = models.ForeignKey(InvestigationGroup, on_delete=models.SET_NULL, blank=False, null=True, default=1)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=False, null=True, default=1)
    direction_state = models.BooleanField()
    
    class Meta:
        verbose_name = 'Dirige'
        verbose_name_plural = 'Dirige'

class IsMember(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=False, null=True)
    inv_group = models.ForeignKey(InvestigationGroup, on_delete=models.SET_NULL, blank=False, null=True)
    membershio_status = models.BooleanField()

    class Meta:
        verbose_name = 'Es Miembro'
        verbose_name_plural = 'Son Miembros'

class WorksDepartm(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=False, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True)
    laboral_category = models.CharField(max_length=50, blank=False, null=False)
    laboral_state = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Labora'
        verbose_name_plural = 'Labora'



