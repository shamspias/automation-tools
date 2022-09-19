from django.db import models


# Create your models here.

class Proofreading(models.Model):
    """
    Modelo for Proofreading documents
    """
    name = models.CharField(max_length=200, blank=True, null=True)
    my_file = models.FileField(upload_to='proofread/', blank=True, null=True)
    proofread_file = models.FileField(upload_to='proofread/done/', blank=True, null=True)

    def __str__(self):
        return "File : " + self.name
