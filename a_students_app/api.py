from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UpdateStudentSerializer,StudentSerializer,StudentProfessorSerializer
from .models import Student,StudentProfessor
from d_information_management_app.models import Professor

class CreateStudentProfessor(generics.GenericAPIView):
    serializer_class=StudentProfessorSerializer
    def post (self,request):
        print("-----",type(request.data["rol"]))
        serializer= self.get_serializer(data=request.data)
        if serializer.is_valid():
            if (int(request.data["rol"])==1):
                print("Entro el director")
                isdirector= StudentProfessor.objects.filter(student=request.data["student"],
                professor=request.data["professor"], rol= request.data["rol"])
            
                if not(isdirector):
                    auxprofessor = Professor.objects.get(id=request.data["professor"])
                    auxprofessor.is_director_student=True
                    auxprofessor.save()
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                return Response(f"Ya cuenta con su director",status=status.HTTP_400_BAD_REQUEST)
            else:
                print("Entro el codirector")
                iscodirector= StudentProfessor.objects.filter(student=request.data["student"], rol= request.data["rol"]) 
                if (len(iscodirector)<2):
                    auxprofessor = Professor.objects.get(id=request.data["professor"])
                    auxprofessor.is_director_student=True
                    auxprofessor.save()
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                return Response(f"Ya cuenta con dos coodirectores",status=status.HTTP_400_BAD_REQUEST)
            
        


'''class UpdateStudenAPI (APIView):
    def get (self,request,*args,**kwargs):
        model=Student.objects.filter(id=kwargs["id"])
        return Response(UpdateStudentSerializer(model, many=True).data,status=status.HTTP_202_ACCEPTED)
    def put (self,request,*args,**kwargs):
        try:
            model = Student.objects.get(id=kwargs["id"])
        except Student.DoesNotExist:
            return Response(f"El Estudiante con el ID solicitado no existe en la Base de Datos.",status= status.HTTP_404_NOT_FOUND)
        serializer = UpdateStudentSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''  
