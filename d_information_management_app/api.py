#Este va servir como un estilo de view.py, este es el enlace el cual recibe la peticion y
#se comunica con el serializador

from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from d_accounts_app.backend import IsProfessor, IsCoordinator
from d_accounts_app.models import User
from a_students_app.models import StudentGroupInvestigation

from .serializers import (CountrySerializer, StateSerializer, CitySerializer, InstitutionSerializer, 
                        ProfessorSerializer, FacultySerializer, DepartmentSerializer, InvestigationGroupSerializer,
                        KnowledgeAreaSerializer, InvestigationLineSerializer, WorksInvestGroupSerializer, 
                        ManageInvestLineSerializer, ManageInvestGroupSerializer, AcademicTrainingSerializer,
                        IsMemberSerializer, WorksDepartmSerializer, CoordinatorProgramSerializer)

from .models import (Country, State, City, Institution, Professor, Faculty, Department, AcademicTraining,
                    InvestigationGroup, KnowledgeArea, InvestigationLine, WorksInvestGroup, ManageInvestGroup,
                    ManageInvestLine, IsMember, WorksDepartm, CoordinatorProgram)

from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from a_students_app.models import Student,Enrrollment

import datetime

# Create your api's here.
# --------------------------------------------------Arias

#region Create
class ReportTest(APIView):
    def get(self, request, *args, **kwargs):

        states={1:"Activo",2:"Inactivo",3:"Graduado",4:"Balanceado",5:"Retirado"}
           
        year = kwargs["year"]
        queryset = Enrrollment.objects.filter(admission_date__range=(str(year)+"-1-1",str(year)+"-12-31"))

        if(kwargs["type"]==1):#Format xlsx request.data["tipo"]==1
            wb = Workbook()
            controller = 3
            ws = wb.active
            ws.title = 'Hoja'+str(1)

            #Create title in the sheet
            ws['B1'].alignment = Alignment(horizontal="center",vertical="center")
            ws['B1'].border = Border(left = Side(border_style = "thin"), right=Side(border_style = "thin"),
            top=Side(border_style="thin"),bottom=Side(border_style ="thin"))
            ws['B1'].fill = PatternFill(start_color = '66FFCC',end_color ='66FFCC', fill_type='solid')
            ws['B1'].font = Font(name = 'Calibri',size =14, bold =True)
            ws['B1'] = "INFORME DEL AÑO "+str(year)
            #Change the characteristics of cells
            ws.merge_cells('B1:G1')
            ws.row_dimensions[1].height = 25
            ws.column_dimensions['B'].width = 20
            ws.column_dimensions['C'].width = 20
            ws.column_dimensions['D'].width = 20
            ws.column_dimensions['E'].width = 20
            ws.column_dimensions['F'].width = 20
            ws.column_dimensions['G'].width = 20
            #Create header
            ws['B2'].alignment = Alignment(horizontal="center",vertical="center")
            ws['B2'].border = Border(left = Side(border_style = "thin"), right=Side(border_style = "thin"),
            top=Side(border_style="thin"),bottom=Side(border_style ="thin"))
            ws['B2'].fill = PatternFill(start_color = '66CFCC',end_color ='66CFCC', fill_type='solid')
            ws['B2'].font = Font(name = 'Calibri',size =12, bold =True)
            ws['B2']='Codigo'

            ws['C2'].alignment = Alignment(horizontal="center",vertical="center")
            ws['C2'].border = Border(left = Side(border_style = "thin"), right=Side(border_style = "thin"),
                                                top=Side(border_style="thin"),bottom=Side(border_style ="thin"))
            ws['C2'].fill = PatternFill(start_color = '66CFCC',end_color ='66CFCC', fill_type='solid')
            ws['C2'].font = Font(name = 'Calibri',size =12, bold =True)
            ws['C2']='Nombre'
                    
            ws['D2'].alignment = Alignment(horizontal="center",vertical="center")
            ws['D2'].border = Border(left = Side(border_style = "thin"), right=Side(border_style = "thin"),
                                                top=Side(border_style="thin"),bottom=Side(border_style ="thin"))
            ws['D2'].fill = PatternFill(start_color = '66CFCC',end_color ='66CFCC', fill_type='solid')
            ws['D2'].font = Font(name = 'Calibri',size =12, bold =True)
            ws['D2']='Estado'

            ws['E2'].alignment = Alignment(horizontal="center",vertical="center")
            ws['E2'].border = Border(left = Side(border_style = "thin"), right=Side(border_style = "thin"),
                                                top=Side(border_style="thin"),bottom=Side(border_style ="thin"))
            ws['E2'].fill = PatternFill(start_color = '66CFCC',end_color ='66CFCC', fill_type='solid')
            ws['E2'].font = Font(name = 'Calibri',size =12, bold =True)
            ws['E2']='Dedicación'

            ws['F2'].alignment = Alignment(horizontal="center",vertical="center")
            ws['F2'].border = Border(left = Side(border_style = "thin"), right=Side(border_style = "thin"),
                                                top=Side(border_style="thin"),bottom=Side(border_style ="thin"))
            ws['F2'].fill = PatternFill(start_color = '66CFCC',end_color ='66CFCC', fill_type='solid')
            ws['F2'].font = Font(name = 'Calibri',size =12, bold =True)
            ws['F2']='Institución'

            ws['G2'].alignment = Alignment(horizontal="center",vertical="center")
            ws['G2'].border = Border(left = Side(border_style = "thin"), right=Side(border_style = "thin"),
                                                top=Side(border_style="thin"),bottom=Side(border_style ="thin"))
            ws['G2'].fill = PatternFill(start_color = '66CFCC',end_color ='66CFCC', fill_type='solid')
            ws['G2'].font = Font(name = 'Calibri',size =12, bold =True)
            ws['G2']='Departamento'

            for q in queryset:    
                ws.cell(row=controller,column=2).alignment = Alignment(horizontal="center")
                ws.cell(row=controller,column=2).border = Border(left = Side(border_style = "thin"), right=Side(border_style = "thin"),
                                                                        top=Side(border_style="thin"),bottom=Side(border_style ="thin"))
                ws.cell(row =controller, column=2).font = Font(name='Calibri',size=12)       
                ws.cell(row =controller, column=2).value = q.student.user.personal_code

                ws.cell(row=controller,column=3).alignment = Alignment(horizontal="center")
                ws.cell(row=controller,column=3).border = Border(left = Side(border_style = "thin"), right=Side(border_style = "thin"),
                                                                        top=Side(border_style="thin"),bottom=Side(border_style ="thin"))
                ws.cell(row =controller, column=3).font = Font(name='Calibri',size=12)       
                ws.cell(row =controller, column=3).value = q.student.user.first_name+" "+q.student.user.last_name 

                ws.cell(row=controller,column=4).alignment = Alignment(horizontal="center")
                ws.cell(row=controller,column=4).border = Border(left = Side(border_style = "thin"), right=Side(border_style = "thin"),
                                                                        top=Side(border_style="thin"),bottom=Side(border_style ="thin"))
                ws.cell(row =controller, column=4).font = Font(name='Calibri',size=12)
                ws.cell(row =controller, column=4).value = states[q.state]

                ws.cell(row=controller,column=5).alignment = Alignment(horizontal="center")
                ws.cell(row=controller,column=5).border = Border(left = Side(border_style = "thin"), right=Side(border_style = "thin"),
                                                                        top=Side(border_style="thin"),bottom=Side(border_style ="thin"))
                ws.cell(row =controller, column=5).font = Font(name='Calibri',size=12)       
                ws.cell(row =controller, column=5).value = "Completo" if q.student.dedication==1 else "Parcial" 
                
                ws.cell(row=controller,column=6).alignment = Alignment(horizontal="center")
                ws.cell(row=controller,column=6).border = Border(left = Side(border_style = "thin"), right=Side(border_style = "thin"),
                                                                        top=Side(border_style="thin"),bottom=Side(border_style ="thin"))
                ws.cell(row =controller, column=6).font = Font(name='Calibri',size=12)       
                ws.cell(row =controller, column=6).value = q.student.program.deparment.faculty.institution.name_inst

                ws.cell(row=controller,column=7).alignment = Alignment(horizontal="center")
                ws.cell(row=controller,column=7).border = Border(left = Side(border_style = "thin"), right=Side(border_style = "thin"),
                                                                        top=Side(border_style="thin"),bottom=Side(border_style ="thin"))
                ws.cell(row =controller, column=7).font = Font(name='Calibri',size=12)       
                ws.cell(row =controller, column=7).value = q.student.program.deparment.name 
                controller +=1

            filename = "ReporteInformePorAño.xlsx"
            #The define the type of response to be give
            response = HttpResponse(content_type = "application/ms-excel")
            content = "attachment; filename = {0}".format(filename)
            response["Content-Disposition"] = content
            wb.save(response)

        if(kwargs["type"]==2):#Format pdf request.data["tipo"]==2
            filename = "ReporteInformePorAño.pdf"
            #The define the type of response to be give
            response = HttpResponse(content_type = "application/pdf")
            content = "attachment; filename = {0}".format(filename)
            response["Content-Disposition"] = content
            #Create the PDF object, using the Bytesobject as its "file"
            buffer = BytesIO()
            c = canvas.Canvas(buffer, pagesize=A4)

            #Header
            c.setLineWidth(.3)
            c.setFont('Helvetica',22)
            c.drawString(30,750,'Reporte anual')
            c.setFont('Helvetica',12)
            c.drawString(30,735,'Report')
            c.setFont('Helvetica-Bold',12)
            c.drawString(460,750,str(year))
            c.line(460,747,560,747)

            #Table header
            styles = getSampleStyleSheet()
            styleBH = styles ["Normal"]
            styleBH.alignment = 1 #TA_CENTER is 1
            styleBH.fontSize=10

            codigo = Paragraph('''Codigo''',styleBH)
            nombre = Paragraph('''Nombre''',styleBH)
            estado = Paragraph('''Estado''',styleBH)
            dedicacion = Paragraph('''Dedicación''',styleBH)
            institucion = Paragraph('''Institución''',styleBH)
            departamento = Paragraph('''Departamento''',styleBH)
            data = []
            data.append([codigo, nombre, estado, dedicacion, institucion, departamento])

            #Table
            styleN = styles["BodyText"]
            styleN.alignment = 1 #TA_CENTER is 1
            styleN.fontSize = 7

            high = 650
            for q in queryset: 
                data.append([ q.student.user.personal_code,
                              q.student.user.first_name+" "+q.student.user.last_name,
                              states[q.state],
                              "Completo" if q.student.dedication==1 else "Parcial",
                              q.student.program.deparment.faculty.institution.name_inst,
                              q.student.program.deparment.name])
                high = high -18
            
            #Table zise
            width, height = A4
            table = Table(data, colWidths=[2.7*cm,6.9*cm,2.2*cm,2.2*cm,2.2*cm,2.7*cm])
            table.setStyle(TableStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black),('BOX',(0,0),(-1,-1),0.25,colors.black)]))
            #Pdf size
            table.wrapOn(c, width, height)
            table.drawOn(c,30,high)
            c.showPage()
            
            c.save()
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)           

        return response        

