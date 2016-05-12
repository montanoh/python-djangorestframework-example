from rest_framework import serializers
from record.models import Record


class RecordSerializer(serializers.ModelSerializer):
    """
    Serializer to parse Record data
    """

    class Meta:
        model = Record
        fields = ('id', 'date', 'gid', 'tag', 'note', 'money')