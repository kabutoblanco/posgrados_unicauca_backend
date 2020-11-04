from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Permission, AbstractUser

# Create your models here.
class User(AbstractUser):
    ID_CHOICES = (
        (1, _("CEDULA")),
        (2, _("CEDULA_EXTRANJERIA")),
        (3, _("TARJETA_IDENTIDAD")),
    )

    type_id = models.IntegerField(verbose_name='Tipo de ID', choices=ID_CHOICES, default=1)
    personal_id = models.CharField(verbose_name='Numero de ID', max_length=24)
    personal_code = models.CharField(verbose_name='Codigo ID', max_length=24)
    photo = models.FileField(verbose_name='Foto', upload_to="d_accounts_app/users", blank=False, null=True)
    telephone = models.CharField(verbose_name='Telefono', max_length=24)
    address = models.CharField(verbose_name='Direccion', max_length=64)

    is_proffessor = models.BooleanField(verbose_name='Es profesor', default=False)
    is_student = models.BooleanField(verbose_name='Es estudiante', default=True)

    class Meta:
        indexes = [
            models.Index(fields=['personal_id', 'personal_code',]),
            ]
    


