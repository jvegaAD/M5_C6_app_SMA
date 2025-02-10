"""
URL configuration for reportesma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('formulario.urls')),
# ]


# CODIGO GEMINI 02/02/2025
# from django.contrib import admin
# from django.urls import path, include
# from formulario.views import reporte_clasificacion_view  # Importa la vista

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('formulario.urls')),
#     path('', reporte_clasificacion_view, name='inicio')  # Agrega la ruta para la página de inicio
# ]


# Actualizacion al 03 02 2025
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('formulario.urls')),  # Incluye las rutas de la aplicación `formulario`
# ]


# Actualizacion 2 para Swagger al 03 02 2025
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from formulario.views import ReporteViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Definir el esquema Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API de Reportes SMA",
        default_version='v1',
        description="Documentación interactiva de la API de reportes",
        contact=openapi.Contact(email="tu-email@dominio.com"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

router = DefaultRouter()
router.register(r'reportes', ReporteViewSet)

# Ajustes 
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
#     path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('formulario.urls')),  # Reintroduce la ruta para la vista principal
]
