from pydoc_data.topics import topics
from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topic(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    webpage=Webpage.objects.all()
    d={'WS':webpage}

    return render(request,'display_webpage.html',d)
