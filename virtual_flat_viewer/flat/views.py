from django.shortcuts import render

from django.views.generic import DetailView
from django_ajax.decorators import ajax

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
        #DEBUG
        logger = logging.getLogger(__name__)
        logger.error("cams:")
        val = request.POST['cams']
        val = json.loads(val)
        for el in val:
            string = "cam_id:" + str(el['id']) + "cam_pos_x:" + str(el['left']) + "cam_pos_y:" + str(el['top'])
            logger.error(string)
        return "Kamerapositionen gesichert"
    else:
        return "Sie haben keine Erlaubnis dies zu tun. Um Änderungen vorzunehmen loggen Sie sich bitte zuerst ein."
