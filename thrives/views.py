from django.shortcuts import render

from django.views.generic import FormView
from .models import ThriveForm

from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

@method_decorator(ensure_csrf_cookie, name='dispatch')
class TestView(FormView):
    template_name = 'form.html'
    form_class = ThriveForm
