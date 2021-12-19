from django.shortcuts import render
from rest_framework import viewsets
import RK2_App.models as models
import RK2_App.serializers as serializers

# Create your views here.


class PCViewSet(viewsets.ModelViewSet):
    queryset = models.PC.objects.all()
    serializer_class = serializers.PCSerializer


class ProcessorViewSet(viewsets.ModelViewSet):
    queryset = models.Processor.objects.all()
    serializer_class = serializers.ProcessorSerializer


def index(request):
    processors = models.Processor.objects.all()
    data = []
    for processor in processors:
        data.append((processor, models.PC.objects.get_pc_by_processor_id(processor.id)))

    return render(request, "index.html", {"data": data})
