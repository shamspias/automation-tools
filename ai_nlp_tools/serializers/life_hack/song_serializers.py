from rest_framework import serializers


class SongSerializers(serializers.Serializer):
    """
    Serializer class for Songs
    """
    topic = serializers.CharField(required=False, allow_blank=True, max_length=250)
    categories = serializers.CharField(required=False, allow_blank=True, max_length=30)