class CreateCountryAPI(generics.GenericAPIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Crear un País, esta función hace uso del metodo POST.
    PATH: 'api/1.0/crear_pais/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    #permission_classes = [IsAuthenticated, IsCoordinator]
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
    #permission_classes = [IsAuthenticated, IsCoordinator]
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
    #permission_classes = [IsAuthenticated, IsCoordinator]
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

class CreateProfessorAPI(generics.GenericAPIView):# toca modificarlo a los cambios nuevos
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Crear un Profesor, esta función hace uso del metodo POST.
    PATH: 'api/1.0/crear_profesor/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    #permission_classes = [IsAuthenticated, IsCoordinator]
    serializer_class = ProfessorSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data) 
        assignedUser = User.objects.get(id=request.data['user'])
        assignedUser.is_proffessor = True
        assignedUser.save()
        if serializer.is_valid():
            professor = serializer.save()              
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
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def get(self, request, *args, **kwargs):
        queryset = Country.objects.filter(status=True)
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
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def get(self, request, *args, **kwargs):
        queryset = Country.objects.filter(id=kwargs["id_country"], status=True)
        returned = CountrySerializer(queryset, many=True).data
        if returned:
            return Response({"Country": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe el País en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = Country.objects.get(id=request.data['id'], status=True)
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
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def get(self, request, *args, **kwargs):
        queryset = State.objects.filter(country=kwargs["id_country"], status=True)
        returned = StateSerializer(queryset, many=True).data
        if returned:
            return Response({"States": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existen Departamentos con ese País en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = State.objects.get(id=request.data['id'], status=True)
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
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def get(self, request, *args, **kwargs):
        queryset = City.objects.filter(state=kwargs["id_dep"], status=True)
        returned = CitySerializer(queryset, many=True).data
        if returned:
            return Response({"Cities": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existen Ciudades con ese Departamento en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = City.objects.get(id=request.data['id'], status=True)
        except City.DoesNotExist:
            return Response(f"No existe esa Ciudad en la base de datos", status=status.HTTP_404_NOT_FOUND)
        
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
        queryset = Institution.objects.filter(status=True, city__state__country__status=True)
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
        queryset = Institution.objects.filter(id=kwargs["id"], status=True) 
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
        queryset = Faculty.objects.filter(status=True)
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
        queryset = Faculty.objects.filter(id=kwargs["id"], status=True)  
        returned = FacultySerializer(queryset, many=True).data
        if returned:
            return Response({"Faculty": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe Facultad en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = Faculty.objects.get(id=request.data['id'], status=True)
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
        queryset = Department.objects.filter(status=True)
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
        queryset = Department.objects.filter(id=kwargs["id"], status=True)  
        returned = DepartmentSerializer(queryset, many=True).data
        if returned:
            return Response({"Department": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe Departamento en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = Department.objects.get(id=request.data['id'], status=True)
        except Department.DoesNotExist:
            return Response(f"No existe Departamento en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class CreateAcademicTrainingAPI(generics.GenericAPIView):
    """
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    API que permite:
    ☠ Crear una Formación Academica, esta función hace uso del metodo POST.
    PATH: 'api/1.0/crear_formacion_academica/'
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    #permission_classes = [IsAuthenticated, IsProfessor]
    serializer_class = AcademicTrainingSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = AcademicTraining.objects.filter(professor=request.data['professor'],degree=request.data['degree'])
            if not(isElement):
                academicTraining = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#endregion

# Create your api's here.
# --------------------------------------------------Jeison

#region Create
# Grupo de investigacion
class CreateInvestigationGroupAPI(generics.GenericAPIView):
    """
    Clase usada para la implementacion de la API para crear un 
    Grupo de Investigacion
    """
    #permission_classes = [IsAuthenticated, IsCoordinator]
    serializer_class = InvestigationGroupSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = InvestigationGroup.objects.filter(name=request.data['name'])
            if not(isElement):
                investigationGroup = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Area del conocimiento
class CreateKnowledgeAreaAPI(APIView):
    """
    Clase usada para la implementacion de la API para crear un 
    Area del Conocimiento
    """
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def post(self, request):
        serializer = KnowledgeAreaSerializer(data = request.data)
        if serializer.is_valid():
            isElement = KnowledgeArea.objects.filter(name=request.data['name'])
            if not(isElement):
                knowledgeArea = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Linea de investigacion
class CreateInvestigationLineAPI(generics.GenericAPIView):
    """
    Clase usada para la implementacion de la API para crear una
    Linea de Investigacion
    """
    #permission_classes = [IsAuthenticated, IsCoordinator]
    serializer_class = InvestigationLineSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = InvestigationLine.objects.filter(name=request.data['name'])
            if not(isElement):
                investigationLine = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Trabaja entre GI y AC
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
                inv_group=request.data['inv_group'], know_area=request.data['know_area'],
                inv_group__status=True, know_area__status=True
            )
            if not(isElement):
                korksInvestGroup = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Dirige entre P y GI
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
                inv_group=request.data['inv_group'], professor=request.data['professor'], 
                professor__status=True, inv_group__status=True, professor__is_director_gi=False
            )
            if not(isElement):
                assignedProfessor = Professor.objects.get(id=request.data['professor'])
                assignedProfessor.is_director_gi = True
                assignedProfessor.save()
                directs = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Es miembro entre P y GI
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
                inv_group=request.data['inv_group'], professor=request.data['professor'],
                professor__status=True, inv_group__status=True
            )
            if not(isElement):
                is_member = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Maneja entre P y LI
class CreateManageInvestLineAPI(generics.GenericAPIView):
    """
    Clase usada para la implementacion de la API para crear una relacion
    de rol Maneja entre los modelos de Profesor y Linea de Investigacion
    """
    serializer_class = ManageInvestLineSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = ManageInvestLine.objects.filter(
                inv_line=request.data['inv_line'], professor=request.data['professor'],
                professor__status=True, inv_line__status=True
            )
            if not(isElement):
                drive = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Labora entre P y Departamento de la U
class CreateWorkDepartmentAPI(generics.GenericAPIView):
    """
    Clase usada para la implementacion de la API para crear una relacion
    de rol Labora entre los modelos de Profesor y Departamento (de la Universidad)
    """
    serializer_class = WorksDepartmSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            isElement = WorksDepartm.objects.filter(
                department=request.data['department'], professor=request.data['professor'],
                professor__status=True, department__status=True
            )
            if not(isElement):
                work = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Director entre profesor y programa
class CreateCoordinatorProgramAPI(generics.GenericAPIView):
    """
    Clase usada para la implementacion de la API para crear una relacion
    de rol coordinador entre los modelos de Profesor y Programa (de la Universidad)
    """
    serializer_class = CoordinatorProgramSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            newCoordinator = Professor.objects.get(id=request.data['professor'])
            userCoordinator = User.objects.get(id=newCoordinator.user.pk)
            userCoordinator.is_coordinator = True
            userCoordinator.save()
            coordinator = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#endregion

#region Consult
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
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def get(self, request, *args, **kwargs):
        queryset = InvestigationGroup.objects.filter(department=kwargs['dep'], status=True)
        return Response({"Groups": InvestigationGroupSerializer(queryset, many=True).data })

class ConsultInvestigationGroup_idAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar y editar un Grupo de Investigacion
    espesifico de la Universidad, esto se logra enviando el ID del Grupo de investigacion mediante 
    el metodo GET y/o enviando la informacion que se va a editar del Grupo de Investigacion mediante
    el metodo PUT
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un grupo de investigacion
    """
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def get(self, request, *args, **kwargs):
        queryset = InvestigationGroup.objects.filter(id=kwargs['id'], status=True)
        
        returned = InvestigationGroupSerializer(queryset, many=True).data
        if returned:
            return Response({"Group": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe el Grupo de investigacion en la base de datos", status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, *args, **kwargs):
        try:
            model = InvestigationGroup.objects.get(id=kwargs['id'], status=True)
        except InvestigationGroup.DoesNotExist:
            return Response(f"No existe el Grupo de investigacion en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = InvestigationGroupSerializer(model, data=request.data)
        if serializer.is_valid():
            if 'status' in request.data.keys():
                if request.data['status'] == False:
                    manageInvLine = ManageInvestGroup.objects.get(inv_group=kwargs['id'], direction_state=True)
                    manageInvLine.direction_state = False
                    oldProfessor = Professor.objects.get(id=manageInvLine.professor.pk, status=True)
                    oldProfessor.is_director_gi = False
                    manageInvLine.save()
                    oldProfessor.save()  
                    isMember = IsMember.objects.filter(inv_group=kwargs['id']) 
                    for reg in isMember: 
                        aux =  IsMember.objects.get(professor = reg.professor, inv_group=reg.inv_group)
                        aux.member_status = False
                        aux.save()

                    isMember = StudentGroupInvestigation.objects.filter(investigation_group=kwargs['id'])
                    for reg in isMember: 
                        aux =  StudentGroupInvestigation.objects.get(student = reg.student, investigation_group=reg.investigation_group)
                        aux.is_active = False
                        aux.save()
                                         
                    
                if request.data['status'] == True:
                    manageInvLine = ManageInvestGroup.objects.get(inv_group=kwargs['id'])
                    manageInvLine.direction_state = True
                    oldProfessor = Professor.objects.get(id=manageInvLine.professor.pk, status=True)
                    oldProfessor.is_director_gi = True                    
                    manageInvLine.save()
                    oldProfessor.save()  
                    isMember = IsMember.objects.filter(inv_group=kwargs['id']) 
                    for reg in isMember: 
                        aux =  IsMember.objects.get(professor = reg.professor, inv_group=reg.inv_group)
                        aux.member_status = True
                        aux.save() 

                    isMember = StudentGroupInvestigation.objects.filter(investigation_group=kwargs['id'])
                    for reg in isMember: 
                        aux =  StudentGroupInvestigation.objects.get(student = reg.student, investigation_group=reg.investigation_group)
                        aux.is_active = True
                        aux.save()

            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultProfessorAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar todos los Profesores
    registrados en la Universidad
    """
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def get(self, request, *args, **kwargs):
        queryset = Professor.objects.filter(status=True)
        return Response({"Professors": ProfessorSerializer(queryset, many=True).data })

class ConsultProfessor_idAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar y editar un Profesor espesifico
    de la Universidad, esto se logra enviando el ID del Profesor mediante el metodo GET y/o enviando
    la informacion que se va a editar del Profesor mediante el metodo PUT
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un profesor
    """
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def get(self, request, *args, **kwargs):
        queryset = Professor.objects.filter(id=kwargs['id'], status=True)

        returned = ProfessorSerializer(queryset, many=True).data
        if returned:
            return Response({"Professor": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe el Profesor en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = Professor.objects.get(id=kwargs['id'], status=True)
        except Professor.DoesNotExist:
            return Response(f"No existe el Profesor en la base de datos", status=status.HTTP_404_NOT_FOUND)

        serializer = ProfessorSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultProfessor_userAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar un Profesor espesifico
    de la Universidad, esto se logra enviando el ID del Usuario asigano al Profesor mediante 
    el metodo GET
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un Usuario
    """
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def get(self, request, *args, **kwargs):
        queryset = Professor.objects.filter(user=kwargs['id'], status=True)

        returned = ProfessorSerializer(queryset, many=True).data
        if returned:
            return Response({"Professor": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe el Profesor en la base de datos", status=status.HTTP_404_NOT_FOUND)


class ConsultKnowledgeAreaAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar todas las Areas del Conocimiento 
    registradas en la Universidad
    """
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def get(self, request, *args, **kwargs):
        queryset = KnowledgeArea.objects.filter(status=True)
        return Response({"Knowledges": KnowledgeAreaSerializer(queryset, many=True).data })

class ConsultKnowledgeArea_idAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar y editar un Area del Conocimiento espesifica
    de la Universidad, esto se logra enviando el ID del Area del Conocimiento mediante el metodo GET y/o enviando
    la informacion que se va a editar del Area del Conocimiento mediante el metodo PUT
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un Area del Conocimiento
    """
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def get(self, request, *args, **kwargs):
        queryset = KnowledgeArea.objects.filter(id=kwargs['id'], status=True)
        returned = KnowledgeAreaSerializer(queryset, many=True).data
        if returned:
            return Response({"Knowledge": KnowledgeAreaSerializer(queryset, many=True).data })
        else:
            return Response(f"No existe el Area de conocimiento en la base de datos...")

    def put(self, request, *args, **kwargs):
        try:
            model = KnowledgeArea.objects.get(id=kwargs['id'], status=True)
        except KnowledgeArea.DoesNotExist:
            return Response(f"No existe el Area de conocimiento en la base de datos...")
        
        serializer = KnowledgeAreaSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultInvestigationLine_knowledgeAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar todas las Lineas de Investigacion que
    pertenecen a un Area del conocimiento espesifica
    """
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def get(self, request, *args, **kwargs):
        queryset = InvestigationLine.objects.filter(know_area=kwargs['id_area'], status=True)
        returned = InvestigationLineSerializer(queryset, many=True).data
        if returned:
            return Response({"Lines": InvestigationLineSerializer(queryset, many=True).data })
        else:
            return Response(f"No existen Lineas de Investigacion asociadas a esa Area del conocimiento...")

class ConsultInvestigationLine_idAPI(APIView):
    """
    Clase usada para la implementacion de la API para consultar una Linea de Investigacion espesifica 
    de la Universidad, esto se logra enviando el ID de la Linea de Investigacion mediante el metodo GET 
    y/o enviando la informacion que se va a editar de la Linea de Investigacion mediante el metodo PUT
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a una Linea de Investigacion
    """
    #permission_classes = [IsAuthenticated, IsCoordinator]
    def get(self, request, *args, **kwargs):
        queryset = InvestigationLine.objects.filter(id=kwargs['id'], status=True)
        returned = InvestigationLineSerializer(queryset, many=True).data
        if returned:
            return Response({"Line": InvestigationLineSerializer(queryset, many=True).data })
        else:
            return Response(f"No existe la Linea de investigacion en la base de datos...")

    def put(self, request, *args, **kwargs):
        try:
            model = InvestigationLine.objects.get(id=kwargs['id'], status=True)
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
    que se va a editar del registro del modelo "Es Miembro" mediante el metodo PUT
    - - - - -
    Parameters
    - - - - -
    id_p : int
        Referencia a un Profesor
    id_gi : int
        Referencia a un Grupo de Investigacion
    """
    def get(self, request, *args, **kwargs):
        queryset = IsMember.objects.filter(inv_group=kwargs['id_gi'], professor=kwargs['id_p'], member_status=True)
        returned = IsMemberSerializer(queryset, many=True).data
        if returned:
            return Response({"IsMember":returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, *args, **kwargs):
        try:
            model = IsMember.objects.get(inv_group=kwargs['id_gi'], professor=kwargs['id_p'], member_status=True)
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
    que se va a editar del registro del modelo "Trabaja" mediante el metodo PUT
    - - - - -
    Parameters
    - - - - -
    id_gi : int
        Referencia a un Grupo de Investigacion
    id_ac : int
        Referencia a un Area del Conocimiento
    """
    def get(self, request, *args, **kwargs):
        queryset = WorksInvestGroup.objects.filter(inv_group=kwargs['id_gi'], know_area=kwargs['id_ac'], study_status=True)
        returned = WorksInvestGroupSerializer(queryset, many=True).data
        if returned:
            return Response({"Work":returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, *args, **kwargs):
        try:
            model = WorksInvestGroup.objects.get(inv_group=kwargs['id_gi'], know_area=kwargs['id_ac'], study_status=True)
        except IsMember.DoesNotExist:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)

        serializer = WorksInvestGroupSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultWorksInvestGroup_GIAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = WorksInvestGroup.objects.filter(inv_group=kwargs['id'], study_status=True)
        returned = WorksInvestGroupSerializer(queryset, many=True).data
        if returned:
            return Response({"Work":returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)

class ConsultManageInvestGroupAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar si un Profesor DIRIGE o no un
    Grupo de Investigacion espesifico de la Universidad, esto se logra enviando el ID del usuario del Profesor y 
    el ID del Grupo de Investigacion (en ese orden) mediante el metodo GET y/o enviando la informacion 
    que se va a editar del registro del modelo "Dirige" mediante el metodo PUT
    - - - - -
    Parameters
    - - - - -
    id_p : int
        Referencia a un Profesor
    id_gi : int
        Referencia a un Grupo de Investigacion
    """
    def get(self, request, *args, **kwargs):
        queryset = ManageInvestGroup.objects.filter(inv_group=kwargs['id_gi'], professor=kwargs['id_p'], direction_state=True)
        returned = ManageInvestGroupSerializer(queryset, many=True).data
        if returned:
            return Response({"Manage":returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, *args, **kwargs):
        try:
            model = ManageInvestGroup.objects.get(inv_group=kwargs['id_gi'], professor=kwargs['id_p'], direction_state=True)
        except IsMember.DoesNotExist:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)

        serializer = ManageInvestGroupSerializer(model, data=request.data)
        if serializer.is_valid():
            if 'professor' in request.data.keys():
                oldProfessor = Professor.objects.get(id=kwargs['id_p'])
                oldProfessor.is_director_gi = False
                oldProfessor.save()
                newProfessor = Professor.objects.get(id=request.data['professor'])
                newProfessor.is_director_gi = True
                newProfessor.save()
            if 'status' in request.data.keys():
                if request.data['status'] == False:
                    oldProfessor = Professor.objects.get(id=kwargs['id_p'])
                    oldProfessor.is_director_gi = False
                    oldProfessor.save()
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

class ConsultManageInvestGroup_GIAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar cual es el profesor que DIRIGE a un grupo de
    investigacion de la Universidad, esto se logra enviando el ID del Grupo de Investigacion mediante el metodo GET
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un Grupo de investigacion
    - - - - -
    Returned
    - - - - -
        Si el id es correcto y se encuentran resultados:
            {"Manage": JsonResultado, HTTP_202_ACCEPTED}}
        Si no se encuentran resultados:
            Se mostrata un mensaje de error, HTTP_404_NOT_FOUND
    """
    def get(self, request, *args, **kwargs):
        queryset = ManageInvestGroup.objects.filter(inv_group=kwargs['id'], direction_state=True)
        returned = ManageInvestGroupSerializer(queryset, many=True).data
        if returned:
            return Response({"Manage": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existen registros en la base de datos para el ID ingresado", status=status.HTTP_404_NOT_FOUND)

#maneja
class ConsultManageInvestLineAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar si un Profesor MANEJA o no una
    Linea de investigacion espesifica, esto se logra enviando el ID del Profesor y el ID de la 
    Linea de investigacion (en ese orden) mediante el metodo GET y/o enviando la informacion
    que se va a editar del registro del modelo "maneja" mediante el metodo PUT
    - - - - -
    Parameters
    - - - - -
    id_p : int
        Referencia a un Profesor
    id_i : int
        Referencia a una Linea de Investigacion de la Universidad
    """
    def get(self, request, *args, **kwargs):
        queryset = ManageInvestLine.objects.filter(inv_line=kwargs['id_i'], professor=kwargs['id_p'], analysis_state=True)
        returned = ManageInvestLineSerializer(queryset, many=True).data
        if returned:
            return Response(returned, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, *args, **kwargs):
        try:
            model = ManageInvestLine.objects.filter(inv_line=kwargs['id_i'], professor=kwargs['id_p'], analysis_state=True)
        except ManageInvestLine.DoesNotExist:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)
        
        serializer = ManageInvestLineSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultManageInvestLine_invLineAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar cuales Profesores MANEJAN una
    Linea de Investigacion, esto se logra enviando el ID de la Linea de Investigacion mediante el metodo GET 
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a una Linea de Investigacion
    """
    def get(self, request, *args, **kwargs):
        queryset = ManageInvestLine.objects.filter(inv_line=kwargs['id'], analysis_state=True)
        returned = ManageInvestLineSerializer(queryset, many=True).data
        if returned:
            return Response(returned, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)

class ConsultManageInvestLine_profAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar si un Profesor MANEJA una o mas
    Lineas de Investigacion, esto se logra enviando el ID del Profesor mediante el metodo GET 
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un Profesor
    """
    def get(self, request, *args, **kwargs):
        queryset = ManageInvestLine.objects.filter(professor=kwargs['id'], analysis_state=True)
        returned = ManageInvestLineSerializer(queryset, many=True).data
        if returned:
            return Response(returned, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)

# labora
class ConsultWorksDepartmAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar si un Profesor LABORA o no un
    Departamento espesifico de la Universidad, esto se logra enviando el ID del Profesor y 
    el ID del Departamento (en ese orden) mediante el metodo GET y/o enviando la informacion 
    que se va a editar del registro del modelo "Labora" mediante el metodo PUT
    - - - - -
    Parameters
    - - - - -
    id_p : int
        Referencia a un Profesor
    id_d : int
        Referencia a un Departamento de la Universidad
    """
    def get(self, request, *args, **kwargs):
        queryset = WorksDepartm.objects.filter(professor=kwargs['id_p'], department=kwargs['id_d'], laboral_state=True)
        returned = WorksDepartmSerializer(queryset, many=True).data
        if returned:
            return Response(returned, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, *args, **kwargs):
        try:
            model = WorksDepartm.objects.filter(professor=kwargs['id_p'], department=kwargs['id_d'], laboral_state=True)
        except WorksDepartm.DoesNotExist:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)
        
        serializer = WorksDepartmSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultWorksDepartm_profAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar si un Profesor LABORA o no un
    Departamento de la Universidad, esto se logra enviando el ID del Profesor mediante el metodo GET 
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un Profesor
    """
    def get(self, request, *args, **kwargs):
        queryset = WorksDepartm.objects.filter(professor=kwargs['id'], laboral_state=True)
        returned = WorksDepartmSerializer(queryset, many=True).data
        if returned:
            return Response(returned, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)

class ConsultWorksDepartm_depAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar cuales Profesores LABORAN en un
    Departamento espesifico de la Universidad, esto se logra enviando el ID del Departamento mediante
    el metodo GET 
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un Departamento de la Universidad
    """
    def get(self, request, *args, **kwargs):
        queryset = WorksDepartm.objects.filter(department=kwargs['id'], laboral_state=True)
        returned = WorksDepartmSerializer(queryset, many=True).data
        if returned:
            return Response(returned, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)

# Formacion academica
class ConsultAcademicTrainingAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar la FORMACION ACADEMICA de un
    Profesor espesifico de la Universidad, esto se logra enviando el ID de la Formacion Academica
    correspondiente mediante el metodo GET y/o enviando la informacion que se va a editar del
    registro del modelo "Formacion academica" mediante el metodo PUT
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a una Formacion academica (Primary key del registro de la tabla)
    """
    def get(self, request, *args, **kwargs):
        queryset = AcademicTraining.objects.filter(id=kwargs['id'], professor__status=True)
        returned = AcademicTrainingSerializer(queryset, many=True).data
        if returned:
            return Response(returned, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = AcademicTraining.objects.get(id=kwargs['id'], professor__status=True)
        except AcademicTraining.DoesNotExist:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)
        
        serializer = AcademicTrainingSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsultAcademicTraining_profAPI(APIView):
    """
    Clase usada para la implementacion de, la API para consultar las FORMACIONES ACADEMICAS de un
    Profesor de la Universidad, esto se logra enviando el ID del Profesor mediante el metodo GET 
    - - - - -
    Parameters
    - - - - -
    id : int
        Referencia a un Profesor
    """
    def get(self, request, *args, **kwargs):
        queryset = AcademicTraining.objects.filter(professor=kwargs['id'], professor__status=True)
        returned = AcademicTrainingSerializer(queryset, many=True).data
        if returned:
            return Response(returned, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)

# Coordinador
class ConsultCoordinatorAPI(APIView):
    # consultar por cuales campos para la edicion
    def get(self, request, *args, **kwargs):
        queryset = CoordinatorProgram.objects.filter(program=kwargs['prog'], academic_period=kwargs['period'])
        returned = CoordinatorProgramSerializer(queryset, many=True).data
        if returned:
            return Response(returned, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            model = CoordinatorProgram.objects.get(program=kwargs['prog'], academic_period=kwargs['period'])
        except AcademicTraining.DoesNotExist:
            return Response(f"No existe un registro en la base de datos para los datos ingresados", status=status.HTTP_404_NOT_FOUND)
        
        serializer = CoordinatorProgramSerializer(model, data=request.data)
        if serializer.is_valid():
            if 'status' in request.data.keys():
                if request.data['is_active'] == False:
                    coordinator = Professor.objects.get(id=request.data['professor'])
                    userCoordinator = User.objects.get(id=coordinator.user.pk)
                    userCoordinator.is_coordinator = False
                    userCoordinator.save()
            model.date_update = datetime.datetime.now()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#endregion
