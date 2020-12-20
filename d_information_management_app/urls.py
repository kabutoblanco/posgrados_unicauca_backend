#General
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

#Javier
# from .views import consultarPais,crearDepartamento, crearCiudad, CrearPais
# from d_information_management_app.views import Home
#-------------------------------------------------

#Jeison
from .api import *

router = DefaultRouter()

router.register('country', CountryAPI) # Incluye crear, deditar y consultar todos los paises
router.register('professor', ProfessorAPI) # Incluye crear, deditar y consultar todos los paises
router.register('state', StateAPI)
router.register('city', CityAPI)
router.register('institution', InstitutionAPI)
router.register('faculty', FacultyAPI)
router.register('department_u', DepartmentAPI)
router.register('academic_training', AcademicTrainingAPI)
router.register('knowledge_area', KnowledgeAreaAPI)
router.register('investigation_group', InvestigationGroupAPI)
router.register('investigation_line', InvestigationLineAPI)

urlpatterns = [
    #Javier
    #Crear
    path('api/', include(router.urls)),
    path('api/1.0/report/<int:year>/<int:type>', ReportTest.as_view()),
    #Consultar
    path('api/1.0/consultar_pais/', ConsultCountryAPI.as_view()),
    path('api/1.0/consultar_departamento_pais/<int:id_country>', ConsultState_CountryAPI.as_view()),
    path('api/1.0/full_consultar_departamento_pais/<int:id_country>', FullConsultState_CountryAPI.as_view()),
    path('api/1.0/consultar_ciudad_departamento/<int:id_dep>', ConsultCity_StateAPI.as_view()),
    path('api/1.0/full_consultar_ciudad_departamento/<int:id_dep>', FullConsultCity_StateAPI.as_view()),
    path('api/1.0/consultar_institucion/', ConsultInstitutionAPI.as_view()),
    path('api/1.0/consultar_facultad/', ConsultFacultyAPI.as_view()),
    path('api/1.0/consultar_departamentoU/', ConsultDepartmentAPI.as_view()),
    #Jeison
    #Crear
    path('api/1.0/crear_trabaja/', CreateWorksInvestGroupAPI.as_view()),
    path('api/1.0/crear_dirige/', CreateManageInvestGroupAPI.as_view()),
    path('api/1.0/crear_maneja/', CreateManageInvestLineAPI.as_view()),
    path('api/1.0/create_is_member/', CreateIsMemberAPI.as_view()),
    path('api/1.0/crear_labora/', CreateWorkDepartmentAPI.as_view()),
    path('api/1.0/crear_coordinador/', CreateCoordinatorProgramAPI.as_view()),
    #Consultar
    path('api/1.0/consultar_gi_ins/<int:id>', ConsultInvestigationGroup_InstAPI.as_view()),
    path('api/1.0/consultar_gi_dep/<int:dep>', ConsultInvestigationGroup_DepartmentAPI.as_view()),
    path('api/1.0/consultar_area_conocimiento/', ConsultKnowledgeAreaAPI.as_view()),
    path('api/1.0/consultar_li_area/<int:id_area>', ConsultInvestigationLine_knowledgeAPI.as_view()),
    # Profesor
    path('api/1.0/profesor_director_gi/', ConsultProfessorDirectorGIAPI.as_view()),
    path('api/1.0/profesor_director_s/', ConsultProfessorDirectorStudentAPI.as_view()),
    path('api/1.0/profesor_coodirector_planta/', ConsultProfessorCoodirectorPlantaAPI.as_view()),
    path('api/1.0/consultar_profesor/', ConsultProfessorAPI.as_view()),
    path('api/1.0/consultar_profesor_user/<int:id>', ConsultProfessor_userAPI.as_view()),
    # Es miembro
    path('api/1.0/consultar_es_miembro/<int:id_p>/<int:id_gi>', ConsultIsMemberAPI.as_view()), # ya esta editar es miembro (P-GI)
    path('api/1.0/consultar_miembro_gi/<int:id>', ConsultMemberIGAPI.as_view()),
    path('api/1.0/consultar_miembro_p/<int:id>', ConsultMemberProfessorAPI.as_view()),
    # Trabaja entre GI y AC
    path('api/1.0/consultar_trabaja/<int:id_gi>/<int:id_ac>', ConsultWorksInvestGroupAPI.as_view()), # ya esta editar trabaja (GI-AC)
    path('api/1.0/consultar_trabaja/<int:id>', ConsultWorksInvestGroup_GIAPI.as_view()),
    # Dirige entre Pfr y GI
    path('api/1.0/consultar_dirige/<int:id_p>/<int:id_gi>', ConsultManageInvestGroupAPI.as_view()), # ya esta editar dirige (P-GI)
    path('api/1.0/consultar_dirige_d/<int:id>', ConsultManageInvestGroup_DirecAPI.as_view()),
    path('api/1.0/consultar_dirige_gi/<int:id>', ConsultManageInvestGroup_GIAPI.as_view()),
    # Maneja entre Prf e IL
    path('api/1.0/consultar_maneja/<int:id_p>/<int:id_i>', ConsultManageInvestLineAPI.as_view()), # ya esta editar maneja (P-D)
    path('api/1.0/consultar_maneja_li/<int:id>', ConsultManageInvestLine_invLineAPI.as_view()),
    path('api/1.0/consultar_maneja_p/<int:id>', ConsultManageInvestLine_profAPI.as_view()),
    # Labora entre Prf y Dep
    path('api/1.0/consultar_labora/<int:id_p>/<int:id_d>', ConsultWorksDepartmAPI.as_view()), # ya esta editar labora (P-D)
    path('api/1.0/consultar_labora_p/<int:id>', ConsultWorksDepartm_profAPI.as_view()),
    path('api/1.0/consultar_labora_d/<int:id>', ConsultWorksDepartm_depAPI.as_view()),
    # Coordinador entre Prf y Programa  
    path('api/1.0/consultar_coordinador/<int:prog>/<str:period>', ConsultCoordinatorAPI.as_view()),

]