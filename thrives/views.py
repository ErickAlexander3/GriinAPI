from django.shortcuts import render

from django.views.generic import FormView
from .models import ThriveForm

class TestView(FormView):
    template_name = 'form.html'
    form_class = ThriveForm
