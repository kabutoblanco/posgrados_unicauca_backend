from django.db import models
from a_students_app.models import Student, Program
from d_information_management_app.models import Institution, InvestigationLine, Professor, City, Country
from django.utils.translation import ugettext_lazy as _

class Activity(models.Model):
    """
    Clase usada para registrar las actividades de investigacion de los estudiantes durante su posgrado
    - - - - -
    Attributes
    - - - - -
    title : str(60) (opcional)
        Titulo de la actividad que realiza el estudiante 
    name : str(60) (opcional)
        Nombre de la actividad que realiza el estudiante
    description : str(148)
        Descripcion de la actividad que realiza el estudiante
    receipt : file
        Justifiante de la actividad, archivo almacenado de tipo .pdf
    state : int
        Controla el estado actual de la actividad
    start_date : date
        Fecha en la que se da inicio, se realiza o se envia la actividad
    end_date : date (opcional)
        Fecha en la que se da por terminada o se publica la actividad
    academic_year : str
        Año academico en el que se registra la actividad
    type : str
        Tipo de actividad que se registra
    student : int
        Referencia a un studiante
    date_record : datetime
        Fecha de registro
    date_update : datetime
        Fecha de último cambio realizado
    is_active : boolean
        Indica si el registro esta activo
    - - - - -
    Methods
    - - - - -
    """
    STATE_CHOICES = (
        (1, _("REGISTRADO")),
        (2, _("EN_REVISION")),
        (3, _("REVISADA")),
        (4, _("ACEPTADA")),
    )
    TYPE_CHOICES = (
        (1, _("Curso, dirección/revisión de proyecto")),
        (2, _("Ponencia en congresos, simposios y/o jornadas")),
        (3, _("Publicación")),
        (4, _("Exposición de resultados parciales de investigación")),
        (5, _("Estancia de investigación en otra institucion")),
        (6, _("Participación en proyecto de investigación")),
    )
    title = models.CharField(max_length=60, blank=True)
    name = models.CharField(max_length=60, blank=True)
    description = models.CharField(max_length=148, blank=True, null=False)
    receipt = models.FileField(upload_to="b_activities_app/archivos", blank=True, null=False)
    state = models.IntegerField(choices=STATE_CHOICES, default=1) 
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=True, null=True)
    academic_year = models.CharField(max_length=10, blank=False, null=False)
    type = models.IntegerField(choices=TYPE_CHOICES, default=1) 

    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=False)
    date_update = models.DateTimeField(auto_now=False) 
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Actividad'
        verbose_name_plural='Actividades'

    def __str__(self):
        return str(self.id)

class Lecture(Activity):
    """
    Clase usada para registrar las actividades de tipo Ponencias en congresos, simposios y/o jornadas
    Attributes
    - - - - -
    place: str
        Lugar donde se realiza la actividad
    institution : int
        Referencia a una institucion donde se realiza la actividad
    - - - - -
    Methods
    - - - - -
    """
    place = models.CharField(max_length=40, blank=False, null=False)

    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        verbose_name='Ponencia en congreso / Simposio / Jornada'
        verbose_name_plural='Ponencias en congresos / Simposios / Jornadas'

class Publication(Activity):
    """
    Clase usada para registrar las actividades de tipo Publicación
    Attributes
    - - - - -
    type_publication: str
        tipo de la publicacion que se realiza
    authors: str
        autores de la publicacion
    general_data : str
        Datos generales de la publicacion
    editorial : str
        Editorial de la publicacion
    - - - - -
    Methods
    - - - - -
    """
    type_publication = models.CharField(max_length=20, blank=False, null=False)
    authors = models.CharField(max_length=80, blank=False, null=False)
    general_data = models.CharField(max_length=148, blank=False, null=False)
    editorial = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name='Publicación'
        verbose_name_plural='Publicaciones'

