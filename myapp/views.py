from django.shortcuts import render, redirect
from django.db import connection
from .models import Paciente
from .models import Paciente, DocumentoIdentificacion

def pagina_principal(request):
    return render(request, "myapp/pagina_principal.html")

def obtener_datos_tabla(nombre_tabla):
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM "{nombre_tabla}"')
        return cursor.fetchall()

def agregar_paciente(request):
    # Obtener tipos de documento desde la tabla DocumentoIdentificacion
    choices_tipodocumentacion = [('CC', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de Identidad'),
                                 ('CE', 'Cédula de Extranjería'),
                                 ('CD', 'Carné diplomático'),
                                 ('PA', 'Pasaporte'),
                                 ('SC', 'Salvoconducto de permanencia'),
                                 ('PT', 'Permiso Temporal de Permanencia'),
                                 ('PE', 'Permiso Especial de Permanencia'),
                                 ('RC', 'Registro civil'),
                                 ('TI', 'Tarjeta de identidad'),
                                 ('CN', 'Certificado de nacido vivo'),
                                 ('AS', 'Adulto sin identificar'),
                                 ('MS', 'Menor sin identificar'),
                                 ('DE', 'Documento extranjero'),
                                 ('SI', 'Sin identificación')]
    paises = obtener_datos_tabla("ct_paiss")
    ocupaciones = obtener_datos_tabla("ct_ocupacionn")
    discapacidades = obtener_datos_tabla("ct_discapacidad")
    departamentos = obtener_datos_tabla("ct_departamentos")
    municipios = obtener_datos_tabla("ct_municipios")
    etnias = obtener_datos_tabla("ct_pertenenciaetnicaa")
    comunidades = obtener_datos_tabla("ct_comunidadetnicaa")
    entidades_responsables = obtener_datos_tabla("ct_entidadresponsablee")

    choices_sexobiologico = [('M', 'Masculino'), ('F', 'Femenino')]
    choices_identidadgenero = [('H', 'Hombre'), ('M', 'Mujer'), ('NB', 'No Binario')]
    choices_oposiciondonacion = [('S', 'Sí'), ('N', 'No')]

#este if es para hacer post y activar la funcionalidad de agregar registros
    if request.method == "POST":
        pais = request.POST.get("pais")
        ocupacion = request.POST.get("ocupacion")
        discapacidad = request.POST.get("discapacidad")
        departamento = request.POST.get("departamento")
        municipio = request.POST.get("municipio")
        etnia = request.POST.get("etnia")
        comunidad = request.POST.get("comunidad")
        entidad_responsable = request.POST.get("entidades_responsables")

        for tipo_id, nombre in choices_tipodocumentacion:
            DocumentoIdentificacion.objects.get_or_create(
                ct_documentoIdentificacionId=tipo_id,
                defaults={'ct_nombreDocumentoIdentificacion': nombre}
            )

        if request.method == "POST":
            tipo_documento_id = request.POST.get("tipodocumentacion")
            numero_documento = request.POST.get("numeroDocumento")

        # Crear o actualizar el registro en DocumentoIdentificacion con el número ingresado
        documento_identificacion, created = DocumentoIdentificacion.objects.get_or_create(
            ct_documentoIdentificacionId=tipo_documento_id,
            defaults={
                'ct_nombreDocumentoIdentificacion': dict(choices_tipodocumentacion).get(tipo_documento_id),
                'ct_numeroDocumentoIdentificacion': numero_documento
            }
        )

        # Datos del paciente
        ct_primerapellido = request.POST.get("ct_primerapellido")
        ct_segundoapellido = request.POST.get("ct_segundoapellido")
        ct_primernombre = request.POST.get("ct_primernombre")
        ct_segundonombre = request.POST.get("ct_segundonombre")
        ct_fechanacimiento = request.POST.get("ct_fechanacimiento")
        ct_nombresexobiologico = request.POST.get("ct_nombresexobiologico")
        ct_nombreidentidadgenero = request.POST.get("ct_nombreidentidadgenero")
        ct_oposiciondonacion = request.POST.get("ct_oposiciondonacion")
        ct_fechaoposiciondonacion = request.POST.get("ct_fechaoposiciondonacion")
        ct_nombrevoluntadanticipada = request.POST.get("ct_nombrevoluntadanticipada")
        ct_fechavoluntadanticipada = request.POST.get("ct_fechavoluntadanticipada")
        ct_categoriadiscapacidad = request.POST.get("ct_categoriadiscapacidad")
        ct_nombrezonaterritorial = request.POST.get("ct_nombrezonaterritorial")

        # Datos quemados
        ct_sexobiologicoid = "01"
        ct_identidadgeneroid = "01"
        ct_voluntadanticipadaprestadorid = "01"
        ct_zonaterritorialid = "01"

        # Guardar el paciente en la base de datos
        Paciente.objects.create(
            ct_pais=pais,
            ct_tipodocumentacion=documento_identificacion,
            ct_primerapellido=ct_primerapellido,
            ct_segundoapellido=ct_segundoapellido,
            ct_primernombre=ct_primernombre,
            ct_segundonombre=ct_segundonombre,
            ct_fechanacimiento=ct_fechanacimiento,
            ct_nombresexobiologico=ct_nombresexobiologico,
            ct_nombreidentidadgenero=ct_nombreidentidadgenero,
            ct_ocupacion=ocupacion,
            ct_oposiciondonacion=ct_oposiciondonacion,
            ct_fechaoposiciondonacion=ct_fechaoposiciondonacion,
            ct_nombrevoluntadanticipada=ct_nombrevoluntadanticipada,
            ct_fechavoluntadanticipada=ct_fechavoluntadanticipada,
            ct_categoriadiscapacidad=discapacidad,
            ct_municipioresidencia=municipio,
            ct_departamentoresidencia=departamento,
            ct_comunidadetnica=comunidad,
            ct_pertenenciaetnica=etnia,
            ct_nombrezonaterritorial=ct_nombrezonaterritorial,
            ct_entidadresponsable=entidad_responsable,
            ct_sexobiologicoid=ct_sexobiologicoid,
            ct_identidadgeneroid=ct_identidadgeneroid,
            ct_voluntadanticipadaprestadorid=ct_voluntadanticipadaprestadorid,
            ct_zonaterritorialid=ct_zonaterritorialid
        )

        # Redirigir o recargar la página
        return redirect('agregar_paciente')

    pacientes = Paciente.objects.all()

    context = {
        'paises': paises,
        'ocupaciones': ocupaciones,
        'discapacidades': discapacidades,
        'departamentos': departamentos,
        'municipios': municipios,
        'etnias': etnias,
        'comunidades': comunidades,
        'entidades_responsables': entidades_responsables,  
        'choices_tipodocumentacion': choices_tipodocumentacion,
        'choices_sexobiologico': choices_sexobiologico,
        'choices_identidadgenero': choices_identidadgenero,
        'choices_oposiciondonacion': choices_oposiciondonacion,
        'pacientes': pacientes,
    }

    return render(request, 'myapp/agregar_paciente.html', context)

def contacto_servicio(request):
    prestadores_servicios = obtener_datos_tabla("ct_prestadorservicio")
    modalidades_servicios = obtener_datos_tabla("ct_modalidadservicio")
    vias_ingreso = obtener_datos_tabla("ct_viaingresoo")
    causas_atencion = obtener_datos_tabla("ct_causaatencionn")
    diagnosticos_principales_ingreso = obtener_datos_tabla("ct_diagnosticoprincipalingreso")

    if request.method == "POST":
        prestador_servicio = request.POST.get("prestador_servicio")
        modalidad_servicio = request.POST.get("modalidad_servicio")
        via_ingreso = request.POST.get("via_ingreso")
        causa_atencion = request.POST.get("causa_atencion")
        diagnostico_principal_ingreso = request.POST.get("diagnostico_principal_ingreso")

    context = {
        'prestadores_servicios': prestadores_servicios,
        'modalidades_servicios': modalidades_servicios,
        'vias_ingreso': vias_ingreso,
        'causas_atencion': causas_atencion,
        'diagnosticos_principales_ingreso': diagnosticos_principales_ingreso,
    }
    return render(request, 'myapp/contacto_servicio.html', context)



