from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, GeneralViewSet, SpecificViewSet

router = DefaultRouter()
router.register('project', ProjectViewSet)
router.register('general', GeneralViewSet)
router.register('specific', SpecificViewSet)



urlpatterns = [ path('',include(router.urls))
]