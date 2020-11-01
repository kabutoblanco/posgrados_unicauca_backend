from rest_framework import permissions

from .models import Professor

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

# class IsStudent(permissions.BasePermission):
#     """
#     Clase que permite determinar si un usuario es estudiante o no
#     """

#     message = "No tiene permisos de un estudiante"

#     def has_permission(self, request, view):
#         try: 
#             Student.objects.get(user=request.user)
#             return True
#         except Student.DoesNotExist:
#             return False

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