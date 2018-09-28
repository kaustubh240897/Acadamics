from django.http import HttpResponse
#from django.template import loader
from django.http import Http404
from django.shortcuts import render
from .models import Album

def index(request):
    all_albums =Album.objects.all()
   # template=loader.get_template('recruiter/index.html')
    context={'all_albums': all_albums,}
    return render(request,'recruiter/index.html',context)

def detail(request,album_id):
    try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request,'recruiter/detail.html',{'album': album})

