from django.db import models
from django.contrib.auth.models import BaseUserManager
from d_accounts_app.models import User

import datetime

# Create your models here.
# --------------------------------------------------Arias

class Country(models.Model):
    """
    Clase usada para gestionar la informacion de un pais
    - - - - -
    Attributes
    - - - - -
    name : string[30]
        Nombre del pais
    """
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
    name : string[30]
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
    """
    Clase usada para gestionar la informacion de una ciudad
    - - - - -
    Attributes
    - - - - -
    name : string[30]
        Nombre de la ciudad
    state : int
        Referencia a un departamento de un pais
    """
    name = models.CharField(max_length=30, blank=False, null=False)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
    
    def __str__(self):
        return self.name

class Institution(models.Model):
    """
    Clase usada para gestionar la informacion de una institucion
    - - - - -
    Attributes
    - - - - -
    name : string[30]
        Nombre de la institucion
    city : int
        Referencia a una ciudad en la cual se encuentra la institucion
    """
    name_inst = models.CharField(max_length=30, blank=False, null=False)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'
    
    def __str__(self):
        return self.name_inst

class Professor(models.Model):
    """
    Clase usada para gestionar la informacion de un profesor
    - - - - -
    Attributes
    - - - - -
    user : int
        Referencia a un usuario del sistema
    institution : int
        Referencia a una institucion registrada
    is_director_student : boolean
        Estado de la relacion en la cual el profesor es director o no de un estudiante
    is_director_gi : boolean
        Estado de la relacion en la cual el profesor es director o no de un grupo de investigacion
    is_internal : boolean
        Estado de la relacion en la cual el profesor es interno o no en la universidad
    """
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
    """
    Clase usada para gestionar la informacion de una facultad
    - - - - -
    Attributes
    - - - - -
    name : string[30]
        Nombre del departamento
    institution : int
        Referencia a una institucion registrada
    """
    name = models.CharField(max_length=30, blank=False, null=False)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'
    
    def __str__(self):
        return self.name

class Department(models.Model):
    """
    Clase usada para gestionar la informacion de un departamento de una universidad
    - - - - -
    Attributes
    - - - - -
    name : string[30]
        Nombre del departamento de la universidad
    faculty : int
        Referencia a una facultad de una universidad
    """
    name = models.CharField(max_length=30, blank=False, null=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        verbose_name = 'Departamento de la universidad'
        verbose_name_plural = 'Departamentos de la universidad'
    
    def __str__(self):
        return self.name

class AcademicTraining(models.Model):
    """
    Clase usada para gestionar la informacion de la formacion academica de un profesor
    - - - - -
    Attributes
    - - - - -
    professor : int
        Referencia a un profesor registrado
    degree : string[30]
        Nombre del titulo que tiene actualmente el profesor
    institution : int
        Referencia a una institucion registrada
    date : date
        Fecha en la cual obtuvo el titutlo
    """
    professor =  models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=False, null=True)
    degree = models.CharField(max_length=30, blank=False, null=False)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, blank=False, null=True)
    date = models.DateField()

    class Meta:
        verbose_name = 'Formacion Academica'
        verbose_name_plural = 'Formaciones Academicas'
    
    def __str__(self):
        return self.degree


# Create your models here.
# --------------------------------------------------Arias

# modelos
class InvestigationGroup(models.Model):
    """
    Clase usada para gestionar la informacion de un grupo de investigacion
    - - - - -
    Attributes
    - - - - -
    departament : int
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
    """
    Clase usada para gestionar la informacion de un area del conocimiento
    - - - - -
    Attributes
    - - - - -
    name : string[50]
        Nombre del grupo del area de conocimiento
    description : string[500]
        Espacio para una descripcion del area de conocimiento
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Area del conocimiento'
        verbose_name_plural = 'Areas del conocimiento'

    def __str__(self):
        return self.name

