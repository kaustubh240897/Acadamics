from django.http import HttpResponse
from django.template import loader
from .models import Album

def index(request):
    all_albums =Album.objects.all()
    template=loader.get_template('recruiter/index.html')
    context={
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))

def detail(request,album_id):
    return HttpResponse("<h2> Details for Album id: " +str(album_id)+ "</h2>")