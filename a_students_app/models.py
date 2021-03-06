from django.db import models
from django.utils.translation import ugettext_lazy as _


from d_information_management_app.models import Professor
from d_accounts_app.models import User
from d_information_management_app.models import InvestigationGroup, Department, Institution


class GrantAgreement(models.Model):
    long = models.IntegerField(default=0)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    

    student = models.ForeignKey ('Student', on_delete=models.CASCADE )
    voucher = models.FileField (verbose_name='Comprobante', upload_to="voucher/%Y/%m/%d")

    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    

    class Meta:
        verbose_name = 'Beca/Convenio'
        verbose_name_plural = 'Becas/Convenios'

    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.start_date, self.end_date)


class Grant(GrantAgreement):
    name = models.CharField(max_length=48)
    announcement = models.IntegerField(default=0)#numero de convocatoria
    description = models.CharField(max_length=48)
    num_resolution = models.CharField(max_length=48)
    name_institution=models.CharField(max_length=60)#nombre de la institucion
    INSTITUTION_CHOICE = ((1, _("PUBLICA")), (2, _("PRIVADA")))
    type_institution= models.IntegerField(choices=INSTITUTION_CHOICE, default=1)
    INSTITUTIONLOCA_CHOICE = ((1, _("NACIONAL")), (2, _("EXTRANJERA")))
    location_institution= models.IntegerField(choices=INSTITUTIONLOCA_CHOICE, default=1)
    
       

    class Meta:
        verbose_name = 'Beca'
        verbose_name_plural = 'Becas'

    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.name, self.announcement)


class Agreement(GrantAgreement):
    agreement_date = models.DateField(auto_now=False)
    period_academic = models.CharField(max_length=12)
    percentage_discount = models.FloatField(default=0.0)
    observation = models.CharField(max_length=148)

   
    class Meta:
        verbose_name = 'Convenio'
        verbose_name_plural = 'Convenios'

    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.period_academic, self.percentage_discount)


class Program(models.Model):
    name = models.CharField(max_length=148)
    deparment = models.ForeignKey(Department, on_delete=models.CASCADE )
    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'

    def __str__(self):
        return '[{}] {}'.format(self.id, self.name)


class Student(models.Model):
    DEDICATION_CHOICE = ((1, _("COMPLETO")), (2, _("PARCIAL")))
    dedication = models.IntegerField(choices=DEDICATION_CHOICE, default=1)
    academic_title=models.CharField(max_length=256)
    instituion_degree = models.CharField(max_length=256)
    city_intituion = models.CharField(max_length=256)
    country_intituion = models.CharField(max_length=256)
    city_origin = models.CharField(max_length=256)
    departament_origin= models.CharField(max_length=256)


    user = models.ForeignKey(User, on_delete=models.CASCADE )
    program = models.ForeignKey(Program, on_delete=models.CASCADE )
    
    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.user, self.program)


class Enrrollment(models.Model):
    TYPE_CHOICES = ((1, _("ACTIVO")), (2, _("INACTIVO")),
                    (3, _("GRADUADO")), (4, _("BALANCEADO")), (5, _("RETIRADO")))

    admission_date = models.DateField(auto_now=False)
    enrrollment_date = models.DateField(auto_now=True)
    state = models.IntegerField(choices=TYPE_CHOICES)
    period = models.CharField(max_length=24)

    student = models.ForeignKey(Student, on_delete=models.CASCADE )

    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'

    def __str__(self):
        return '[{}] {} | {} | {}'.format(self.id, self.student, self.state, self.period)


class StudentProfessor(models.Model):
    TYPE_CHOICES = ((1, _("DIRECTOR")), (2, _("COODIRECTOR")))

    rol = models.IntegerField(choices=TYPE_CHOICES, default=1, verbose_name='rol')

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='estudiante')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name='profesor')
    

    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("student", "professor")
        verbose_name = 'Director/Coodirectores'
        verbose_name_plural = 'Directores/Coodirector'
        

        

    def __str__(self):
        return '[{}] {} | {} | {}'.format(self.id, self.student, self.professor, self.rol)


class StudentGroupInvestigation(models.Model):
    ##Hacer api     
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='estudiante')
    investigation_group = models.ForeignKey(InvestigationGroup, on_delete=models.CASCADE, verbose_name='grupo de investigacion')
    memberstatus = models.BooleanField(default=True)

    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Mis grupos de investigacion'
        verbose_name_plural = 'Mi grupo de investigacion'
       
    def __str__(self):
        return '[{}] {} | {}'.format(self.id, self.student, self.investigation_group)

