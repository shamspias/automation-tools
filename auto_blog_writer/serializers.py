from rest_framework import serializers


class BlogSerializers(serializers.Serializer):
    """
    Make Blog
    """
    topic = serializers.CharField(required=False, allow_blank=True, max_length=250)
    title = serializers.CharField(required=False, allow_blank=True, max_length=250)
    section = serializers.CharField(required=False, allow_blank=True, max_length=250)
