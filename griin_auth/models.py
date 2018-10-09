from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel


#custom profiles
class UserProfile(PolymorphicModel):
    phone_number = models.CharField(max_length=15)

class IndividualProfile(UserProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # custom fields for user
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    GENDER_OPTIONS = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('N', 'Prefer Not To Say')
    )
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    date_of_birth = models.DateField()

class OrganizationProfile(UserProfile):
    admins = models.ManyToManyField(User, related_name='organizations')
    # custom fields for organization
    organization_name = models.CharField(max_length=100)