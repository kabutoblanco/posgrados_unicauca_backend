from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UpdateProject
from .models import Project


class UpdateProjectAPI (APIView):
    def get (self,request,*args,**kwargs):
        model= Project.objects.filter(id=kwargs["id"])
        return Response(UpdateProject(model, many=True).data,status=status.HTTP_202_ACCEPTED)
    def put (self,request,*args,**kwargs):
        try:
            model = Project.objects.get(id=kwargs["id"])
        except Project.DoesNotExist:
            return Response(f"El proyecto solicitado no existe en la Base de Datos.",status= status.HTTP_404_NOT_FOUND)
        serializer = UpdateProject(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)