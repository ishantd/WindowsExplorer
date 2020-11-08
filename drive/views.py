
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from drive.models import *

import re


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def created(request):
    if request.method == 'POST':
        event = request.POST.get('event')
        if 'FileCreatedEvent' in event:
            event = event.replace("'", '"')
            path = re.findall(r'"([^"]*)"', event)[0]
            name = path.split('/')[-1]
            extension = name.split('.')[-1]
            parent_path = path.replace(f'/{name}', "")
            parent = Directory.objects.get(path=parent_path)
            data = {
                'parent': parent,
                'name': name,
                'path': path,
                'extension': extension,
            }
            file, created = File.objects.get_or_create(**data)
            if created:
                print("File created in database")
        if 'DirCreatedEvent' in event:
            event = event.replace("'", '"')
            path = re.findall(r'"([^"]*)"', event)[0]
            name = path.split('/')[-1]
            parent_path = path.replace(f'/{name}', "")
            parent = Directory.objects.get(path=parent_path)
            data = {
                'parent': parent,
                'name': name,
                'path': path,
            }
            directory, created = Directory.objects.get_or_create(**data)
            if created:
                print("Directory created in database")
    return HttpResponse(status=200)