class ProjectCourse(Activity):
    """
    Clase usada para registrar las actividades de tipo Curso / Direccion de proyectos / Revision de proyectos
    Attributes
    - - - - -
    assigned_hours: int
        horas que duro la actividad
    program : int
        Referencia a un programa
    - - - - -
    Methods
    - - - - -
    """
    assigned_hours = models.PositiveIntegerField(blank=False, null=False)

    program = models.ForeignKey(Program, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        verbose_name='Curso / Direccion de proyectos / Revision de proyectos'
        verbose_name_plural='Cursos / Direcciones de proyectos / Revisiones de proyectos'

class ResearchStays(Activity):
    """
    Clase usada para registrar las actividades de tipo Estancia de investigación en otras instituciones
    Attributes
    - - - - -
    purpose: str
        Proposito de la actividad
    responsible : str
        Responsable de realizar la actividad
    institution : int
        Referencia a una institucion donde se realizo la actividad
    city : int
        Referencia a la ciudad donde se realizo la actividad
    country : int
        Referencia al pais donde se realiza la actividad
    - - - - -
    Methods
    - - - - -
    """
    purpose = models.CharField(max_length=100, blank=False, null=False)
    responsible = models.CharField(max_length=60, blank=False, null=False)

    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, blank=False, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=False, null=True)
    #country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        verbose_name='Estancia de investigación en otras instituciones'
        verbose_name_plural='Estancias de investigación en otras instituciones'

class PresentationResults(Activity):
    """
    Clase usada para registrar las actividades de tipo Exposición de resultados parciales de investigación
    Attributes
    - - - - -
    modality: str
        Modalidad de la actividad
    duration_hours : int
        Numero de horas que duro la actividad
    place : str
        Referencia a una institucion donde se realizo la actividad
    - - - - -
    Methods
    - - - - -
    """
    modality = models.CharField(max_length=40, blank=False, null=False)
    duration_hours = models.PositiveIntegerField(blank=False, null=False)
    place = models.CharField(max_length=40, blank=False, null=False)

    class Meta:
        verbose_name='Exposición de resultados parciales de investigación'
        verbose_name_plural='Exposiciónes de resultados parciales de investigación'

class ParticipationProjects(Activity):
    """
    Clase usada para registrar las actividades de tipo Participación en proyecto de investigación
    Attributes
    - - - - -
    place : str
        Referencia al lugar donde se realizo la actividad
    code_VRI: int
        codigo VRI asignado al projecto
    convocation : str
        Descripcion de la convocacion
    type_convocation : str
        Tipo de convocacion (externa o interna)
    investigation_line : int
        Referencia a la linea de investigacion que correponde al proyecto
    investigator : int
        Referencia al profesor que actua como investigador en el proyecto
    - - - - -
    Methods
    - - - - -
    """
    place = models.CharField(max_length=40, blank=False, null=False)
    code_VRI = models.IntegerField(blank=False, null=False)
    convocation = models.CharField(max_length=148, blank=False, null=False)
    type_convocation = models.CharField(max_length=20, blank=False, null=False)

    investigation_line =  models.ForeignKey(InvestigationLine, on_delete=models.SET_NULL, blank=False, null=True)
    investigator = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        verbose_name='Participación en proyecto de investigación'
        verbose_name_plural='Participaciónes en proyectos de investigación'

class Prize(models.Model):
    """
    Clase usada para registrar las actividades de tipo Participación en proyecto de investigación
    Attributes
    - - - - -
    name : str
        Nombre del premio
    activity : int
        Referencia a la actividad que gano el premio
    date_record : datetime
        Fecha de registro
    date_update : datetime
        Fecha de último cambio realizado
    is_active : boolean
        Indica si el registro esta activo
    - - - - -
    Methods
    - - - - -
    """
    name = models.CharField(max_length=40, blank=False, null=False)

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=False)
    date_update = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Premio'
        verbose_name_plural='Premios'

    def __str__(self):
        return self.id + " " + self.name