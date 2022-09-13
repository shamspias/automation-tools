from rest_framework import serializers


class ProofreadingSerializers(serializers.Serializer):
    """
    Get paragraph
    """
    word = serializers.CharField(required=False, allow_blank=True, max_length=100)
