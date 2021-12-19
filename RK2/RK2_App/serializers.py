from rest_framework import serializers
import RK2_App.models as models


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PC
        fields = ["id", "name", "price", "id_processor"]


class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Processor
        fields = ["id", "name", "frequency", "memory_cash"]