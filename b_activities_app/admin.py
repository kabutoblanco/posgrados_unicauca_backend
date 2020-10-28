from django.contrib import admin
from .models import *

admin.site.register([
    Activity,
    Presentation,
    Publication,
    ProjectCourse,
    ResearchStays,
    PresentationResults,
    ParticipationProjects,
    Prize
])
