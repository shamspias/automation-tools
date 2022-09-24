from rest_framework import serializers


class ResearchPaperSerializers(serializers.Serializer):
    """
    Serializer class for Research Paper
    """
    topic = serializers.CharField(required=False, allow_blank=True, max_length=250)
    title = serializers.CharField(required=False, allow_blank=True, max_length=250)
    field = serializers.CharField(required=False, allow_blank=True, max_length=250)
