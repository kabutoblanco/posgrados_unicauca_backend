from django.contrib import admin
from .models import *

admin.site.register([
    Activity,
    Lecture,
    Publication,
    ProjectCourse,
    ResearchStays,
    PresentationResults,
    ParticipationProjects,
    Prize
])
