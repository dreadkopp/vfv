from django.shortcuts import render

# Create your views here.
from .models import house
from flat.models import flat
from cameras.models import camera
from django.views.generic import TemplateView, DetailView

class HouseView(TemplateView, house):


    def get_context_data(self, **kwargs):
        flats = flat.objects.all()
        houses = []
        for node in flats:
            houses.append(node.Haus)
        houses = list(set(houses))    
        context = super(HouseView, self).get_context_data(**kwargs)
        context['flats'] = flats
        context['houses'] = houses
        return context

    model = flat
    template_name = "web/pages/house.html"



class FlatView(DetailView):
    model = flat
    template_name = "web/pages/flat.html"



class CameraView(DetailView):
    model = camera
    template_name = "web/pages/camera.html"
