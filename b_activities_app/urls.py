from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .api import *

# Modulo B #
router = DefaultRouter()

router.register('activity', ActivityViewSet)
router.register('lecture', LectureViewSet)
router.register('publication', PublicationViewSet)
router.register('projectCourse', ProjectCourseViewSet)
router.register('researchStays', ResearchStaysViewSet)
router.register('presentationResults', PresentationResultsViewSet)
router.register('participationProjects', ParticipationProjectsViewSet)
router.register('prize', PrizeViewSet)

# Consultas a otros modulos #
router.register('program', ProgramViewSet)
router.register('instititution', InstitutionViewSet)
router.register('investigationline', InvestigationLineViewSet)
router.register('investigator', InvestigatorViewSet)
router.register('city', CityViewSet)
router.register('country', CountryViewSet)

urlpatterns = [
    path( 'api/', include(router.urls) ),
    
    # Otro tipo de Consultas #
    path( 'api/testDirector/<int:id_activity>/', TestDirectorAPI.as_view() ),
    path( 'api/testCoordinator/<int:id_activity>/', TestCoordinatorAPI.as_view() ),
    path( 'api/period/student/<int:id_user>/', PeriodAPI.as_view() ),
    path( 'api/periods/student/<int:id_user>/', PeriodsAPI.as_view() ),
    path( 'api/activities/student/<int:id_user>/<str:academic_year>/', ActivitiesAPI.as_view() )
]

#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)