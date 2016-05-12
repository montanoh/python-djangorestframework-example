from rest_framework import viewsets
from record.models import Record
from api.serializers import RecordSerializer


class Record(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
