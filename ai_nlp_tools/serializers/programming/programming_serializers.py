from rest_framework import serializers


class ProgrammingSerializers(serializers.Serializer):
    """
    Serializer class for Research Paper
    """
    code = serializers.CharField(required=False, allow_blank=True)
