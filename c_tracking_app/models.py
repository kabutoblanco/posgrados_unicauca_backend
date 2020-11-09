from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

from d_information_management_app.models import Professor
from b_activities_app.models import Activity
from a_students_app.models import Student, Enrrollment

class TestCoordinator(models.Model):
    """
    Clase usada para registrar los log de las evaluaciones del coordinador para una actividad
    - - - - -
    Attributes
    - - - - -
    credits : int
        Número de créditos
    observations : str
        Observaciones realizadas (opcional)
    activity : int
        Referencia a una actividad
    coordinator : int
        Referencia a un profesor
    date_record : datetime
        Fecha de registro
    date_update : datetime
        Fecha de último cambio realizado
    is_active : boolean
        Indica si el registro esta activo
    Methods
    - - - - - 
    void
    """
    
    credits = models.IntegerField(default=0, verbose_name='creditos')  
    observations = models.CharField(max_length=148, blank=True, verbose_name='observaciones')

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='actividad')
    coordinator = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='profesor')

    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Evaluación del coordinador'
        verbose_name_plural = 'Evaluaciónes de los coordinadores'

    def __str__(self):
        return '[{}] {}'.format(self.id, self.activity)


class TestDirector(models.Model):
    """
    Clase usada para registrar los log de las evaluaciones del director para una actividad
    - - - - -
    Attributes
    - - - - -
    value : int
        choices: 1_FAVORABLE, 2_NO_FAVORABLE
    observations : str
        Observaciones realizadas (opcional)
    activity : int
        Referencia a una actividad
    director : int
        Referencia a un profesor
    date_record : datetime
        Fecha de registro
    date_update : datetime
        Fecha de último cambio realizado
    is_active : boolean
        Indica si el registro esta activo
    Methods
    - - - - - 
    void
    """

    VALUE_CHOICES = ((1, _("FAVORABLE")), (2, _("NO_FAVORABLE")))

    value = models.IntegerField(choices=VALUE_CHOICES, default=1, verbose_name='calificacion')
    observations = models.CharField(max_length=148, blank=True, verbose_name='observacion')

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='actividad')
    director = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='profesor')

    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Evaluación del director'
        verbose_name_plural = 'Evaluaciones de los directores'

    def __str__(self):
        return '[{}] {}'.format(self.id, self.activity)


class Tracking(models.Model):
    """
    Clase usada para realizar el seguimiento de un estudiante
    - - - - -
    Attributes
    - - - - -
    status : int
        choices: 1_ACTIVO, 2_INACTIVO, 3_GRADUADO, 4_BALANCEADO, 5_RETIRADO
    enrrollment_date : date
        Fecha de matricula
    graduation_date : date
        Fecha de graduación
    num_folio : string
        Número de folio
    num_acta : string
        Número de acta
    num_diploma : string
        Número de diploma
    num_resolution : string
        Número de resolución
    observations : string (opcional)
        Observaciones
    student : int
        Referencia a un estudiante
    date_record : datetime
        Fecha de registro
    date_update : datetime
        Fecha de último cambio realizado
    is_active : boolean
        Indica si el registro esta activo
    Methods
    - - - - - 
    void
    """

    TYPE_CHOICES = ((1, _("ACTIVO")), (2, _("INACTIVO")),
                    (3, _("GRADUADO")), (4, _("BALANCEADO")), (5, _("RETIRADO")))
    
    status = models.IntegerField(choices=TYPE_CHOICES, default=1, verbose_name='estado')
    enrrollment_date = models.DateField(auto_now=False, blank=True, null=True, verbose_name='fecha de matricula')
    graduation_date = models.DateField(auto_now=False, blank=True, null=True, verbose_name='fecha de graduación')
    num_folio = models.CharField(max_length=24, blank=True, verbose_name='numero de folio')
    num_acta = models.CharField(max_length=24, blank=True, verbose_name='numero de acta')
    num_diploma = models.CharField(max_length=24, blank=True, verbose_name='numero de diploma')
    num_resolution = models.CharField(max_length=24, blank=True, verbose_name='numero de resolucion')
    observations = models.CharField(max_length=148, blank=True, verbose_name='observaciones')

    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='estudiante')

    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Seguimiento'
        verbose_name_plural = 'Seguimientos'

    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.student, self.status)

def create_customer(sender, instance, created, **kwargs):
    if created:
        try:
            queryset = Enrrollment.objects.filter(
                student__user=instance.student.user).order_by('-period')[:1]
            queryset = queryset[0]
            queryset.state = instance.status
            queryset.save()
        except:
            pass

post_save.connect(create_customer, sender=Tracking)


class ActivityProfessor(models.Model):
    """
    Clase usada para vincular profesores a la activdad como director, coodirector y/o coordinador
    - - - - -
    Attributes
    - - - - -
    activity : int
        Referencia a una actividad
    professor : int
        Referencia a un profesor
    rol : int
        Rol del profesor en la actividad
        choices: 1_DIRECTOR, 2_COODIRECTOR, 3_COORDINADOR
    Methods
    - - - - - 
    void
    """

    TYPE_CHOICES = ((1, _("DIRECTOR")), (2, _("COODIRECTOR")), (3, _("COORDINADOR")))

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='actividad')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name='profesor')
    rol = models.IntegerField(choices=TYPE_CHOICES, default=1, verbose_name='rol')

    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Actividad de un profesor'
        verbose_name_plural = 'Actividades de un profesor'

    def __str__(self):
        return '[{}] {} | {} | {}'.format(self.id, self.activity, self.professor, self.rol)