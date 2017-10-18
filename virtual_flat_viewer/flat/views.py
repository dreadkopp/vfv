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
        #DEBUG
        logger = logging.getLogger(__name__)
        logger.error("cams:")
        val = request.POST['cams']
        val = json.loads(val)
        for el in val:
            string = "cam_id:" + str(el['id']) + "cam_pos_x:" + str(el['left']) + "cam_pos_y:" + str(el['top'])
            logger.error(string)
        logger.error("expose position")
        logger.error("left: " + str(exposeX) + "px; top: " + str(exposeY) + "px")
        logger.error("expose dimensions")
        logger.error("width: " + str(exposewidth) + "px; height: " + str(exposeheight) + "px")
        #calculate postition
        for el in val:
            #sanity check
            if (exposeX > el['left']) or ( el['left'] > (exposeX + exposewidth )) or (exposeY > el['top']) or ( el['top'] > (exposeY + exposeheight)):
                logger.error("camera " + str(el['id']) + " is not placed in image")
            else:
                relative_left = el['left'] - exposeX
                relative_top =  el['top'] - exposeY
                logger.error("relative position of cam " + str(el['id']) + " - left: " + str(relative_left) + " px; top: " + str(relative_top) + "px")
                relative_left_percent =  int( relative_left / exposewidth * 100 )
                relative_top_percent =   int( relative_top / exposeheight * 100 )
                logger.error("cam id: " + str(el['id']) + " - left: " + str(relative_left_percent) + "% - top: " + str(relative_top_percent) + "%")
                #update camera
                cam = camera.objects.get(pk=el['id'])
                cam.position_left = relative_left_percent
                cam.position_top = relative_top_percent
                cam.save()

        return "Kamerapositionen gesichert"
    else:
        return "Sie haben keine Erlaubnis dies zu tun. Um Änderungen vorzunehmen loggen Sie sich bitte zuerst ein."
