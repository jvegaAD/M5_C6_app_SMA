

# # Codigo inicial funcionando.
# from rest_framework import viewsets
# from .models import Reporte
# from .serializers import ReporteSerializer

# class ReporteViewSet(viewsets.ModelViewSet):
#     queryset = Reporte.objects.all()
#     serializer_class = ReporteSerializer

# ------------------------------------------------------------------------------------------------------
# Codigo GPT para configurar una vista de inicio "No logrado, la incluyo como uan vista independiente"
# from django.shortcuts import render
# from .models import Reporte

# def clasificacion_normativa(reporte):
#     clasificacion = ""
#     if reporte.tema == 'Uso residencial de calefactores':
#         if reporte.unidad == 'mg/m3' and reporte.cantidad > 150:
#             clasificacion = 'Fuera de norma'
#         else:
#             clasificacion = 'Dentro de norma'
#     elif reporte.tema == 'Quemas agrícola':
#         if reporte.cantidad > 200:
#             clasificacion = 'Fuera de norma'
#         else:
#             clasificacion = 'Dentro de norma'
#     else:
#         clasificacion = 'Sin clasificación definida'
#     return clasificacion

# def obtener_tabla_clasificacion():
#     return {
#         'Uso residencial de calefactores': {
#             'unidad': 'mg/m3',
#             'limite': 150,
#             'descripcion': 'Límite máximo permitido para emisiones de calefactores residenciales.'
#         },
#         'Quemas agrícola': {
#             'unidad': 'kg',
#             'limite': 200,
#             'descripcion': 'Cantidad máxima permitida para quemas agrícolas por temporada.'
#         }
#     }

# def reporte_clasificacion_view(request):
#     reportes = Reporte.objects.all()
#     reportes_clasificados = [
#         {
#             'departamento': reporte.departamento,
#             'comuna': reporte.comuna,
#             'fecha': reporte.fecha,
#             'tema': reporte.tema,
#             'descripcion': reporte.descripcion_reporte,
#             'unidad': reporte.unidad,
#             'cantidad': reporte.cantidad,
#             'estado': reporte.estado,
#             'clasificacion': clasificacion_normativa(reporte)
#         } for reporte in reportes
#     ]

#     tablas_clasificacion = obtener_tabla_clasificacion()
#     return render(request, 'reporte_clasificacion.html', {
#         'reportes': reportes_clasificados,
#         'tablas_clasificacion': tablas_clasificacion
#     })


# ------------------------------------------------------------------------------------------------------
# # Codigo GPT modificación.
# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Reporte
# from .serializers import ReporteSerializer

# # Definición del ViewSet para la API REST
# class ReporteViewSet(viewsets.ModelViewSet):
#     queryset = Reporte.objects.all()
#     serializer_class = ReporteSerializer

# # Función para clasificar reportes según ciertas normativas
# def clasificacion_normativa(reporte):
#     clasificacion = ""
#     if reporte.tema == 'Uso residencial de calefactores':
#         if reporte.unidad == 'mg/m3' and reporte.cantidad > 150:
#             clasificacion = 'Fuera de norma'
#         else:
#             clasificacion = 'Dentro de norma'
#     elif reporte.tema == 'Quemas agrícola':
#         if reporte.cantidad > 200:
#             clasificacion = 'Fuera de norma'
#         else:
#             clasificacion = 'Dentro de norma'
#     else:
#         clasificacion = 'Sin clasificación definida'
#     return clasificacion

# # Función para obtener una tabla de clasificación de normativas
# def obtener_tabla_clasificacion():
#     return {
#         'Uso residencial de calefactores': {
#             'unidad': 'mg/m3',
#             'limite': 150,
#             'descripcion': 'Límite máximo permitido para emisiones de calefactores residenciales.'
#         },
#         'Quemas agrícola': {
#             'unidad': 'kg',
#             'limite': 200,
#             'descripcion': 'Cantidad máxima permitida para quemas agrícolas por temporada.'
#         }
#     }

# Vista para mostrar los reportes clasificados
# def reporte_clasificacion_view(request):
#     reportes = Reporte.objects.all()
#     reportes_clasificados = [
#         {
#             'id': reporte.id,  # Mostrar el ID del registro
#             'departamento': reporte.departamento,
#             'comuna': reporte.comuna,
#             'fecha': reporte.fecha,
#             'tema': reporte.tema,
#             'descripcion': reporte.descripcion_reporte,
#             'unidad': reporte.unidad,
#             'cantidad': reporte.cantidad,
#             'estado': reporte.estado,
#             'clasificacion': clasificacion_normativa(reporte)
#         } for reporte in reportes
#     ]

#     tablas_clasificacion = obtener_tabla_clasificacion()
#     return render(request, 'reporte_clasificacion.html', {
#         'reportes': reportes_clasificados,
#         'tablas_clasificacion': tablas_clasificacion
#     })


# ajuste del 03/02/2025

# from django.shortcuts import render
# from django.db.models import Min, Max
# from rest_framework import viewsets
# from django.http import HttpResponse  # Import necesario para la página de inicio
# from .models import Reporte
# from .serializers import ReporteSerializer

# # Definición del ViewSet para la API REST
# class ReporteViewSet(viewsets.ModelViewSet):
#     queryset = Reporte.objects.all()
#     serializer_class = ReporteSerializer

# # Vista para mostrar el resumen de parámetros
# def resumen_parametros_view(request):
#     # Consulta para agrupar por Parametro, obteniendo el mínimo y máximo de ValorReportado
#     resumen = Reporte.objects.values('Parametro', 'Unidad').annotate(
#         min_valor=Min('ValorReportado'),
#         max_valor=Max('ValorReportado')
#     )

#     # Renderiza la plantilla con los datos agrupados
#     return render(request, 'reporte_clasificacion.html', {'resumen': resumen})

# # Página de inicio
# def pagina_inicio(request):
#     return HttpResponse("<h1>Bienvenido a la Aplicación SMA</h1><p>Selecciona una opción del menú para continuar.</p>")



# ajuste n°2 del 03/02/2025

from django.shortcuts import render
from django.db.models import Min, Max
from rest_framework import viewsets
from .models import Reporte
from .serializers import ReporteSerializer

# Definición del ViewSet para la API REST
class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

# Vista para mostrar el resumen de parámetros
def resumen_parametros_view(request):
    resumen = Reporte.objects.values('Parametro', 'Unidad').annotate(
        min_valor=Min('ValorReportado'),
        max_valor=Max('ValorReportado')
    )
    return render(request, 'reporte_clasificacion.html', {'resumen': resumen})

# Vista principal de la aplicación
def pagina_inicio(request):
    resumen = Reporte.objects.values('Parametro', 'Unidad').annotate(
        min_valor=Min('ValorReportado'),
        max_valor=Max('ValorReportado')
    )
    return render(request, 'reporte_resumen.html', {'resumen': resumen})
