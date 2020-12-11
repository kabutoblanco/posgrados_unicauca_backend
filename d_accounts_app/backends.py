from rest_framework import permissions

from .models import User
from d_information_management_app.models import Professor
from c_tracking_app.models import ActivityProfessor
from a_students_app.models import Student, StudentProfessor

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

class IsProfessor(permissions.BasePermission):
    """
    Clase para verificar si un usuario es profesor o no
    """

    message = "No tienes permisos de un profesor"

    def has_permission(self, request, view):
        try:
            professor = Professor.objects.get(user=request.user)
            if request.method == DELETE:
                return False
            elif request.method in permissions.SAFE_METHODS:
                return True
            else:
                return True
        except Professor.DoesNotExist:
            return False

class IsCoordinator(permissions.BasePermission):
    """
    Clase para verificar si un usuario es coordinador o no
    """

    message = "No tienes permisos de un coordinador"

    def has_permission(self, request, view):
        try:
            User.objects.get(id=request.user.pk, is_coordinator=True)
            return True
        except User.DoesNotExist:
            return False

class IsCoordinator_user(permissions.BasePermission):
    """
    Clase para verificar si un usuario es coordinador o no
    """

    message = "No tienes permisos de un coordinador"

    def has_permission(self, request, view):
        try:
            User.objects.get(id=request.user.pk, is_coordinator=True)
            if request.method == POST:
                return True
            return True
        except User.DoesNotExist:
            return False

class IsDirector_C(permissions.BasePermission):
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

class IsDirector_B(permissions.BasePermission):
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

class IsCoordinador_C(permissions.BasePermission):
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

class IsCoordinador_B(permissions.BasePermission):
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

class IsCoordinator2(permissions.BasePermission):
    """
    Clase que permite determinar si un usuario es del comite de coordinadores
    """
    message = "No tiene permisos de un Coordinador del comite"

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
