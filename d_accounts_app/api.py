from rest_framework import generics, permissions, views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from knox.models import AuthToken
from .models import User
from .serializers import *

from d_information_management_app.models import Professor, ManageInvestGroup, CoordinatorProgram
from c_tracking_app.models import ActivityProfessor
from a_students_app.models import Student, StudentProfessor

#region loguin
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user":
            UserSerializer(user, context=self.get_serializer_context()).data,
            "token":
            AuthToken.objects.create(user)[1]
        })

#endregion

#region usuarios

class CreateUserAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ConsultUserAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        return Response({"Users": ConsultUserSerializer(queryset, many=True).data })

class ConsultUser_PersonalAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.filter(personal_id=kwargs['id'])
        return Response({"Users": ConsultUserSerializer(queryset, many=True).data })

class ConsultUser_idAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.filter(id=kwargs['id'])
        return Response({"Users": ConsultUserSerializer(queryset, many=True).data })

    def put(self, request, *args, **kwargs):
        try:
            model = User.objects.get(id=kwargs['id'])
        except User.DoesNotExist:
            return Response(f"No existe el Usuario en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateUserSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
   
#endregion

#region autenticacion usuarios
class AuthUserAPI(APIView):
    def get(self, request, *args, **kwargs):
        typeList = ["Usuario sin rol"]
        try:
            CoordinatorProgram.objects.get(professor__user=kwargs['id'], professor__status=True)
            typeList.append("coordinador")
        except CoordinatorProgram.DoesNotExist:
            print("No es coordinador")
        try:
            ManageInvestGroup.objects.get(professor__user=kwargs['id'], professor__status=True)
            typeList.append("director")
        except ManageInvestGroup.DoesNotExist:
            print("No es director")
        try:
            Professor.objects.get(user=kwargs['id'], status=True)
            typeList.remove("Usuario sin rol")
            typeList.append("profesor")
        except Professor.DoesNotExist:
            print("No es profesor")
        try:
            Student.objects.get(user=kwargs['id'], is_active=True)
            typeList.append("estudiante")
        except Student.DoesNotExist:
            return Response(typeList)
        return Response(typeList)
        


#endregion

