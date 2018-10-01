# from django.http import HttpResponse
# #from django.template import loader
# from django.http import Http404
# from django.shortcuts import render,get_object_or_404
# from .models import Album,Song
#
#
# def index(request):
#     all_albums =Album.objects.all()
#    # template=loader.get_template('recruiter/index.html')
#     context={'all_albums': all_albums,}
#     return render(request,'music/index.html',context)
#
# def detail(request,album_id):
#     #album = Album.objects.get(pk=album_id)
#     album=get_object_or_404(Album,pk=album_id)
#     return render(request,'music/detail.html',{'album': album})
#
# def favourite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song=album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#             'album': album,
#             'error_message':"You did not selected valid song",
#         })
#     else:
#         selected_song.is_favourite=True
#         selected_song.save()
#         return render(request,'music/detail.html',{'album':album})
#

from django.views import generic
from .models import Album
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model=Album
    template_name='music/detail.html'


class AlbumCreate(CreateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']
    template_name = 'music/album_form.html'


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model =Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class= UserForm
    template_name='music/registration_form.html'

    #display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form' : form})

    #process from data
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)


            #clean and normalize data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user objects if credentials are correct
            user= authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('music:index')

        return render(request,self.template_name,{'form':form})





































