from .models import *
from a_projects_app.models import Project
def change_enrrollment (sender, instance, created, **kwargs):
    pass

def change_student (sender, instance, created, **kwargs):
    if instance.is_active:
        projects = Project.objects.filter(student=instance.id)
        for project in projects:
            project.is_active = True
            project.save()
        grants = Grant.objects.filter(student=instance.id)
        for grant in grants:
            grant.is_active = True
            grant.save()
        agreements = Agreement.objects.filter(student=instance.id)
        for agrement in agreements:
            agrement.is_active = True
            agrement.save()
    else:
        projects = Project.objects.filter(student=instance.id)
        for project in projects:
            project.is_active = False
            project.save()
        grants = Grant.objects.filter(student=instance.id)
        for grant in grants:
            grant.is_active = False
            grant.save()
        agreements = Agreement.objects.filter(student=instance.id)
        for agrement in agreements:
            agrement.is_active = False
            agrement.save()

