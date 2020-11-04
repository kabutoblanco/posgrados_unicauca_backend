from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView 
from .models import Student,Enrrollment
from .serializers import StudentSerializer, UserSerializer, EnrrollmentSerializer, GrantSerializer, AgreementSerializer
from d_accounts_app.models import User
from rest_framework.status import (HTTP_201_CREATED)
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EnrrollmentViewSet(ModelViewSet):
    queryset = Enrrollment.objects.all()
    serializer_class = EnrrollmentSerializer

class StudentApiView(APIView):
    serializer_student= StudentSerializer
    serializer_enrrollment= EnrrollmentSerializer
    serializer_grant = GrantSerializer
    serializer_agreement = AgreementSerializer
    
    '''def post (self,request,*args):
        serializer = self.serializer_student(data=request.data['student'])
        if serializer.is_valid(raise_exception=True):
            serializer = serializer.save()
            
        enrrollment = request.data (request.data['enrrollment'])
        enrrollment['student']=serializer
        serializer = self.serializer_enrrollment(data=request.data['enrrollment'])
        if serializer.is_valid(raise_exception=True):
            serializer = serializer.save()
        if request.data (request.data['is_grant']):
            grant = request.data (request.data['grant'])
            grant['student']=serializer
            serializer = self.serializer_grant(data=request.data['grant'])
            if serializer.is_valid(raise_exception=True):
                serializer = serializer.save()
        else:
            aggreement = request.data (request.data['aggreement'])
            aggreement['student']=serializer
            serializer = self.serializer_agreement(data=request.data['aggreement'])
            if serializer.is_valid(raise_exception=True):
                serializer = serializer.save()
        return Response(status=HTTP_201_CREATED)'''
        
        
