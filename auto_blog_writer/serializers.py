from rest_framework import serializers


class BlogSerializers(serializers.Serializer):
    """
    Get Topic
    """
    topic = serializers.CharField(required=False, allow_blank=True, max_length=250)
    section = serializers.CharField(required=False, allow_blank=True, max_length=250)
    content = serializers.CharField(required=False, allow_blank=True)
