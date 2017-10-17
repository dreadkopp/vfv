from django.shortcuts import render

from django.views.generic import DetailView
from .models import flat

# Create your views here.
class ManageCamsView(DetailView):

    template_name = "web/pages/managecams.html"
    model = flat
