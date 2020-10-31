from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()

router.register('activity', ActivityViewSet)
router.register('lecture', LectureViewSet)
router.register('publication', PublicationViewSet)
router.register('projectCourse', ProjectCourseViewSet)
router.register('researchStays', ResearchStaysViewSet)
router.register('presentationResults', PresentationResultsViewSet)
router.register('participationProjects', ParticipationProjectsViewSet)
router.register('prize', PrizeViewSet)

urlpatterns = [
    path( 'api/', include(router.urls) ),
    path( 'api/period/student/<int:id_user>/', PeriodAPI.as_view() ),
    path( 'api/periods/student/<int:id_user>/', PeriodsAPI.as_view() ),
    path( 'api/activities/student/<int:id_user>/<str:academic_year>/', ActivitiesAPI.as_view() )
]

#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)