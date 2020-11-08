
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

@csrf_exempt
def deleted(request):
    if request.method == 'POST':
        event = request.POST.get('event')
        if 'FileDeletedEvent' in event:
            event = event.replace("'", '"')
            path = re.findall(r'"([^"]*)"', event)[0]
            try:
                file = File.objects.get(path=path).delete()
            except:
                print("Unable to delete, file does not exist")
        if 'DirDeletedEvent' in event:
            event = event.replace("'", '"')
            path = re.findall(r'"([^"]*)"', event)[0]
            try:
                directory= Directory.objects.get(path=path).delete()
                print("Directory deleted")
            except:
                print("Unable to delete, directory does not exist")
    return HttpResponse(status=200)

@csrf_exempt
def modified(request):
    if request.method == 'POST':
        event = request.POST.get('event')
        print(event)
        if 'FileModifiedEvent' in event:
            event = event.replace("'", '"')
            path = re.findall(r'"([^"]*)"', event)[0]
            file = File.objects.get(path=path)
            file.save()
    return HttpResponse(status=200)

# @csrf_exempt
# def moved(request):
#     if request.method == 'POST':
#         event = request.POST.get('event')
#         if 'FileCreatedEvent' in event:
#             event = event.replace("'", '"')
#             path = re.findall(r'"([^"]*)"', event)[0]
#             name = path.split('/')[-1]
#             extension = name.split('.')[-1]
#             parent_path = path.replace(f'/{name}', "")
#             parent = Directory.objects.get(path=parent_path)
#             data = {
#                 'parent': parent,
#                 'name': name,
#                 'path': path,
#                 'extension': extension,
#             }
#             file, created = File.objects.get_or_create(**data)
#             if created:
#                 print("File created in database")
#         if 'DirCreatedEvent' in event:
#             event = event.replace("'", '"')
#             path = re.findall(r'"([^"]*)"', event)[0]
#             name = path.split('/')[-1]
#             parent_path = path.replace(f'/{name}', "")
#             parent = Directory.objects.get(path=parent_path)
#             data = {
#                 'parent': parent,
#                 'name': name,
#                 'path': path,
#             }
#             directory, created = Directory.objects.get_or_create(**data)
#             if created:
#                 print("Directory created in database")
#     return HttpResponse(status=200)