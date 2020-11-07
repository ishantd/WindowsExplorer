
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def created(request):
    print("created")
    return HttpResponse("Created!")