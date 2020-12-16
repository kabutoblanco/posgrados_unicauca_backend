from rest_framework import viewsets, generics, views
from rest_framework.response import Response
from .models import *
from .serializers import *
from a_students_app.models import StudentProfessor
from .backends import IsDirector, IsCoordinador
from django.db.models import Avg, Sum, Count, Q
from rest_framework.permissions import IsAuthenticated
from .email import send_email
from django.views.generic.base import TemplateView
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from django.http.response import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

from django.db.models import Avg, Sum, Count

# - - - - - PRIMER SPRINT - - - - -
class StudentAPI(views.APIView):
    """
    API usada para retornar un estudiante con fecha y estado del último cohorte de matricula
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    """

    # permission_classes = (IsAuthenticated, )
    serializer_class = EnrrollmentSerializer

    def get(self, request, *args, **kwargs):
        queryset = Enrrollment.objects.filter(
            student__user=kwargs['id_student']).order_by('-period')[:1]
        try:
            return Response({"student": EnrrollmentSerializer(queryset[0]).data})
        except:
            return Response({"student": []})


class StudentListAPI(generics.RetrieveAPIView):
    """
    API usada para retornar la lista de estudiantes con fecha y estado del último cohorte de matricula
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    """

    # permission_classes = (IsAuthenticated, )
    serializer_class = EnrrollmentSerializer

    def get(self, request, *args, **kwargs):
        queryset = Student.objects.filter(is_active=True)
        queryset_list = Enrrollment.objects.none()
        for student in queryset:
            queryset_list = queryset_list | Enrrollment.objects.filter(
                student__user=student.user).order_by('-period')[:1]
        return Response({"students": EnrrollmentSerializer(queryset_list, many=True).data})


class TrackingAPI(viewsets.ModelViewSet):
    """
    API usada para gestionar el modelo de Tracking
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    IsCoordinator
        El usuario debe tener a cargo al menos una actividad como coordinator
    """

    # permission_classes = [IsAuthenticated, (IsDirector | IsCoordinador)]
    serializer_class = TrackingSerializer
    queryset = Tracking.objects.all()


class ActivityAPI(generics.RetrieveAPIView):
    """
    API usada para obtener una actividad por id
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    """

    # permission_classes = [IsAuthenticated]
    serializer_class = ActivitySerializer

    def get(self, request, *args, **kwargs):
        queryset = Activity.objects.get(id=kwargs['id'])
        return Response({"activity": ActivitySerializer(queryset[0]).data})


class ActivityListStudentAPI(generics.RetrieveAPIView):
    """
    API usada para filtrar los registros del modelo Activity por estudiante
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    IsCoordinator
        El usuario debe tener a cargo al menos una actividad como coordinator
    """

    # permission_classes = [IsAuthenticated, (IsDirector | IsCoordinador)]
    serializer_class = ActivitySerializer

    def get(self, request, *args, **kwargs):
        queryset = Activity.objects.filter(
            is_active=True, student__user=kwargs['id_student'])
        return Response({"activities": ActivitySerializer(queryset, many=True).data})
# - - - - - PRIMER SPRINT - - - - -


# - - - - - SEGUNDO SPRINT - - - - -
class DirectorStudentsAPI(generics.RetrieveAPIView):
    """
    API usada para obtener los estudiantes que un director tiene a cargo
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    IsCoordinator
        El usuario debe tener a cargo al menos una actividad como coordinator
    """

    # permission_classes = (IsAuthenticated, IsDirector)
    serializer_class = EnrrollmentSerializer

    def get(self, request, *args, **kwargs):
        queryset = StudentProfessor.objects.filter(
            is_active=True, professor__user=kwargs['id_professor']).values('student')
        list = [e['student'] for e in queryset]
        queryset = Student.objects.filter(is_active=True, id__in=list)
        queryset_list = Enrrollment.objects.none()
        for student in queryset:
            queryset_list = queryset_list | Enrrollment.objects.filter(
                student__user=student.user.id).order_by('-period')[:1]
        return Response({"students": EnrrollmentSerializer(queryset_list, many=True).data})


