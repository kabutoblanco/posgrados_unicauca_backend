from django.db import models
from a_students_app.models import Student, Program
from d_information_management_app.models import Institution, InvestigationLine, Professor
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

    title = models.CharField(max_length=60, blank=True)
    name = models.CharField(max_length=60, blank=True)
    description = models.CharField(max_length=148, blank=False, null=False)
    receipt = models.FileField(upload_to="b_activities_app/archivos", blank=False, null=False)
    state = models.IntegerField(choices=STATE_CHOICES, default=1) 
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    academic_year = models.CharField(max_length=10, blank=False, null=False)
    type = models.CharField(max_length=40, blank=False, null=False)

    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=False)
    date_update = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Actividad'
        verbose_name_plural='Actividades'

    def __str__(self):
        return self.name

# Ponencias en congresos, simposios y/o jornadas
class Presentation(models.Model):
    place = models.CharField(max_length=40, blank=False, null=False)

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=False, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=False)
    date_update = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Ponencia en congreso / Simposio / Jornada'
        verbose_name_plural='Ponencias en congresos / Simposios / Jornadas'

# Publicación
class Publication(models.Model):
    type = models.CharField(max_length=20, blank=False, null=False)
    authors = models.CharField(max_length=80, blank=False, null=False)
    general_data = models.CharField(max_length=148, blank=False, null=False)
    editorial = models.CharField(max_length=100, blank=False, null=False)

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=False)
    date_update = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Publicación'
        verbose_name_plural='Publicaciones'

# Curso / Direccion de proyectos / Revision de proyectos
class ProjectCourse(models.Model):
    assigned_hours = models.PositiveIntegerField(blank=False, null=False)

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=False, null=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=False)
    date_update = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Curso / Direccion de proyectos / Revision de proyectos'
        verbose_name_plural='Cursos / Direcciones de proyectos / Revisiones de proyectos'

# Estancia de investigación en otras instituciones
class ResearchStays(models.Model):
    purpose = models.CharField(max_length=100, blank=False, null=False)
    responsible = models.CharField(max_length=20, blank=False, null=False)

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=False, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=False)
    date_update = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Estancia de investigación en otras instituciones'
        verbose_name_plural='Estancias de investigación en otras instituciones'

# Exposición de resultados parciales de investigación
class PresentationResults(models.Model):
    modality = models.CharField(max_length=40, blank=False, null=False)
    duration = models.CharField(max_length=20, blank=False, null=False)
    place = models.CharField(max_length=40, blank=False, null=False)

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=False)
    date_update = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Exposición de resultados parciales de investigación'
        verbose_name_plural='Exposiciónes de resultados parciales de investigación'

# Participación en proyecto de investigación
class ParticipationProjects(models.Model):
    place = models.CharField(max_length=40, blank=False, null=False)
    code_VRI = models.IntegerField(blank=False, null=False)
    convocation = models.CharField(max_length=40, blank=False, null=False)
    typo_convocation = models.CharField(max_length=100, blank=False, null=False)

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=False, null=True)
    investigation_line =  models.ForeignKey(InvestigationLine, on_delete=models.SET_NULL, blank=False, null=True)
    investigator = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=False)
    date_update = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Participación en proyecto de investigación'
        verbose_name_plural='Participaciónes en proyectos de investigación'

class Prize(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=False, null=True)

    date_record = models.DateTimeField(auto_now=False)
    date_update = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Premio'
        verbose_name_plural='Premios'

    def __str__(self):
        return self.name