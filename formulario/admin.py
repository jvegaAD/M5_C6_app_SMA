# from django.contrib import admin
# from .models import Reporte

# class ReporteAdmin(admin.ModelAdmin):
#     # Mostrar el ID en la vista de lista del panel de administración
#     list_display = ('id', 'departamento', 'comuna', 'fecha', 'tema', 'estado')

#     # Hacer que el ID sea solo de lectura en la vista de detalle
#     readonly_fields = ('id',)

# admin.site.register(Reporte, ReporteAdmin)


# codigo al 02/02/2025
# from django.contrib import admin
# from .models import Reporte

# class ReporteAdmin(admin.ModelAdmin):
#     list_display = (
#         'id', 'PeriodoInforme', 'RUT', 'RazonSocial', 'Planta', 'PuntoDeDescarga',
#         'CuerpoReceptor', 'Norma', 'Muestra', 'Parametro', 'Unidad', 'ValorReportado',
#         'TipoDeControl', 'Laboratorio', 'UnidadFiscalizable', 'departamento', 'ComunaId',
#         'comuna', 'NombreCategoria', 'NombreSubCategoria', 'Direccion', 'NumeroRCA', 'FechaRCA'
#     )

#     # Hacer la columna 'id' solo de lectura
#     readonly_fields = ('id',)

#     # Configurar campos de búsqueda (opcional)
#     search_fields = ('RazonSocial', 'RUT', 'Planta')

#     # Configurar filtros (opcional)
#     list_filter = ('PeriodoInforme', 'RazonSocial', 'departamento')

# admin.site.register(Reporte, ReporteAdmin)


# Ajuste del 03 02 2025

from django.contrib import admin
from .models import Reporte
from django.utils.translation import gettext_lazy as _

# Filtro por año
class YearFilter(admin.SimpleListFilter):
    title = _('Año PeriodoInforme')
    parameter_name = 'PeriodoInforme__year'

    def lookups(self, request, model_admin):
        years = Reporte.objects.dates('PeriodoInforme', 'year')
        return [(year.year, year.year) for year in years]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(PeriodoInforme__year=self.value())

# Filtro por mes
class MonthFilter(admin.SimpleListFilter):
    title = _('Mes PeriodoInforme')
    parameter_name = 'PeriodoInforme__month'

    def lookups(self, request, model_admin):
        months = [
            (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'),
            (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'),
            (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')
        ]
        return months

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(PeriodoInforme__month=self.value())

# Configuración del admin
class ReporteAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'PeriodoInforme', 'RUT', 'RazonSocial', 'Planta', 'PuntoDeDescarga',
        'CuerpoReceptor', 'Norma', 'Muestra', 'Parametro', 'Unidad', 'ValorReportado',
        'TipoDeControl', 'Laboratorio', 'UnidadFiscalizable', 'departamento', 'ComunaId',
        'comuna', 'NombreCategoria', 'NombreSubCategoria', 'Direccion', 'NumeroRCA', 'FechaRCA'
    )

    readonly_fields = ('id',)
    search_fields = ('RazonSocial', 'RUT', 'Planta')

    # Nuevo orden de filtros
    list_filter = (
        'departamento',
        'comuna',
        YearFilter,            # Filtro personalizado por año
        MonthFilter,           # Filtro personalizado por mes
        'RazonSocial',
        'Planta',
        'PuntoDeDescarga',
        'CuerpoReceptor',
    )

# Registrar el modelo en el admin
admin.site.register(Reporte, ReporteAdmin)
