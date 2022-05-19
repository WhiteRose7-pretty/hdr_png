from django.db import models


class HDRImage(models.Model):
    file = models.FileField(upload_to='hdr', null=True, blank=True)
    png_file = models.FileField(upload_to='hdr', null=True, blank=True)
    string = models.TextField(null=True, blank=True)
