from django.shortcuts import render,redirect
from .models import movie

from .forms import movieform


def index(request):
    Movie=movie.objects.all()
    context = {
         'movielist': Movie
    }
    return render(request,"index.html",context)
def details(request,movie_id):
    actor = movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie': actor})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name',)
        details = request.POST.get('details', )
        year = request.POST.get('year', )
        pic = request.FILES('pic')

        flim = movie(name=name,details=details,year=year, pic=pic)
        flim.save()
    return render(request,"add.html")
def update(request,id):
    Movie =movie.objects.get(id=id)
    form =movieform(request.POST or None,request.FILES,instance=Movie)
    if form. is_valid():
        form.save()
        return redirect("/")
    return render(request,'edit.html',{'movie':Movie,'form':form})

