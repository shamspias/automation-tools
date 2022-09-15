from rest_framework import serializers


class TranslationFileSerializers(serializers.Serializer):
    """
    Translate all text inside file
    """
    source_ln = serializers.CharField(allow_blank=True, max_length=20)
    target_ln = serializers.CharField(allow_blank=True, max_length=20)
    document = serializers.FileField(allow_empty_file=True)
