from django.shortcuts import render

# Create your views here.
from .models import house
from django.views.generic import TemplateView

class HouseView(TemplateView, house):
    def get_context_data(self, **kwargs):
        context = super(HouseView, self).get_context_data(**kwargs)
        context['houses'] = house.objects.all
        return context

    model = house
    template_name = "web/pages/house.html"



class FlatView(TemplateView):
    model = house
    template_name = "web/pages/flat.html"



class CameraView(TemplateView):
    model = house
    template_name = "web/pages/camera.html"
