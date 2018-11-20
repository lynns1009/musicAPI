from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Music,Album


def home(request):
    albums = Album.objects.all()
    return render(request,'home.html',{'albums':albums})


def songs_list(request):
    songs=Music.objects.all()
    return render(request, 'song_list.html', {'songs': songs})


def song_detail(request,id):
    try:
        song=Music.objects.get(id=id)
    except Music.DoesNotExist:
        raise Http404("Song not found")
    return render(request,'song_detail.html',{'song':song})


def album_detail(request,id):
    try:
        album=Album.objects.get(id=id)
    except Album.DoesNotExist:
        raise Http404("Album not found")
    return render(request,'album_detail.html',{'album':album})