from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from .models import Movie


def index(request):
    if request.POST.get('new_movie_name', ''):
        new_movie = Movie(movie_name=request.POST['new_movie_name'])
        new_movie.save()
    movies_list = Movie.objects.all()
    context = {'movies_list': movies_list}

    return render(request, 'movielist/index.html', context)
