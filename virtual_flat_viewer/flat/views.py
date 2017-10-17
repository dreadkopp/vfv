from django.shortcuts import render

from django.views.generic import DetailView
from django_ajax.decorators import ajax

from .models import flat

import json

# Create your views here.

class ManageCamsView(DetailView):

    template_name = "web/pages/managecams.html"
    model = flat

@ajax
def setcamera(request):

    #parse json to array , set new values to cams
    data = request.POST.data
    return
