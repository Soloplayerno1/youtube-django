from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Movie

def home(request):
    return HttpResponse("Home page")

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html',{'movies': data})

def detail(request, id):
    movie = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': movie})

def add(request):
    if request.method == "GET":
        return render(request, 'movies/add.html')
    else:
        title = request.POST.get('title')
        year = request.POST.get('year')
        movie = Movie(title=title, year=year)
        movie.save()
        return redirect('/movies')
    
def delete(request,id):
    try:
        Movie.objects.get(pk=id).delete()
    except:
        raise Http404("Movie does not exist!")
    return redirect('/movies/')
    
    