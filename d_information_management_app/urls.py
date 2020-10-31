#General
from django.urls import path, include

#Javier
# from .views import consultarPais,crearDepartamento, crearCiudad, CrearPais
# from d_information_management_app.views import Home
#-------------------------------------------------

#Jeison
from .api import (CreateCountryAPI, CreateStateAPI, CreateCityAPI, CreateInstitutionAPI, CreateProfessorAPI,
                 CreateFacultyAPI, CreateDepartmentAPI, CreateAcademicTrainingAPI, CreateWorksInvestGroupAPI, 
                 CreateManageInvestLineAPI, CreateManageInvestGroupAPI, ConsultCountryAPI, ConsultState_CountryAPI, 
                 ConsultCity_StateAPI, ConsultInstitutionAPI, ConsultInstitution_idAPI, 
                 #ConsultProfessorAPI, ConsultProfessor_idAPI,
                 ConsultFacultyAPI, ConsultFaculty_idAPI, ConsultDepartmentAPI, ConsultDepartment_idAPI,
                 CreateKnowledgeAreaAPI, CreateInvestigationGroupAPI, CreateInvestigationLineAPI, 
                 ConsultInvestigationGroup_idAPI, ConsultInvestigationGroup_DepartmentAPI,  ConsultKnowledgeAreaAPI, 
                 ConsultKnowledgeArea_idAPI, ConsultInvestigationLine_knowledgeAPI, ConsultInvestigationLine_idAPI)

urlpatterns = [
    #Javier
    #Crear
    path('api/1.0/crear_pais/', CreateCountryAPI.as_view()),
    path('api/1.0/crear_departamento/', CreateStateAPI.as_view()),
    path('api/1.0/crear_ciudad/', CreateCityAPI.as_view()),
    path('api/1.0/crear_institucion/', CreateInstitutionAPI.as_view()),
    path('api/1.0/crear_profesor/', CreateProfessorAPI.as_view()),
    path('api/1.0/crear_facultad/', CreateFacultyAPI.as_view()),
    path('api/1.0/crear_departamento_u/', CreateDepartmentAPI.as_view()),
    path('api/1.0/crear_formacion_academica/', CreateAcademicTrainingAPI.as_view()),
    #Consultar
    path('api/1.0/consultar_pais/', ConsultCountryAPI.as_view()),
    path('api/1.0/consultar_departamento_pais/<int:id_country>', ConsultState_CountryAPI.as_view()),
    path('api/1.0/consultar_ciudad_departamento/<int:id_dep>', ConsultCity_StateAPI.as_view()),
    path('api/1.0/consultar_institucion/', ConsultInstitutionAPI.as_view()),
    path('api/1.0/consultar_institucion_id/<int:id>', ConsultInstitution_idAPI.as_view()),
    # path('api/1.0/consultar_profesor/', ConsultProfessorAPI.as_view()),
    # path('api/1.0/consultar_profesor_id/<int:id>', ConsultProfessor_idAPI.as_view()),#TODO ESTA RECIBIENDO UN OBJETO USER
    path('api/1.0/consultar_facultad/', ConsultFacultyAPI.as_view()),
    path('api/1.0/consultar_facultad_id/<int:id>', ConsultFaculty_idAPI.as_view()),
    path('api/1.0/consultar_departamentoU/', ConsultDepartmentAPI.as_view()),
    path('api/1.0/consultar_departamentoU_id/<int:id>', ConsultDepartment_idAPI.as_view()),
    #Jeison
    #Crear
    path('api/1.0/crear_grupo_investigacion/', CreateInvestigationGroupAPI.as_view()),
    path('api/1.0/crear_area_conocimiento/', CreateKnowledgeAreaAPI.as_view()),
    path('api/1.0/crear_linea_investigacion/', CreateInvestigationLineAPI.as_view()),
    path('api/1.0/crear_trabaja/', CreateWorksInvestGroupAPI.as_view()),
    path('api/1.0/crear_dirige/', CreateManageInvestGroupAPI.as_view()),
    path('api/1.0/crear_maneja/', CreateManageInvestLineAPI.as_view()),
    #Consultar
    path('api/1.0/consultar_gi_dep/<int:dep>', ConsultInvestigationGroup_DepartmentAPI.as_view()),
    path('api/1.0/consultar_gi_id/<int:id>', ConsultInvestigationGroup_idAPI.as_view()),
    path('api/1.0/consultar_area_conocimiento/', ConsultKnowledgeAreaAPI.as_view()),
    path('api/1.0/consultar_area_conocimiento/<int:id>', ConsultKnowledgeArea_idAPI.as_view()),
    path('api/1.0/consultar_li_area/<int:id_area>', ConsultInvestigationLine_knowledgeAPI.as_view()),
    path('api/1.0/consultar_li_id/<int:id>', ConsultInvestigationLine_idAPI.as_view()),
    
]