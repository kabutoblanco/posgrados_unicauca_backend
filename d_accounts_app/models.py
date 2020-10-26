from django.db import models
from django.contrib.auth.models import Permission, AbstractUser

# Create your models here.
class User(AbstractUser):
    ID_CHOICES = (
        (1, _("CEDULA")),
        (2, _("CEDULA_EXTRANJERIA")),
        (3, _("TARJETA_IDENTIDAD")),
    )

    type_id = models.IntegerField(choices=ID_CHOICES, default=1)
    personal_id = models.CharField(max_length=24)
    personal_code = models.CharField(max_length=24)
    photo = models.FileField()
    telephone = models.CharField(max_length=24)
    address = models.CharField(max_length=64)

    is_proffessor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    