class InvestigationLine(models.Model):
    """
    Clase usada para gestionar la informacion de una linea de investigacion
    - - - - -
    Attributes
    - - - - -
    know_area : int
        Referencia a un area del conocimiento a la cual esta asociada la linea de investigacion
    name : string[50]
        Nombre de la linea de investigacion
    description : string[500]
        Espacio para una descripcion del area de conocimiento
    """
    know_area = models.ForeignKey(KnowledgeArea, on_delete=models.SET_NULL, blank=False, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Linea de investigación'
        verbose_name_plural = 'Lineas de investigación'

    def __str__(self):
        return self.name

class WorksInvestGroup(models.Model):
    """
    Clase usada para tener el registro de la relacion entre grupo de investigacion y el area del conocimiento
    en la cual se encuentra trabajando (puede ser 1 o varios registros)
    - - - - -
    Attributes
    - - - - -
    inv_group : int
        Referencia a un grupo de investigacion
    know_area : int
        Referencia a un area del conocimiento
    study_status : boolean
        Estado de la relacion en  la cual un grupo de investigacion trabaja o no en un area del conocimiento
    """
    inv_group = models.ForeignKey(InvestigationGroup, on_delete=models.SET_NULL, blank=False, null=True)
    know_area = models.ForeignKey(KnowledgeArea, on_delete=models.SET_NULL, blank=False, null=True)
    study_status = models.BooleanField()

    class Meta:
        verbose_name = 'Trabaja'
        verbose_name_plural = 'Trabaja'

class ManageInvestLine(models.Model):
    """
    Clase usada para tener el registro de la relacion entre profesor y la linea de investigacion que el profesor
    se encuentra o no manejando (puede ser 1 o varios registros)
    - - - - -
    Attributes
    - - - - -
    inv_line : int
        Referencia a una linea de investigacion
    profesor : int
        Referencia a un profesor
    analysis_state : boolean
        Estado de la relacionen en la cual el profesor maneja o no una linea de investigacion
    """
    inv_line = models.ForeignKey(InvestigationLine, on_delete=models.SET_NULL, blank=False, null=True, default=1)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=False, null=True, default=1)
    analysis_state = models.BooleanField()

    class Meta:
        verbose_name = 'Maneja'
        verbose_name_plural = 'Maneja'

class ManageInvestGroup(models.Model):
    """
    Clase usada para tener el registro de la relacion entre un profesor y el grupo de investigacion que el profesor
    se encuentra o no dirigiendo (puede ser 1 o varios registros)
    - - - - -
    Attributes
    - - - - -
    inv_group : int
        Referencia a un grupo de investigacion
    professor : int
        Referencia a un profesor
    direction_state : boolean
        Estado de la relacion en la cual el profesor dirige o no un grupo de investigacion
    """
    inv_group = models.ForeignKey(InvestigationGroup, on_delete=models.SET_NULL, blank=False, null=True, default=1)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=False, null=True, default=1)
    direction_state = models.BooleanField()
    
    class Meta:
        verbose_name = 'Dirige'
        verbose_name_plural = 'Dirige'

class IsMember(models.Model):
    """
    Clase usada para tener el registro de la relacion entre un profesor y un grupo de investigacion del cual puede o no
    ser miembro el profesor (puede ser 1 o varios registros)
    - - - - -
    Attributes
    - - - - -
    professor : int
        Referencia a un profesor
    inv_group : int
        Referencia a un grupo de investigacion
    membershio_status : boolean
        Estado de la relacion en la cual el profesor es miembro o no de un grupo de investigacion
    """
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=False, null=True)
    inv_group = models.ForeignKey(InvestigationGroup, on_delete=models.SET_NULL, blank=False, null=True)
    membershio_status = models.BooleanField()

    class Meta:
        verbose_name = 'Es Miembro'
        verbose_name_plural = 'Son Miembros'

class WorksDepartm(models.Model):
    """
    Clase usada para tener el registro de la relacion entre un profesor y un departamento de la universidad en el cual
    puede o no laborar el profesor (puede ser 1 o varios registros)
    - - - - -
    Attributes
    - - - - -
    professor : int
        Referencia a un profesor
    department : int
        Referencia a un departamento de la universidad
    laboral_category : string[50]
        Tipo de categoria laboral en la que se encuentra el profeosor dentro de la universidad 
        (es escrita por el usuario, no hay categorias predefinidas)
    laboral_state : boolean
        Estado de la relacion en la cual el profesor es labora o no de un departamento de la universidad
    """
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=False, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True)
    laboral_category = models.CharField(max_length=50, blank=False, null=False)
    laboral_state = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Labora'
        verbose_name_plural = 'Labora'



