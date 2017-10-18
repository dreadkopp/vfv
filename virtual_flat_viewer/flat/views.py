from django.shortcuts import render

from django.views.generic import DetailView
from django_ajax.decorators import ajax
from cameras.models import camera

from .models import flat

import json
import logging

# Create your views here.

class ManageCamsView(DetailView):

    template_name = "web/pages/managecams.html"

    model = flat

@ajax
def setcamera(request):


    if request.user.is_authenticated:
        exposewidth = int(float(request.POST['exposewidth']))
        exposeheight = int(float(request.POST['exposeheight']))
        exposeY = int(float(request.POST['exposeY']))
        exposeX = int(float(request.POST['exposeX']))
        val = request.POST['cams']
        val = json.loads(val)
        #calculate postition
        for el in val:
            #sanity check
            if (exposeX > el['left']) or ( el['left'] > (exposeX + exposewidth )) or (exposeY > el['top']) or ( el['top'] > (exposeY + exposeheight)):
                pass
            else:
                relative_left = el['left'] - exposeX
                relative_top =  el['top'] - exposeY

                relative_left_percent =  int( relative_left / exposewidth * 100 )
                relative_top_percent =   int( relative_top / exposeheight * 100 )

                #update camera
                cam = camera.objects.get(pk=el['id'])
                cam.position_left = relative_left_percent
                cam.position_top = relative_top_percent
                cam.save()

        return "Kamerapositionen gesichert"
    else:
        return "Sie haben keine Erlaubnis dies zu tun. Um Änderungen vorzunehmen loggen Sie sich bitte zuerst ein."
