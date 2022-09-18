from django.db import models


# Create your models here.
class TranslatedFile(models.Model):
    """
    File to translate
    """
    name = models.CharField(max_length=200, blank=True, null=True)
    my_file = models.FileField(upload_to='files/', blank=True, null=True)
    translated_file = models.FileField(upload_to='translated/', blank=True, null=True)

    def __str__(self):
        return "File : " + self.name
