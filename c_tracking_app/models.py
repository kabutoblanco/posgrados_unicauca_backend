from django.db import models
from django.utils.translation import ugettext_lazy as _

from d_information_management_app.models import Professor
from b_activities_app.models import Activity

class TestCoordinator(models.Model):
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