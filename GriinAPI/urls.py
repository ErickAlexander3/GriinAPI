"""GriinAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from rest_framework import routers
from allauth.account.views import confirm_email as allauthemailconfirmation

from thrives.views import UserViewSet, ThriveViewSet

#API router
router = routers.DefaultRouter()
router.register(r'thrives', ThriveViewSet)

urlpatterns = [
    #webapp URLs
    path('', include('webapp.urls')),
    url(r'^accounts/', include('allauth.urls')),
    #API URLs
	path('API/', include(router.urls)),
    path('API/s3direct/', include('s3direct.urls')),
    #overriden REST authentication links
    url(r'^API/rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', allauthemailconfirmation, name="account_confirm_email"), 
    #REST authentication
    path('API/rest-auth/', include('rest_auth.urls')),
    path('API/rest-auth/registration/', include('rest_auth.registration.urls')),
    #for login in the browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
