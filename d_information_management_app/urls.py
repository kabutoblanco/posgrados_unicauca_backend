#General
from django.urls import path, include

#Javier
# from .views import consultarPais,crearDepartamento, crearCiudad, CrearPais
# from d_information_management_app.views import Home
#-------------------------------------------------

#Jeison
from .api import (CreateCountryAPI, CreateStateAPI, CreateCityAPI, CreateInstitutionAPI, CreateProfessorAPI,
                 CreateFacultyAPI, CreateDepartmentAPI, CreateAcademicTrainingAPI, ConsultManageInvestGroupAPI,
                 CreateWorksInvestGroupAPI, CreateManageInvestLineAPI, CreateManageInvestGroupAPI,
                 ConsultCountryAPI, ConsultCountry_idAPI,ConsultState_CountryAPI, ConsultCity_StateAPI,
                 ConsultInstitutionAPI, ConsultInstitution_idAPI, ConsultIsMemberAPI, ConsultMemberIGAPI,
                 ConsultProfessorAPI, ConsultProfessor_idAPI, CreateIsMemberAPI, ConsultWorksInvestGroupAPI,
                 ConsultFacultyAPI, ConsultFaculty_idAPI, ConsultDepartmentAPI, ConsultDepartment_idAPI,
                 CreateKnowledgeAreaAPI, CreateInvestigationGroupAPI, CreateInvestigationLineAPI, 
                 ConsultInvestigationGroup_idAPI, ConsultInvestigationGroup_DepartmentAPI, ConsultMemberProfessorAPI,
                 ConsultKnowledgeAreaAPI, ConsultKnowledgeArea_idAPI, ConsultInvestigationLine_knowledgeAPI,
                 ConsultInvestigationLine_idAPI, ConsultManageInvestGroup_DirecAPI, ConsultManageInvestGroup_GIAPI,
                 ConsultWorksInvestGroup_GIAPI,ReportTest, ConsultWorksDepartmAPI, ConsultWorksDepartm_profAPI,
                 ConsultWorksDepartm_depAPI, ConsultManageInvestLineAPI, ConsultManageInvestLine_invLineAPI, 
                 ConsultManageInvestLine_profAPI, ConsultProfessor_userAPI, CreateCoordinatorProgramAPI,
                 ConsultCoordinatorAPI)

urlpatterns = [
    #Javier
    #Crear
    path('api/1.0/report/<int:year>/<int:type>', ReportTest.as_view()),
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
    path('api/1.0/consultar_pais_id/<int:id_country>', ConsultCountry_idAPI.as_view()),
    path('api/1.0/consultar_departamento_pais/<int:id_country>', ConsultState_CountryAPI.as_view()),
    path('api/1.0/consultar_ciudad_departamento/<int:id_dep>', ConsultCity_StateAPI.as_view()),
    path('api/1.0/consultar_institucion/', ConsultInstitutionAPI.as_view()),
    path('api/1.0/consultar_institucion_id/<int:id>', ConsultInstitution_idAPI.as_view()),
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
    path('api/1.0/crear_maneja/', CreateManageInvestLineAPI.as_view()), # falta editar
    path('api/1.0/create_is_member/', CreateIsMemberAPI.as_view()),
    path('api/1.0/crear_coordinador/', CreateCoordinatorProgramAPI.as_view()),
    # falta todo lo relacionado con labora, desde crear hasta editar
    #Consultar
    path('api/1.0/consultar_gi_dep/<int:dep>', ConsultInvestigationGroup_DepartmentAPI.as_view()),
    path('api/1.0/consultar_gi_id/<int:id>', ConsultInvestigationGroup_idAPI.as_view()),
    path('api/1.0/consultar_area_conocimiento/', ConsultKnowledgeAreaAPI.as_view()),
    path('api/1.0/consultar_area_conocimiento/<int:id>', ConsultKnowledgeArea_idAPI.as_view()),
    path('api/1.0/consultar_li_area/<int:id_area>', ConsultInvestigationLine_knowledgeAPI.as_view()),
    path('api/1.0/consultar_li_id/<int:id>', ConsultInvestigationLine_idAPI.as_view()),
    path('api/1.0/consultar_profesor/', ConsultProfessorAPI.as_view()),
    path('api/1.0/consultar_profesor/<int:id>', ConsultProfessor_idAPI.as_view()),
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
    path('api/1.0/consultar_maneja/<int:id_p>/<int:id_i>', ConsultManageInvestLineAPI.as_view()), # ya esta editar labora (P-D)
    path('api/1.0/consultar_maneja_li/<int:id>', ConsultManageInvestLine_invLineAPI.as_view()),
    path('api/1.0/consultar_maneja_p/<int:id>', ConsultManageInvestLine_profAPI.as_view()),
    # Labora entre Prf y Dep
    path('api/1.0/consultar_labora/<int:id_p>/<int:id_d>', ConsultWorksDepartmAPI.as_view()), # ya esta editar labora (P-D)
    path('api/1.0/consultar_labora_p/<int:id>', ConsultWorksDepartm_profAPI.as_view()),
    path('api/1.0/consultar_labora_d/<int:id>', ConsultWorksDepartm_depAPI.as_view()),
    # Coordinador entre Prf y Programa  
    path('api/1.0/consultar_coordinador/<int:prog>/<str:period>', ConsultCoordinatorAPI.as_view()),

]