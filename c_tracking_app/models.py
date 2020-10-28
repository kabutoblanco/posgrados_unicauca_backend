from django.db import models
from django.utils.translation import ugettext_lazy as _

from d_information_management_app.models import Professor
from b_activities_app.models import Activity

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
    credits = models.IntegerField(default=0)        
    observations = models.CharField(max_length=148)

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=True, null=True)
    coordinator = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=True, null=True)

    date_record = models.DateTimeField(auto_now=False)
    date_update = models.DateTimeField(auto_now=False)
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
    credits = models.IntegerField(default=0)
    observations = models.CharField(max_length=148)

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=True, null=True)
    coordinator = models.ForeignKey(Professor, on_delete=models.SET_NULL, blank=True, null=True)

    date_record = models.DateTimeField(auto_now=False)
    date_update = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Evaluación del director'
        verbose_name_plural = 'Evaluaciónes de los directores'

    def __str__(self):
        return '[{}] {}'.format(self.id, self.activity)


class Tracking(models.Model):
    """
    Clase usada para realizar el seguimiento de un estudiante
    - - - - -
    Attributes
    - - - - -
    state : int
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
    
    state = models.IntegerField(choices=TYPE_CHOICES, default=1)
    enrollment_date = models.DateField(auto_now=False)
    graduation_date = models.DateField(auto_now=False)
    num_folio = models.CharField(max_length=24)
    num_acta = models.CharField(max_length=24)
    num_diploma = models.CharField(max_length=24)
    num_resolution = models.CharField(max_length=24)
    observations = models.CharField(max_length=148, blank=True)

    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)

    date_record = models.DateTimeField(auto_now=False)
    date_update = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Seguimiento'
        verbose_name_plural = 'Seguimientos'

    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.student, self.state)