class DirectorActiviesAPI(generics.RetrieveAPIView):
    """
    API usada para obtener las actividades que un director tiene de los estudiantes a cargo
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    """

    # permission_classes = (IsAuthenticated, IsDirector)
    serializer_class = ActivitySerializer

    def get(self, request, *args, **kwargs):
        queryset = ActivityProfessor.objects.filter(Q(rol=1) | Q(rol=2))
        queryset = queryset.filter(
            is_active=True, professor__user=kwargs['id_professor'], ).values('activity')
        list = [e['activity'] for e in queryset]
        queryset_list = Activity.objects.filter(
            is_active=True, id__in=list)
        return Response({"activities": ActivitySerializer(queryset_list, many=True).data})


class CoordinatorActivitiesAPI(generics.RetrieveAPIView):
    """
    API usada para obtener las actividades que un coordinador tiene a cargo
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    IsCoordinator
        El usuario debe tener a cargo al menos una actividad como coordinator
    """

    # permission_classes = (IsAuthenticated, IsCoordinador)
    serializer_class = ActivitySerializer

    def intersection(self, lst1, lst2):
        temp = set(lst2)
        lst3 = [value for value in lst1 if value in temp]
        return lst3

    def get(self, request, *args, **kwargs):
        queryset = ActivityProfessor.objects.filter(
            is_active=True, professor__user=kwargs['id_professor'], rol=3).values('activity')
        list = [e['activity'] for e in queryset]
        queryset_1 = TestDirector.objects.filter(
            is_active=True, activity__in=list).values('activity')[:1]
        print(list)
        list_1 = [e['activity'] for e in queryset_1]
        list = self.intersection(list, list_1)
        queryset_list = Activity.objects.filter(is_active=True, id__in=list)
        return Response({"activities": ActivitySerializer(queryset_list, many=True).data})
# - - - - - SEGUNDO SPRINT - - - - -


# - - - - - TERCER SPRINT - - - - -
class TestDirectorAPI(viewsets.ModelViewSet):
    """
    API usada para gestionar el modelo de TestDirector
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    """

    # permission_classes = [IsAuthenticated, IsDirector]
    serializer_class = TestDirectorSerializer
    queryset = TestDirector.objects.all()


class TestCoordinatorAPI(viewsets.ModelViewSet):
    """
    API usada para gestionar el modelo de TestCoordinator
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsCoordinator
        El usuario debe tener a cargo al menos una actividad como coordinator
    """

    # permission_classes = [IsAuthenticated, IsCoordinador]
    serializer_class = TestCoordinatorSerializer
    queryset = TestCoordinator.objects.all()


class TestDirectorListAPI(generics.RetrieveAPIView):
    """
    API usada para obtener todas las evaluaciones de un director
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    """

    # permission_classes = [IsAuthenticated, IsDirector]
    serializer_class = TestDirectorSerializer

    def get(self, request, *args, **kwargs):
        print(kwargs['id_professor'])
        queryset = TestDirector.objects.filter(
            is_active=True, director__user=kwargs['id_professor'])
        return Response({"test_activities": TestDirectorSerializer(queryset, many=True).data})


class TestCoordinatorListAPI(generics.RetrieveAPIView):
    """
    API usada para obtener todas las evaluaciones de un coordinador
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsCoordinator
        El usuario debe tener a cargo al menos un estudiante como coordinador
    """

    # permission_classes = [IsAuthenticated, IsCoordinador]
    serializer_class = TestCoordinatorSerializer

    def get(self, request, *args, **kwargs):
        queryset = TestCoordinator.objects.filter(
            is_active=True, coordinator__user=kwargs['id_professor'])
        return Response({"test_activities": TestCoordinatorSerializer(queryset, many=True).data})
# - - - - - TERCER SPRINT - - - - -


