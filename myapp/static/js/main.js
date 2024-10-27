document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM loaded with JavaScript");
});

function mostrarDetalles(pacienteId) {
  // Obtener detalles del paciente usando pacienteId (esto es un marcador de posición, reemplazar con la lógica real de obtención de datos)
  const paciente = obtenerDetallesPaciente(pacienteId);

  // Rellenar contenido del modal
  const contenidoModal = document.getElementById("contenidoModal");
  contenidoModal.innerHTML = `
            <p><strong>Documento de Identificación:</strong> ${paciente.ct_numeroDocumentoIdentificacion}</p>
            <p><strong>País:</strong> ${paciente.ct_pais}</p>
            <p><strong>Tipo Documentación:</strong> ${paciente.ct_tipodocumentacion_id}</p>
            <p><strong>Primer Apellido:</strong> ${paciente.ct_primerapellido}</p>
            <p><strong>Segundo Apellido:</strong> ${paciente.ct_segundoapellido}</p>
            <p><strong>Primer Nombre:</strong> ${paciente.ct_primernombre}</p>
            <p><strong>Segundo Nombre:</strong> ${paciente.ct_segundonombre}</p>
            <p><strong>Fecha de Nacimiento:</strong> ${paciente.ct_fechanacimiento}</p>
            <p><strong>Sexo Biológico:</strong> ${paciente.ct_nombresexobiologico}</p>
            <p><strong>Identidad de Género:</strong> ${paciente.ct_nombreidentidadgenero}</p>
            <p><strong>Ocupación:</strong> ${paciente.ct_ocupacion}</p>
            <p><strong>Oposición Donación:</strong> ${paciente.ct_oposiciondonacion}</p>
            <p><strong>Fecha Oposición Donación:</strong> ${paciente.ct_fechaoposiciondonacion}</p>
            <p><strong>Nombre Voluntad Anticipada:</strong> ${paciente.ct_nombrevoluntadanticipada}</p>
            <p><strong>Fecha Voluntad Anticipada:</strong> ${paciente.ct_fechavoluntadanticipada}</p>
            <p><strong>Categoría Discapacidad:</strong> ${paciente.ct_categoriadiscapacidad}</p>
            <p><strong>Municipio de Residencia:</strong> ${paciente.ct_municipioresidencia}</p>
            <p><strong>Departamento de Residencia:</strong> ${paciente.ct_departamentoresidencia}</p>
            <p><strong>Comunidad Étnica:</strong> ${paciente.ct_comunidadetnica}</p>
            <p><strong>Pertenencia Étnica:</strong> ${paciente.ct_pertenenciaetnica}</p>
            <p><strong>Zona Territorial:</strong> ${paciente.ct_nombrezonaterritorial}</p>
            <p><strong>Entidad Responsable:</strong> ${paciente.ct_entidadresponsable}</p>
        `;

  // Mostrar modal
  document.getElementById("detallesModal").classList.remove("hidden");
}

function cerrarModal() {
  document.getElementById("detallesModal").classList.add("hidden");
}

function obtenerDetallesPaciente(pacienteId) {
  // Función de marcador de posición para simular la obtención de detalles del paciente
  // Reemplazar esto con la lógica real de obtención de datos
  return {
    ct_numeroDocumentoIdentificacion: "12345678",
    ct_pais: "País Ejemplo",
    ct_tipodocumentacion_id: "Tipo Ejemplo",
    ct_primerapellido: "Apellido1",
    ct_segundoapellido: "Apellido2",
    ct_primernombre: "Nombre1",
    ct_segundonombre: "Nombre2",
    ct_fechanacimiento: "01/01/2000",
    ct_nombresexobiologico: "Masculino",
    ct_nombreidentidadgenero: "Masculino",
    ct_ocupacion: "Ocupación Ejemplo",
    ct_oposiciondonacion: "No",
    ct_fechaoposiciondonacion: "N/A",
    ct_nombrevoluntadanticipada: "N/A",
    ct_fechavoluntadanticipada: "N/A",
    ct_categoriadiscapacidad: "N/A",
    ct_municipioresidencia: "Municipio Ejemplo",
    ct_departamentoresidencia: "Departamento Ejemplo",
    ct_comunidadetnica: "Comunidad Ejemplo",
    ct_pertenenciaetnica: "Pertenencia Ejemplo",
    ct_nombrezonaterritorial: "Zona Ejemplo",
    ct_entidadresponsable: "Entidad Ejemplo",
  };
}
