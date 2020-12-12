from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student,Enrrollment,Program, StudentProfessor,Agreement,Grant
from .serializers import StudentSerializer, UserSerializer, EnrrollmentSerializer, GrantSerializer, AgreementSerializer,ProgramSerializer
from d_accounts_app.models import User

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EnrrollmentViewSet(ModelViewSet):
    queryset = Enrrollment.objects.all()
    serializer_class = EnrrollmentSerializer
    

class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer



class GrantViewSet(ModelViewSet):
    queryset = Grant.objects.all()
    serializer_class = GrantSerializer

class AgreementViewSet(ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

'''class StudentApiView(APIView):
    serializer_student= StudentSerializer
    serializer_enrrollment= EnrrollmentSerializer
    serializer_grant = GrantSerializer
    serializer_agreement = AgreementSerializer
    
    def post (self,request,*args):
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
        
        
