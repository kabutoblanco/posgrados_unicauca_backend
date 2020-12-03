#Este va servir como un estilo de view.py, este es el enlace el cual recibe la peticion y
#se comunica con el serializador

from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from d_accounts_app.backends import IsProfessor

from .serializers import (CountrySerializer, StateSerializer, CitySerializer, InstitutionSerializer, 
                        ProfessorSerializer, FacultySerializer, DepartmentSerializer, InvestigationGroupSerializer,
                        KnowledgeAreaSerializer, InvestigationLineSerializer, WorksInvestGroupSerializer, 
                        ManageInvestLineSerializer, ManageInvestGroupSerializer, AcademicTrainingSerializer,
                        IsMemberSerializer)

from .models import (Country, State, City, Institution, Professor, Faculty, Department, AcademicTraining,
                    InvestigationGroup, KnowledgeArea, InvestigationLine, WorksInvestGroup, ManageInvestGroup,
                    ManageInvestLine, IsMember)

# Create your api's here.
# --------------------------------------------------Arias

#region Create
#coordinador_comite de programa y el superUser 
class CreateCountryAPI(generics.GenericAPIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Crear un País, esta función hace uso del metodo POST.
    PATH: 'api/1.0/crear_pais/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    #permission_classes = [IsAuthenticated, IsProfessor]
    serializer_class = CountrySerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data) 
        if serializer.is_valid():#Valida que los tipos de datos sean correctos
            test = Country.objects.filter(name=request.data["name"])
            if not(test):
                country = serializer.save()              
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateStateAPI(generics.GenericAPIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒►Departamento en contexto de País
    API que permite:
    ☠ Crear un Departamento, esta función hace uso del metodo POST.
    PATH: 'api/1.0/crear_departamento/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    serializer_class = StateSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = State.objects.filter(name=request.data['name'])
            if not(isElement):
                department = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateCityAPI(generics.GenericAPIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Crear una Ciudad, esta función hace uso del metodo POST.
    PATH: 'api/1.0/crear_ciudad/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    serializer_class = CitySerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = City.objects.filter(name=request.data['name'])
            if not(isElement):
                city = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateInstitutionAPI(generics.GenericAPIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Crear una Institución, esta función hace uso del metodo POST.
    PATH: 'api/1.0/crear_institucion/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    serializer_class = InstitutionSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = Institution.objects.filter(name_inst=request.data['name_inst'])
            if not(isElement):
                institution = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateFacultyAPI(generics.GenericAPIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Crear una Facultad, esta función hace uso del metodo POST.
    PATH: 'api/1.0/crear_facultad/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    serializer_class = FacultySerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = Faculty.objects.filter(name=request.data['name'])
            if not(isElement):
                faculty = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateDepartmentAPI(generics.GenericAPIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒►Departamento en contexto de Facultad
    API que permite:
    ☠ Crear un Departamento, esta función hace uso del metodo POST.
    PATH: 'api/1.0/crear_departamento_u/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    serializer_class = DepartmentSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = Department.objects.filter(name=request.data['name'])
            if not(isElement):
                department = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#endregion

#region Consult
class ConsultCountryAPI(APIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Consultar Paises, esta función hace uso del metodo GET.
    PATH: 'api/1.0/consultar_pais/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    def get(self, request, *args, **kwargs):
        queryset = Country.objects.all()
        return Response({"Countrys": CountrySerializer(queryset, many=True).data })

class ConsultCountry_idAPI(APIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Consultar País enviando su id, esta función hace uso del metodo GET.
    ☠ Actualizar un País enviando un JSON, esta función hace uso del método PUT.
    PATH: 'api/1.0/consultar_pais_id/<int:id_country>'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    def get(self, request, *args, **kwargs):
        queryset = Country.objects.filter(id=kwargs["id_country"])
        returned = CountrySerializer(queryset, many=True).data
        if returned:
            return Response({"Country": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe el País en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = Country.objects.get(id=request.data['id'])
        except Country.DoesNotExist:
            return Response(f"No existe el País en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = CountrySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultState_CountryAPI(APIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒►Departamento en contexto de País
    API que permite:
    ☠ Consultar Departamentos de un determinado País enviando su id, esta función hace uso del metodo GET.
    ☠ Actualizar un País enviando un JSON, esta función hace uso del método PUT.
    PATH: 'api/1.0/consultar_departamento_pais/<int:id_country>'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    def get(self, request, *args, **kwargs):
        queryset = State.objects.filter(country=kwargs["id_country"])
        returned = StateSerializer(queryset, many=True).data
        if returned:
            return Response({"States": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existen Departamentos con ese País en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = State.objects.get(id=request.data['id'])
        except State.DoesNotExist:
            return Response(f"No existe ese Departamento en la base de datos", status=status.HTTP_404_NOT_FOUND)
        
        print(request.data)
        serializer = StateSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultCity_StateAPI(APIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Consultar Ciudades de un determinado Departamento enviando su id, esta función hace uso del metodo GET.
    ☠ Actualizar un Departamento enviando un JSON, esta función hace uso del método PUT.
    PATH: 'api/1.0/consultar_ciudad_departamento/<int:id_dep>'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    def get(self, request, *args, **kwargs):
        queryset = City.objects.filter(state=kwargs["id_dep"])
        returned = CitySerializer(queryset, many=True).data
        if returned:
            return Response({"Cities": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existen Ciudades con ese Departamento en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = City.objects.get(id=request.data['id'])
        except City.DoesNotExist:
            return Response(f"No existe esa Ciudad en la base de datos", status=status.HTTP_404_NOT_FOUND)
        
        print(request.data)
        serializer = CitySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultInstitutionAPI(APIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Consultar Instituciones, esta función hace uso del metodo GET.
    PATH: 'api/1.0/consultar_institucion/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    def get(self, request, *args, **kwargs):
        queryset = Institution.objects.all()
        return Response({"Institutions": InstitutionSerializer(queryset, many=True).data })

class ConsultInstitution_idAPI(APIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Consultar un Instituto enviando su id, esta función hace uso del metodo GET.
    ☠ Actualizar un Instituto enviando un JSON, esta función hace uso del método PUT.
    PATH: 'api/1.0/consultar_institucion_id/<int:id>'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    def get(self, request, *args, **kwargs):
        queryset = Institution.objects.filter(id=kwargs["id"]) 
        returned = InstitutionSerializer(queryset, many=True).data
        if returned:
            return Response({"Institution": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe Instituto en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = Institution.objects.get(id=request.data['id'])
        except Institution.DoesNotExist:
            return Response(f"No existe Instituto en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = InstitutionSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultFacultyAPI(APIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Consultar Facultades, esta función hace uso del metodo GET.
    PATH: 'api/1.0/consultar_facultad/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    def get(self, request, *args, **kwargs):
        queryset = Faculty.objects.all()
        return Response({"Facultys": FacultySerializer(queryset, many=True).data })

class ConsultFaculty_idAPI(APIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Consultar una Facultad enviando su id, esta función hace uso del metodo GET.
    ☠ Actualizar una Facultad enviando un JSON, esta función hace uso del método PUT.
    PATH: 'api/1.0/consultar_facultad_id/<int:id>'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    def get(self, request, *args, **kwargs):
        queryset = Faculty.objects.filter(id=kwargs["id"])  
        returned = FacultySerializer(queryset, many=True).data
        if returned:
            return Response({"Faculty": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe Facultad en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = Faculty.objects.get(id=request.data['id'])
        except Faculty.DoesNotExist:
            return Response(f"No existe Facultad en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = FacultySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultDepartmentAPI(APIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒►Departamento en contexto de Facultad
    API que permite:
    ☠ Consultar Departamentos, esta función hace uso del metodo GET.
    PATH: 'api/1.0/consultar_departamentoU/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    def get(self, request, *args, **kwargs):
        queryset = Department.objects.all()
        return Response({"Departments": DepartmentSerializer(queryset, many=True).data })

class ConsultDepartment_idAPI(APIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒►Departamento en contexto de Facultad
    API que permite:
    ☠ Consultar un Departamento enviando su id, esta función hace uso del metodo GET.
    ☠ Actualizar un Departamento enviando un JSON, esta función hace uso del método PUT.
    PATH: 'api/1.0/consultar_departamentoU_id/<int:id>'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    def get(self, request, *args, **kwargs):
        queryset = Department.objects.filter(id=kwargs["id"])  
        returned = DepartmentSerializer(queryset, many=True).data
        if returned:
            return Response({"Department": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe Departamento en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = Department.objects.get(id=request.data['id'])
        except Department.DoesNotExist:
            return Response(f"No existe Departamento en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#endregion

# Create your api's here.
# --------------------------------------------------Jeison

#region Create
#coordinador_comite de programa y el superUser 
class CreateInvestigationGroupAPI(generics.GenericAPIView):
    """
    Clase usada para la implementacion de la API para crear un 
    Grupo de Investigacion
    """

    serializer_class = InvestigationGroupSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = InvestigationGroup.objects.filter(name=request.data['name'])
            if not(isElement):
                investigationGroup = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#director de grupo de inv y el coordinador_comite
class CreateKnowledgeAreaAPI(APIView):
    """
    Clase usada para la implementacion de la API para crear un 
    Area del Conocimiento
    """
    def post(self, request):
        serializer = KnowledgeAreaSerializer(data = request.data)
        if serializer.is_valid():
            isElement = KnowledgeArea.objects.filter(name=request.data['name'])
            if not(isElement):
                knowledgeArea = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateInvestigationLineAPI(generics.GenericAPIView):
    """
    Clase usada para la implementacion de la API para crear una
    Linea de Investigacion
    """
    serializer_class = InvestigationLineSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = InvestigationLine.objects.filter(name=request.data['name'])
            if not(isElement):
                investigationLine = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateProfessorAPI(generics.GenericAPIView):# toca modificarlo a los cambios nuevos
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Crear un Profesor, esta función hace uso del metodo POST.
    PATH: 'api/1.0/crear_profesor/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    serializer_class = ProfessorSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data) 
        if serializer.is_valid():
            professor = serializer.save()              
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateAcademicTrainingAPI(generics.GenericAPIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Crear una Formación Academica, esta función hace uso del metodo POST.
    PATH: 'api/1.0/crear_formacion_academica/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    permission_classes = [IsAuthenticated, IsProfessor]
    serializer_class = AcademicTrainingSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():#Toca arreglar el filtro. Att_:JAVIER
            isElement = AcademicTraining.objects.filter(professor=request.data['professor'],degree=request.data['degree'])
            if not(isElement):
                academicTraining = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#director de grupo de inv
class CreateWorksInvestGroupAPI(generics.GenericAPIView):
    """
    Clase usada para la implementacion de la API para crear una relacion
    de rol Trabaja entre los modelos de Grupo de Investigacion y Area del Conocimiento
    """
    serializer_class = WorksInvestGroupSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = WorksInvestGroup.objects.filter(
                inv_group=request.data['inv_group'], know_area=request.data['know_area']
            )
            if not(isElement):
                korksInvestGroup = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#coordinador_commite
class CreateManageInvestGroupAPI(generics.GenericAPIView):
    """
    Clase usada para la implementacion de la API para crear una relacion
    de rol Dirige entre los modelos de Profesor y Grupo de Investigacion
    """
    serializer_class = ManageInvestGroupSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = ManageInvestGroup.objects.filter(
                inv_group=request.data['inv_group'], professor=request.data['professor']
            )
            if not(isElement):
                directs = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#profesor no puede manejar una linea de investigacion si no pertenece a un grupo de inv que trabaje 
#con el area de conocimiento al que pertenece la linea de inv
class CreateManageInvestLineAPI(generics.GenericAPIView):
    """
    Clase usada para la implementacion de la API para crear una relacion
    de rol Maneja entre los modelos de Profesor y Linea de Investigacion
    """
    serializer_class = ManageInvestLineSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            drive = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateIsMemberAPI(generics.GenericAPIView):
    """
    Clase usada para la implementacion de la API para crear una relacion
    de rol Es Miembro entre los modelos de Profesor y Grupo de Investigacion
    """
    serializer_class = IsMemberSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = IsMember.objects.filter(
                inv_group=request.data['inv_group'], professor=request.data['professor']
            )
            if not(isElement):
                is_member = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#endregion

#region Consult

#coordinador_comite 
class ConsultInvestigationGroup_DepartmentAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar todos los
    Grupos de Investigacion que pertenecen a un Departamento espesifico de la Universidad,
    esto se logra enviando el ID del departamento mediante el metodo GET
    - - - - -
    Parameter
    - - - - -
    dep : int
        Referencia a un departamento
    """
    def get(self, request, *args, **kwargs):
        queryset = InvestigationGroup.objects.filter(department=kwargs['dep'])
        return Response({"Groups": InvestigationGroupSerializer(queryset, many=True).data })

class ConsultInvestigationGroup_idAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar y editar un Grupo de Investigacion
    espesifico de la Universidad, esto se logra enviando el ID del Grupo de investigacion mediante 
    el metodo GET y/o enviando la informacion que se va a editar del Grupo de Investigacion mediante
    el metodo POST
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un grupo de investigacion
    """
    def get(self, request, *args, **kwargs):
        queryset = InvestigationGroup.objects.filter(id=kwargs['id'])
        
        returned = InvestigationGroupSerializer(queryset, many=True).data
        if returned:
            return Response({"Group": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe el Grupo de investigacion en la base de datos", status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, *args, **kwargs):
        try:
            model = InvestigationGroup.objects.get(id=kwargs['id'])
        except InvestigationGroup.DoesNotExist:
            return Response(f"No existe el Grupo de investigacion en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = InvestigationGroupSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultProfessorAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar todos los Profesores
    registrados en la Universidad
    """
    def get(self, request, *args, **kwargs):
        queryset = Professor.objects.all()
        return Response({"Professors": ProfessorSerializer(queryset, many=True).data })

class ConsultProfessor_idAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar y editar un Profesor espesifico
    de la Universidad, esto se logra enviando el ID del Profesor mediante el metodo GET y/o enviando
    la informacion que se va a editar del Profesor mediante el metodo POST
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un profesor
    """
    def get(self, request, *args, **kwargs):
        queryset = Professor.objects.filter(id=kwargs['id'])

        returned = ProfessorSerializer(queryset, many=True).data
        if returned:
            return Response({"Professor": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe el Profesor en la base de datos", status=status.HTTP_404_NOT_FOUND)

#coordinador_comite, profesor_director
class ConsultKnowledgeAreaAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar todas las Areas del Conocimiento 
    registradas en la Universidad
    """
    def get(self, request, *args, **kwargs):
        queryset = KnowledgeArea.objects.all()
        return Response({"Knowledges": KnowledgeAreaSerializer(queryset, many=True).data })

class ConsultKnowledgeArea_idAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar y editar un Area del Conocimiento espesifica
    de la Universidad, esto se logra enviando el ID del Area del Conocimiento mediante el metodo GET y/o enviando
    la informacion que se va a editar del Area del Conocimiento mediante el metodo POST
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un Area del Conocimiento
    """
    def get(self, request, *args, **kwargs):
        queryset = KnowledgeArea.objects.filter(id=kwargs['id'])
        returned = KnowledgeAreaSerializer(queryset, many=True).data
        if returned:
            return Response({"Knowledge": KnowledgeAreaSerializer(queryset, many=True).data })
        else:
            return Response(f"No existe el Area de conocimiento en la base de datos...")

    def put(self, request, *args, **kwargs):
        try:
            model = KnowledgeArea.objects.get(id=kwargs['id'])
        except KnowledgeArea.DoesNotExist:
            return Response(f"No existe el Area de conocimiento en la base de datos...")
        
        serializer = KnowledgeAreaSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#profesor, profesor_director, coordinador_comite
class ConsultInvestigationLine_knowledgeAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar todas las Lineas de Investigacion que
    pertenecen a un Area del conocimiento espesifica
    - - - - -
    Returned
    - - - - -
    Metodo GET:
        Si el id es correcto y se encuentran resultados:
            {"Lines": JsonResultado}}
        Si no se encuentran resultados:
            Se mostrata un mensaje de error
    """
    def get(self, request, *args, **kwargs):
        queryset = InvestigationLine.objects.filter(know_area=kwargs['id_area'])
        returned = InvestigationLineSerializer(queryset, many=True).data
        if returned:
            return Response({"Lines": InvestigationLineSerializer(queryset, many=True).data })
        else:
            return Response(f"No existen Lineas de Investigacion asociadas a esa Area del conocimiento...")

class ConsultInvestigationLine_idAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar una Linea de Investigacion espesifica 
    de la Universidad, esto se logra enviando el ID de la Linea de Investigacion mediante el metodo GET 
    y/o enviando la informacion que se va a editar de la Linea de Investigacion mediante el metodo POST
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a una Linea de Investigacion
    - - - - -
    Returned
    - - - - -
    Metodo GET:
        Si el id es correcto y se encuentran resultados:
            {"Line": JsonResultado, HTTP_202_ACCEPTED}}
        Si no se encuentran resultados:
            Se mostrata un mensaje de error, HTTP_404_NOT_FOUND
    Metodo PUT:
        Si el id es correcto y se encuentran resultados:
            {JsonResultado, HTTP_202_ACCEPTED}}
        Si no se encuentran resultados:
            Se mostrata un mensaje de error, HTTP_404_NOT_FOUND
            Se mostrata un mensaje de error, HTTP_400_BAD_REQUEST
    """
    def get(self, request, *args, **kwargs):
        queryset = InvestigationLine.objects.filter(id=kwargs['id'])
        returned = InvestigationLineSerializer(queryset, many=True).data
        if returned:
            return Response({"Line": InvestigationLineSerializer(queryset, many=True).data })
        else:
            return Response(f"No existe la Linea de investigacion en la base de datos...")

    def put(self, request, *args, **kwargs):
        try:
            model = InvestigationLine.objects.get(id=kwargs['id'])
        except InvestigationLine.DoesNotExist:
            return Response(f"No existe la Linea de investigacion en la base de datos...")

        serializer = InvestigationLineSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultIsMemberAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar si un profesor ES MIEMBRO o no de un 
    grupo de investigacion espesifico de la Universidad, esto se logra enviando el ID del Profesor y 
    el ID del Grupo de Investigacion (en ese orden) mediante el metodo GET y/o enviando la informacion 
    que se va a editar del registro del modelo "Es Miembro" mediante el metodo POST
    - - - - -
    Parameters
    - - - - -
    id_p : int
        Referencia a un Profesor
    id_gi : int
        Referencia a un Grupo de Investigacion
    - - - - -
    Returned
    - - - - -
    Metodo GET:
        Si el id es correcto y se encuentran resultados:
            {"IsMember": JsonResultado, HTTP_202_ACCEPTED}}
        Si no se encuentran resultados:
            Se mostrata un mensaje de error, HTTP_404_NOT_FOUND
    Metodo PUT:
        Si el id es correcto y se encuentran resultados:
            {JsonResultado, HTTP_202_ACCEPTED}}
        Si no se encuentran resultados:
            Se mostrata un mensaje de error, HTTP_404_NOT_FOUND
            Se mostrata un mensaje de error, HTTP_400_BAD_REQUEST
    """
    def get(self, request, *args, **kwargs):
        queryset = IsMember.objects.filter(inv_group=kwargs['id_gi'], professor=kwargs['id_p'])
        returned = IsMemberSerializer(queryset, many=True).data
        if returned:
            return Response({"IsMember":returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, *args, **kwargs):
        try:
            model = IsMember.objects.get(inv_group=kwargs['id_gi'], professor=kwargs['id_p'])
        except IsMember.DoesNotExist:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)

        serializer = IsMemberSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultWorksInvestGroupAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar si un Grupo de Investigacion TRABAJA o no en un
    Area del Conocimiento espesifica de la Universidad, esto se logra enviando el ID del Grupo de Investigacion y 
    el ID del Area del Conocimiento (en ese orden) mediante el metodo GET y/o enviando la informacion 
    que se va a editar del registro del modelo "Trabaja" mediante el metodo POST
    - - - - -
    Parameters
    - - - - -
    id_gi : int
        Referencia a un Grupo de Investigacion
    id_ac : int
        Referencia a un Area del Conocimiento
    - - - - -
    Returned
    - - - - -
    Metodo GET:
        Si el id es correcto y se encuentran resultados:
            {"Work": JsonResultado, HTTP_202_ACCEPTED}}
        Si no se encuentran resultados:
            Se mostrata un mensaje de error, HTTP_404_NOT_FOUND
    Metodo PUT:
        Si el id es correcto y se encuentran resultados:
            {JsonResultado, HTTP_202_ACCEPTED}}
        Si no se encuentran resultados:
            Se mostrata un mensaje de error, HTTP_404_NOT_FOUND
            Se mostrata un mensaje de error, HTTP_400_BAD_REQUEST
    """
    def get(self, request, *args, **kwargs):
        queryset = WorksInvestGroup.objects.filter(inv_group=kwargs['id_gi'], know_area=kwargs['id_ac'], study_status=True)
        returned = WorksInvestGroupSerializer(queryset, many=True).data
        if returned:
            return Response({"Work":returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, *args, **kwargs):
        try:
            model = WorksInvestGroup.objects.get(inv_group=kwargs['id_gi'], know_area=kwargs['id_ac'], study_status=True)
        except IsMember.DoesNotExist:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)

        serializer = WorksInvestGroupSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultManageInvestGroupAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar si un Profesor DIRIGE o no un
    Grupo de Investigacion espesifico de la Universidad, esto se logra enviando el ID del usuario del Profesor y 
    el ID del Grupo de Investigacion (en ese orden) mediante el metodo GET y/o enviando la informacion 
    que se va a editar del registro del modelo "Dirige" mediante el metodo POST
    - - - - -
    Parameters
    - - - - -
    id_p : int
        Referencia a un Profesor
    id_gi : int
        Referencia a un Grupo de Investigacion
    - - - - -
    Returned
    - - - - -
    Metodo GET:
        Si el id es correcto y se encuentran resultados:
            {"Manage": JsonResultado, HTTP_202_ACCEPTED}}
        Si no se encuentran resultados:
            Se mostrata un mensaje de error, HTTP_404_NOT_FOUND
    Metodo PUT:
        Si el id es correcto y se encuentran resultados:
            {JsonResultado, HTTP_202_ACCEPTED}}
        Si no se encuentran resultados:
            Se mostrata un mensaje de error, HTTP_404_NOT_FOUND
            Se mostrata un mensaje de error, HTTP_400_BAD_REQUEST
    """
    def get(self, request, *args, **kwargs):
        queryset = ManageInvestGroup.objects.filter(inv_group=kwargs['id_gi'], professor=kwargs['id_p'], direction_state=True)
        returned = ManageInvestGroupSerializer(queryset, many=True).data
        if returned:
            return Response({"Manage":returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, *args, **kwargs):
        try:
            model = ManageInvestGroup.objects.get(inv_group=kwargs['id_gi'], professor=kwargs['id_p'], direction_state=True)
        except IsMember.DoesNotExist:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)

        serializer = ManageInvestGroupSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultMemberIGAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar todos los miembros de un grupo de investigacion
    espesifico de la Universidad, esto se logra enviando el ID del Grupo de Investigacion (en ese orden) mediante
    el metodo GET
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un grupo de investigacion
    - - - - -
    Returned
    - - - - -
        Si el id es correcto y se encuentran resultados:
            {"Members": JsonResultado, HTTP_202_ACCEPTED}}
        Si no se encuentran resultados:
            Se mostrata un mensaje de error, HTTP_404_NOT_FOUND
    """
    def get(self, request, *args, **kwargs):
        queryset = IsMember.objects.filter(inv_group=kwargs['id'], member_status=True)
        returned = IsMemberSerializer(queryset, many=True).data
        if returned:
            return Response({"Members": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existen registros en la base de datos para el ID ingresado", status=status.HTTP_404_NOT_FOUND)

class ConsultMemberProfessorAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar si un profesor ES MIEMBRO o no de un 
    grupo de investigacion de la Universidad, esto se logra enviando el ID del Profesor mediante el metodo GET
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un Profesor
    - - - - -
    Returned
    - - - - -
        Si el id es correcto y se encuentran resultados:
            {"Members": JsonResultado, HTTP_202_ACCEPTED}}
        Si no se encuentran resultados:
            Se mostrata un mensaje de error, HTTP_404_NOT_FOUND
    """
    def get(self, request, *args, **kwargs):
        queryset = IsMember.objects.filter(professor=kwargs['id'], member_status=True)
        returned = IsMemberSerializer(queryset, many=True).data
        if returned:
            return Response({"Members": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            queryset = IsMember.objects.filter(professor=kwargs['id'])
            returned = IsMemberSerializer(queryset, many=True).data
            if returned:
                return Response(f"El profesor no se encuentra activo", status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(f"No existen registros en la base de datos para el ID ingresado", status=status.HTTP_404_NOT_FOUND)

class ConsultManageInvestGroup_DirecAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar que un profesor DIRIGE o no a un
    grupo de investigacion de la Universidad, esto se logra enviando el ID del Profesor mediante el metodo GET
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un Profesor
    - - - - -
    Returned
    - - - - -
        Si el id es correcto y se encuentran resultados:
            {"Manage": JsonResultado, HTTP_202_ACCEPTED}}
        Si no se encuentran resultados:
            Se mostrata un mensaje de error, HTTP_404_NOT_FOUND
    """
    def get(self, request, *args, **kwargs):
        queryset = ManageInvestGroup.objects.filter(professor=kwargs['id'], direction_state=True)
        returned = ManageInvestGroupSerializer(queryset, many=True).data
        if returned:
            return Response({"Manage": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existen registros en la base de datos para el ID ingresado", status=status.HTTP_404_NOT_FOUND)

#endregion




