from django.urls import path, include
from .api import UserAPI, LoginAPI, CreateUserAPI, ConsultUser_PersonalAPI, ConsultUserAPI
from knox import views as knox_views


urlpatterns = [
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/auth/create_user', CreateUserAPI.as_view()),
    path('api/auth/consult_user', ConsultUserAPI.as_view()),
    path('api/auth/consult_user/<int:id>', ConsultUser_PersonalAPI.as_view()),
]