class ReportAPI(TemplateView):
    def get(self, request, *args, **kwargs):
        queryset = Student.objects.filter(is_active=True)
        queryset_list1 = Enrrollment.objects.none()
        for student in queryset:
            queryset_list1 = queryset_list1 | Enrrollment.objects.filter(state=1).values('period').annotate(enrrollment=Count('state')).order_by('period')
        print(queryset_list1)
        queryset_list2 = Enrrollment.objects.none()
        for student in queryset:
            queryset_list2 = queryset_list2 | Enrrollment.objects.filter(state=3).values('period').annotate(enrrollment=Count('state')).order_by('period')
        print(queryset_list2)
        queryset_list3 = Enrrollment.objects.all().values('period').annotate(period_i=Count('period')).order_by('period')
        print(queryset_list3)
        cohorte_list = []
        for period in queryset_list3:
            cohorte = {"period": None, "enrrollment": 0, "graduate": 0}
            cohorte["period"] = period["period"]
            for enrrollment in queryset_list1:
                if enrrollment["period"] == cohorte["period"]:
                    cohorte["enrrollment"] = enrrollment["enrrollment"]
                    break
            for graduate in queryset_list2:
                if graduate["period"] == cohorte["period"]:
                    cohorte["graduate"] = graduate["enrrollment"]
                    break
            cohorte_list.append(cohorte)
        print(cohorte_list)
            
        if(kwargs["type"] == 1):
            wb = Workbook()
            count = 3
            ws = wb.active
            ws.title = 'Hoja 1'
            #Create title in the sheet
            ws['A1'].alignment = Alignment(horizontal="center", vertical="center")
            ws['A1'].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"), top = Side(border_style="thin"), bottom=Side(border_style="thin"))
            ws['A1'].fill = PatternFill(start_color='66FFCC', end_color='66FFCC', fill_type='solid')
            ws['A1'].font = Font(name='Calibri', size=14, bold=True)
            ws['A1'] = "INFORME POR COHORTE"
            #Change the characteristics of cells
            ws.merge_cells('A1:E1')
            ws.row_dimensions[1].height = 25
            ws.column_dimensions['A'].width = 10
            ws.column_dimensions['B'].width = 20
            ws.column_dimensions['C'].width = 20
            ws.column_dimensions['D'].width = 20
            ws.column_dimensions['E'].width = 20
            #Create header
            ws['A2'].alignment = Alignment(horizontal="center", vertical="center")
            ws['A2'].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"), top = Side(border_style="thin"), bottom=Side(border_style ="thin"))
            ws['A2'].fill = PatternFill(start_color='66CFCC', end_color='66CFCC', fill_type='solid')
            ws['A2'].font = Font(name='Calibri', size=12, bold=True)
            ws['A2']='No.'

            ws['B2'].alignment = Alignment(horizontal="center", vertical="center")
            ws['B2'].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"), top = Side(border_style="thin"), bottom=Side(border_style ="thin"))
            ws['B2'].fill = PatternFill(start_color='66CFCC', end_color='66CFCC', fill_type='solid')
            ws['B2'].font = Font(name='Calibri', size=12, bold=True)
            ws['B2']='Cohorte'

            ws['C2'].alignment = Alignment(horizontal="center", vertical="center")
            ws['C2'].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"), top = Side(border_style="thin"), bottom=Side(border_style ="thin"))
            ws['C2'].fill = PatternFill(start_color='66CFCC', end_color='66CFCC', fill_type='solid')
            ws['C2'].font = Font(name='Calibri', size=12, bold=True)
            ws['C2']='No. Matriculados'

            ws['D2'].alignment = Alignment(horizontal="center", vertical="center")
            ws['D2'].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"), top = Side(border_style="thin"), bottom=Side(border_style ="thin"))
            ws['D2'].fill = PatternFill(start_color='66CFCC', end_color='66CFCC', fill_type='solid')
            ws['D2'].font = Font(name='Calibri', size=12, bold=True)
            ws['D2']='No. Graduados'

            ws['E2'].alignment = Alignment(horizontal="center", vertical="center")
            ws['E2'].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"), top = Side(border_style="thin"), bottom=Side(border_style ="thin"))
            ws['E2'].fill = PatternFill(start_color='66CFCC', end_color='66CFCC', fill_type='solid')
            ws['E2'].font = Font(name='Calibri', size=12, bold=True)
            ws['E2']='% Graduados'

            for q in cohorte_list:
                ws.cell(row=count, column=1).alignment = Alignment(horizontal="center")
                ws.cell(row=count, column=1).border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"), top=Side(border_style="thin"), bottom=Side(border_style ="thin"))
                ws.cell(row=count, column=1).font = Font(name='Calibri', size=12)       
                ws.cell(row=count, column=1).value = count - 2

                ws.cell(row=count, column=2).alignment = Alignment(horizontal="center")
                ws.cell(row=count, column=2).border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"), top=Side(border_style="thin"), bottom=Side(border_style ="thin"))
                ws.cell(row=count, column=2).font = Font(name='Calibri', size=12)       
                ws.cell(row=count, column=2).value = q["period"]

                ws.cell(row=count, column=3).alignment = Alignment(horizontal="center")
                ws.cell(row=count, column=3).border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"), top=Side(border_style="thin"), bottom=Side(border_style ="thin"))
                ws.cell(row=count, column=3).font = Font(name='Calibri', size=12)       
                ws.cell(row=count, column=3).value = q["enrrollment"]

                ws.cell(row=count, column=4).alignment = Alignment(horizontal="center")
                ws.cell(row=count, column=4).border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"), top=Side(border_style="thin"), bottom=Side(border_style ="thin"))
                ws.cell(row=count, column=4).font = Font(name='Calibri', size=12)       
                ws.cell(row=count, column=4).value = q["graduate"]

                ws.cell(row=count, column=5).alignment = Alignment(horizontal="center")
                ws.cell(row=count, column=5).border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"), top=Side(border_style="thin"), bottom=Side(border_style ="thin"))
                ws.cell(row=count, column=5).font = Font(name='Calibri', size=12)       
                ws.cell(row=count, column=5).value = str((int(q["graduate"]) / (int(q["graduate"]) + int(q["enrrollment"]))) * 100) + "%"

                count += 1

            #Name file
            filename = "reporte_cohortes.xlsx"
            #The define the type of response to be give
            response = HttpResponse(content_type = "application/ms-excel")
            content = "attachment; filename = {0}".format(filename)
            response["Content-Disposition"] = content
            wb.save(response)

        if(kwargs["type"]==2):#Format pdf request.data["tipo"]==2
            filename = "reporte_cohortes.pdf"
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
            c.drawString(30,750,'Reporte por cohorte')
            c.setFont('Helvetica',12)
            c.drawString(30,735, 'Report')
            c.setFont('Helvetica-Bold',12)
            c.drawString(460,750, ' cohorte')
            c.line(460,747,560,747)

            #Table header
            styles = getSampleStyleSheet()
            styleBH = styles ["Normal"]
            styleBH.alignment = 1 #TA_CENTER is 1
            styleBH.fontSize=10

            codigo = Paragraph('''No.''',styleBH)
            cohorte = Paragraph('''Cohorte''',styleBH)
            no_matriculados = Paragraph('''No. Matriculados''',styleBH)
            no_graduados = Paragraph('''No. Graduados''',styleBH)
            por_matriculados = Paragraph('''% Matriculados''',styleBH)
            data = []
            data.append([codigo, cohorte, no_matriculados, no_graduados, por_matriculados])

            #Table
            styleN = styles["BodyText"]
            styleN.alignment = 1 #TA_CENTER is 1
            styleN.fontSize = 7

            high = 650
            count = 1
            for q in cohorte_list:
                data.append([ count,
                              q["period"],
                              q["enrrollment"],
                              q["graduate"],
                              str((int(q["graduate"]) / (int(q["graduate"]) + int(q["enrrollment"]))) * 100) + "%"
                            ])
                high = high -18
                count += 1
            
            #Table zise
            width, height = A4
            table = Table(data, colWidths=[2.7*cm,2.2*cm,5*cm,5*cm,4*cm])
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
        
