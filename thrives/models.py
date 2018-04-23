from django.db import models
from s3direct.fields import S3DirectField

from django import forms
from s3direct.widgets import S3DirectWidget

class Thrive(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=800)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    #location stuff
    address = models.CharField(max_length=200)
    longitude = models.DecimalField(max_digits=9, decimal_places=6) #temporal
    latitude = models.DecimalField(max_digits=9, decimal_places=6) #temporal
    radius = models.PositiveSmallIntegerField()
    #media related stuff
    story = S3DirectField(dest='thrive_media_destination')

    class Meta:
        ordering = ('created',)

class ThriveForm(forms.Form):
    story = forms.URLField(widget=S3DirectWidget(dest='thrive_media_destination'))