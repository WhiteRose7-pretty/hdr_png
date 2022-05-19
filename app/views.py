import json
from django.shortcuts import render
from django.http import JsonResponse
import os
import base64
from django.core.files.base import ContentFile
from .engine import convert_hdr
from .models import *
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'app/log.html')


@csrf_exempt
def convert_hdr_to_png(request):
    data = json.loads(request.body)
    b64_string = data['image']
    file_name = data['file']
    data = ContentFile(base64.b64decode(b64_string), file_name)
    hdr = HDRImage.objects.create(file=data)
    hdr.save()
    os.chmod(hdr.file.path, 0o0774)
    png_path = convert_hdr(hdr.file.path)
    hdr.png_file.name = png_path
    hdr.save()

    with open(png_path, "rb") as png_file:
        b64_string = base64.b64encode(png_file.read()).decode('utf-8')

    json_response = {
        "file_name": file_name.split('.')[0] + '.png',
        "b64_string": b64_string,
    }

    return JsonResponse(json_response, safe=True)
