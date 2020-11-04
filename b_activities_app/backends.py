from rest_framework import permissions

from a_students_app.models import Student, StudentProfessor
from c_tracking_app.models import ActivityProfessor

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

class IsStudent(permissions.BasePermission):
    """
    Clase que permite determinar si un usuario es estudiante o no
    """
    message = "No tiene permisos de un estudiante"

    def has_permission(self, request, view):
        try:
            student = Student.objects.get(user=request.user)
            if request.method == DELETE:
                return False
            elif request.method in permissions.SAFE_METHODS:
                return True
            else:
                return True
        except Student.DoesNotExist:
            return False
        
class IsDirector(permissions.BasePermission):
    """
    Clase que permite determinar si un usuario es director o no
    """
    message = "No tiene permisos de un director"

    def has_permission(self, request, view):
        try:
            StudentProfessor.objects.get(professor__user=request.user)
            if request.method == POST or request.method == DELETE:
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
            if request.method == POST or request.method == DELETE:
                return False
            else:
                return True
        except ActivityProfessor.DoesNotExist:
            return False
