# from django.db import models

# class Reporte(models.Model):
#     # Columna 'id' de sistema para registro (autoincremental y clave primaria)
#     id = models.BigAutoField(primary_key=True)

#     # Definición de las demás columnas
#     PeriodoInforme = models.DateField()
#     RUT = models.CharField(max_length=20)
#     RazonSocial = models.CharField(max_length=255)
#     Planta = models.CharField(max_length=255)
#     PuntoDeDescarga = models.CharField(max_length=255)
#     CuerpoReceptor = models.CharField(max_length=255)
#     Norma = models.CharField(max_length=50)
#     Muestra = models.IntegerField()
#     Parametro = models.CharField(max_length=255)
#     Unidad = models.CharField(max_length=50)
#     ValorReportado = models.FloatField()
#     TipoDeControl = models.CharField(max_length=100)
#     Laboratorio = models.CharField(max_length=255)
#     UnidadFiscalizable = models.CharField(max_length=255)
#     departamento = models.CharField(max_length=255)
#     ComunaId = models.IntegerField()
#     comuna = models.CharField(max_length=255)
#     NombreCategoria = models.CharField(max_length=255)
#     NombreSubCategoria = models.CharField(max_length=255)
#     Direccion = models.CharField(max_length=255)
#     NumeroRCA = models.IntegerField()
#     FechaRCA = models.DateField()

#     class Meta:
#         db_table = 'formulario_reporte'


#Actualizacion al 03 02 2025

from django.db import models

class Reporte(models.Model):
    id = models.BigAutoField(primary_key=True)
    PeriodoInforme = models.DateField()
    RUT = models.CharField(max_length=20)
    RazonSocial = models.CharField(max_length=255)
    Planta = models.CharField(max_length=255)
    PuntoDeDescarga = models.CharField(max_length=255)
    CuerpoReceptor = models.CharField(max_length=255)
    Norma = models.CharField(max_length=50)
    Muestra = models.IntegerField()
    Parametro = models.CharField(max_length=255)
    Unidad = models.CharField(max_length=50)
    ValorReportado = models.FloatField()
    TipoDeControl = models.CharField(max_length=100)
    Laboratorio = models.CharField(max_length=255)
    UnidadFiscalizable = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    ComunaId = models.IntegerField()
    comuna = models.CharField(max_length=255)
    NombreCategoria = models.CharField(max_length=255)
    NombreSubCategoria = models.CharField(max_length=255)
    Direccion = models.CharField(max_length=255)
    NumeroRCA = models.IntegerField()
    FechaRCA = models.DateField()

    class Meta:
        db_table = 'formulario_reporte'




# Nuevo Ajuste anulado
# from django.db import models

# class Reporte(models.Model):
#     PeriodoInforme = models.DateField()  # Fecha del informe
#     RUT = models.CharField(max_length=20)  # RUT único
#     RazonSocial = models.CharField(max_length=255)  # Razón social de la entidad
#     Planta = models.CharField(max_length=255)  # Nombre de la planta
#     PuntoDeDescarga = models.CharField(max_length=255)  # Punto de descarga
#     CuerpoReceptor = models.CharField(max_length=255)  # Cuerpo receptor de residuos
#     Norma = models.CharField(max_length=50)  # Norma que regula el proceso
#     Muestra = models.PositiveIntegerField()  # Número de muestra
#     Parametro = models.CharField(max_length=255)  # Parámetro medido en la muestra
#     Unidad = models.CharField(max_length=50)  # Unidad de medición
#     ValorReportado = models.FloatField()  # Valor reportado de la muestra
#     TipoDeControl = models.CharField(max_length=100)  # Tipo de control aplicado
#     Laboratorio = models.CharField(max_length=255)  # Laboratorio responsable del análisis
#     UnidadFiscalizable = models.CharField(max_length=255)  # Unidad fiscalizable
#     departamento = models.CharField(max_length=255)  # Departamento o región
#     ComunaId = models.PositiveIntegerField()  # Identificación única de la comuna
#     comuna = models.CharField(max_length=255)  # Nombre de la comuna
#     NombreCategoria = models.CharField(max_length=255)  # Categoría del reporte
#     NombreSubCategoria = models.CharField(max_length=255)  # Subcategoría del reporte
#     Direccion = models.CharField(max_length=255)  # Dirección de la planta o punto de control
#     NumeroRCA = models.PositiveIntegerField()  # Número de la RCA (Resolución de Calificación Ambiental)
#     FechaRCA = models.DateField()  # Fecha de emisión de la RCA

#     class Meta:
#         db_table = 'formulario_reporte'
#         verbose_name = "Reporte"
#         verbose_name_plural = "Reportes"

#     def __str__(self):
#         return f"{self.RazonSocial} - {self.Parametro} ({self.PeriodoInforme})"
