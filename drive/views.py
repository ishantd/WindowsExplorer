
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
    return HttpResponse(status=200)