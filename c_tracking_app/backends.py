from rest_framework import permissions

from a_students_app.models import StudentProfessor
from d_information_management_app.models import Professor
from .models import ActivityProfessor

class IsDirector(permissions.BasePermission):
    """
    Clase que permite determinar si un usuario es director o no
    """
    message = "No tiene permisos de un director"

    def has_permission(self, request, view):
        try:
            StudentProfessor.objects.get(professor__user=request.user)
            if request.method == DELETE:
                return False
            else:
                return True
        except StudentProfessor.DoesNotExist:
            return False

class IsCoordinador(permissions.BasePermission):
    """
    Clase que permite determinar si un usuario es coordinador o no
    """
    message = "No tiene permisos de un coordinador"

    def has_permission(self, request, view):
        try:
            ActivityProfessor.objects.get(professor__user=request.user)
            if request.method == DELETE:
                return False
            else:
                return True
        except ActivityProfessor.DoesNotExist:
            return False
