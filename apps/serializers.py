from .models import Juego
from rest_framework import serializers


class JuegoSerializer(serializers.ModelSerializer):
    nombre_Compañia = serializers.CharField(read_only=True,source="Compañia.nombre")
    class Meta:
        model = Juego
        fields = '__all__'