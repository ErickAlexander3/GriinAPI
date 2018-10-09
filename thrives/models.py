from django.db import models
from griin_auth.models import UserProfile

#thrive data
class Thrive(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(UserProfile, related_name='thrives', on_delete=models.CASCADE)
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
    story = models.TextField()

    class Meta:
        ordering = ('created',)
