# from rest_framework.routers import DefaultRouter
# from .views import ReporteViewSet

# router = DefaultRouter()
# router.register(r'reportes', ReporteViewSet)

# urlpatterns = router.urls




# actualizacion al 03 02 2025


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ReporteViewSet, resumen_parametros_view, pagina_inicio

# router = DefaultRouter()
# router.register(r'reportes', ReporteViewSet)

# urlpatterns = [
#     path('', pagina_inicio, name='inicio'),  # Página de inicio
#     path('api/', include(router.urls)),
#     path('resumen/', resumen_parametros_view, name='resumen_parametros'),
# ]



# actualizacion  N°2 al 03 02 2025

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReporteViewSet, resumen_parametros_view, pagina_inicio

router = DefaultRouter()
router.register(r'reportes', ReporteViewSet)

urlpatterns = [
    path('', pagina_inicio, name='inicio'),  # Página de inicio
    path('api/', include(router.urls)),
    path('resumen/', resumen_parametros_view, name='resumen_parametros'),
]
