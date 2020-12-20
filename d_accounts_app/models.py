from django.db import models
from django.contrib.auth.models import Permission, AbstractUser
from django.utils.translation import ugettext_lazy as _


# Create your models here.
# MODIFICACIÓN DEL MODELO DE USUARIO POR DEFECTO DE DJANGO, INCLUYE:
    # - username
    # - email
    # - first_name, last_name
    # - password
    # - is_active
# POR DEFECTO, EL username ES USADO PARA EL LOGIN

# Create your models here.
class User(AbstractUser):
    ID_CHOICES = (
        (1, _("CEDULA")),
        (2, _("CEDULA_EXTRANJERIA")),
        (3, _("TARJETA_IDENTIDAD")),
    )

    type_id = models.IntegerField(verbose_name='Tipo de ID', choices=ID_CHOICES, default=1)
    personal_id = models.CharField(
        verbose_name='Numero de ID', 
        max_length=24, unique=True,
        error_messages={
            'Unico': _("El personal ID ya esta registrado."),
        },
    )
    personal_code = models.CharField(
        verbose_name='Codigo ID',
        max_length=24, unique=True,
        error_messages={
            'Unico': _("El Codigo Personal ya esta registrado."),
        },
    )
    photo = models.FileField(verbose_name='Foto', upload_to="d_accounts_app/users/%Y/%m/%d", default="/default/default_user.png")
    telephone = models.CharField(verbose_name='Telefono', max_length=24)
    address = models.CharField(verbose_name='Direccion', max_length=64)
    email = models.EmailField(
        _('email address'), 
        blank=True, unique=True,
        error_messages={
            'Unico': _("El Email ya esta registrado."),
        },
    )

    class Meta:
        indexes = [
            models.Index(fields=['personal_id', 'personal_code',]),
            ]


