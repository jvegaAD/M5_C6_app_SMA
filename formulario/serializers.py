# from rest_framework import serializers
# from .models import Reporte

# class ReporteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reporte
#         fields = '__all__'


# Actualizacion al 2025 02 03

from rest_framework import serializers
from .models import Reporte

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'
