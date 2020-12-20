from d_accounts_app.models import User
from .models import *
from a_students_app.models import Student, StudentGroupInvestigation, Program


def change_country(sender, instance, created, **kwargs):
    queryset = State.objects.filter(country=instance.id)
    if not instance.status:
        for state in queryset:
            state.status = False
            state.save()
    else:
        for state in queryset:
            state.status = True
            state.save()

def change_state(sender, instance, created, **kwargs):
    queryset = City.objects.filter(state=instance.id)
    if not instance.status:
        for city in queryset:
            city.status = False
            city.save()
    else:
        for city in queryset:
            city.status = True
            city.save()

def change_city(sender, instance, created, **kwargs):
    queryset = Institution.objects.filter(city=instance.id)
    if not instance.status:
        for institution in queryset:
            institution.status = False
            institution.save()
    else:
        for institution in queryset:
            institution.status = True
            institution.save()

def change_professor(sender, instance, created, **kwargs):
    if not instance.status:
        queryset = IsMember.objects.filter(professor=instance.id)
        for professor in queryset:
            professor.member_status = False
            professor.save()
        queryset = ManageInvestLine.objects.filter(professor=instance.id)
        for manage in queryset:
            manage.analysis_state = False
            manage.save()
        queryset = ManageInvestGroup.objects.filter(professor=instance.id)
        for manage in queryset:
            manage.direction_state = False
            manage.save()
        queryset = WorksDepartm.objects.filter(professor=instance.id)
        for works in queryset:
            works.laboral_state = False
            works.save()
        queryset = CoordinatorProgram.objects.filter(professor=instance.id)
        for coord in queryset:
            coord.is_active = False
            coord.save()
    else:
        queryset = IsMember.objects.filter(professor=instance.id)
        for professor in queryset:
            professor.member_status = True
            professor.save()
        queryset = ManageInvestLine.objects.filter(professor=instance.id)
        for manage in queryset:
            manage.analysis_state = True
            manage.save()
        queryset = ManageInvestGroup.objects.filter(professor=instance.id)
        for manage in queryset:
            manage.direction_state = True
            manage.save()
        queryset = WorksDepartm.objects.filter(professor=instance.id)
        for works in queryset:
            aux = Department.objects.filter(id=works.department.id, status=True)
            if aux:
                works.laboral_state = False
                works.save()
        queryset = CoordinatorProgram.objects.filter(professor=instance.id)
        for coord in queryset:
            aux = Program.objects.filter(id=coord.program.id, is_active=True)
            if aux:
                coord.is_active = False
                coord.save()

def change_inv_group(sender, instance, created, **kwargs):
    if not instance.status:
        queryset = WorksInvestGroup.objects.filter(inv_group=instance.id)
        for work in queryset:
            work.study_status = False
            work.save()
        try:
            queryset = ManageInvestGroup.objects.get(inv_group=instance.id, direction_state=True)
            queryset.direction_state = False
            queryset.save()
            oldProfessor = Professor.objects.get(id=queryset.professor.pk, status=True)
            oldProfessor.is_director_gi = False
            oldProfessor.save()
        except:
            pass
        queryset = IsMember.objects.filter(inv_group=instance.id) 
        for member in queryset:
            member.is_active = False
            member.save()
        queryset = StudentGroupInvestigation.objects.filter(investigation_group=instance.id)
        for member in queryset:
            member.is_active = False
            member.save()
    else:
        queryset = WorksInvestGroup.objects.filter(inv_group=instance.id)
        for work in queryset:
            work.study_status = True
            work.save()
        try:
            queryset = ManageInvestGroup.objects.get(inv_group=instance.id, direction_state=True)
            queryset.direction_state = True
            queryset.save()
            oldProfessor = Professor.objects.get(id=queryset.professor.pk, status=True)
            oldProfessor.is_director_gi = True
            oldProfessor.save()
        except:
            pass
        queryset = IsMember.objects.filter(inv_group=instance.id) 
        for member in queryset:
            aux = Professor.objects.filter(id=member.professor.id, status=True)
            if aux:
                member.is_active = True
                member.save()
        queryset = StudentGroupInvestigation.objects.filter(investigation_group=instance.id)
        for member in queryset:
            aux = Student.objects.filter(id=member.student.id, is_active=True)
            if aux:
                member.is_active = True
                member.save()

def change_know_area(sender, instance, created, **kwargs):
    if instance.status:
        queryset = InvestigationLine.objects.filter(know_area=instance.id)
        for invLine in queryset:
            invLine.status = True
            invLine.save()
        queryset = WorksInvestGroup.objects.filter(inv_group=instance.id)
        for work in queryset:
            aux = InvestigationGroup.objects.filter(id=work.inv_group.id, status=True)
            if aux:
                work.study_status = True
                work.save()
    else:
        queryset = InvestigationLine.objects.filter(know_area=instance.id)
        for invLine in queryset:
            invLine.status = False
            invLine.save()
        queryset = WorksInvestGroup.objects.filter(inv_group=instance.id)
        for work in queryset:
            work.study_status = False
            work.save()

def change_inv_line(sender, instance, created, **kwargs):
    if instance.status:
        queryset = ManageInvestLine.objects.filter(inv_line=instance.id)
        for manage in queryset:
            aux = Professor.objects.filter(id=manage.professor.id, status=True)
            if aux:
                manage.analysis_state = False
                manage.save()
    else:
        queryset = ManageInvestLine.objects.filter(inv_line=instance.id)
        for manage in queryset:
            manage.analysis_state = False
            manage.save()

def change_user(sender, instance, created, **kwargs):
    if instance.is_active:
        queryset = Student.objects.filter(user=instance.id)
        for student in queryset:
            student.is_active = True
            student.save()
        queryset = Professor.objects.filter(user=instance.id)
        for professor in queryset:
            professor.status = True
            professor.save()
    else:
        queryset = Student.objects.filter(user=instance.id)
        for student in queryset:
            student.is_active = False
            student.save()
        queryset = Professor.objects.filter(user=instance.id)
        for professor in queryset:
            professor.status = False
            professor.save()

