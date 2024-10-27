from django.db import models

#Nueva implementación para documento de identifiación
class DocumentoIdentificacion(models.Model):
    ct_documentoIdentificacionId = models.CharField(max_length=2, primary_key=True)  # Ej. 'CC'
    ct_nombreDocumentoIdentificacion = models.CharField(max_length=40)  # Ej. 'Cédula de Ciudadanía'
    ct_numeroDocumentoIdentificacion = models.CharField(max_length=20)  # Número que ingresará el usuario

    class Meta:
        db_table = 'ct_documentoIdentificacion'

    def __str__(self):
        return f"{self.ct_nombreDocumentoIdentificacion} - {self.ct_numeroDocumentoIdentificacion}"

class Paciente(models.Model):
    ct_pacienteId = models.AutoField(primary_key=True)
    ct_pais = models.CharField(max_length=100)
    #Esto sirve como referencia a la otra tabla ct_documentoIdentificacion
    ct_tipodocumentacion = models.ForeignKey(DocumentoIdentificacion, on_delete=models.CASCADE)
    ct_primerapellido = models.CharField(max_length=100)
    ct_segundoapellido = models.CharField(max_length=100)
    ct_primernombre = models.CharField(max_length=100)
    ct_segundonombre = models.CharField(max_length=100, blank=True)
    ct_fechanacimiento = models.DateField()
    ct_nombresexobiologico = models.CharField(max_length=50)
    ct_nombreidentidadgenero = models.CharField(max_length=50)
    ct_ocupacion = models.CharField(max_length=100)
    ct_oposiciondonacion = models.CharField(max_length=50)
    ct_fechaoposiciondonacion = models.DateField(null=True, blank=True)
    ct_nombrevoluntadanticipada = models.CharField(max_length=100, blank=True)
    ct_fechavoluntadanticipada = models.DateField(null=True, blank=True)
    ct_categoriadiscapacidad = models.CharField(max_length=100)
    ct_municipioresidencia = models.CharField(max_length=100)
    ct_departamentoresidencia = models.CharField(max_length=100)
    ct_comunidadetnica = models.CharField(max_length=100)
    ct_pertenenciaetnica = models.CharField(max_length=100)
    ct_nombrezonaterritorial = models.CharField(max_length=100)
    ct_entidadresponsable = models.CharField(max_length=100)
    ct_sexobiologicoid = models.CharField(max_length=2, default='01')
    ct_identidadgeneroid = models.CharField(max_length=2, default='01')
    ct_voluntadanticipadaprestadorid = models.CharField(max_length=2, default='01')
    ct_zonaterritorialid = models.CharField(max_length=2, default='01')

    class Meta:
        db_table = 'ct_paciente'

    def __str__(self):
        return f"{self.ct_primernombre} {self.ct_primerapellido}"





