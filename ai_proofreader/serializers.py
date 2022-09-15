from rest_framework import serializers


class ProofreadingSerializers(serializers.Serializer):
    """
    Get paragraph
    """
    word = serializers.CharField(required=False, allow_blank=True, max_length=100)


class ProofreadingFileSerializers(serializers.Serializer):
    """
    proofread all text inside file
    """
    document = serializers.FileField(allow_empty_file=True)
