from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import HomeObject,Info
def index(request):
    return HttpResponse("<style> body{background-size:cover;text-align:center;"
                        "background-image:"
                        "url(http://awallpapershub.com/wp-content/uploads/2018/05/Awesome-Minimalist-HD-Wallpaper.jpg)}"
                        "a{font-size:30px;color:purple;}a:hover{color:pink;}</style>"
                        "<a href=""/home"">HOME</a><br><a href=""/info"">INFO PAGE</a>")
def home(request):
    st = "<style>a:hover{color:pink;} body{background-size:cover;text-align:center;font-size:20px;color:white;" \
         "background-image:url(http://awallpapershub.com/wp-content/uploads/2018/05/Awesome-Minimalist-HD-Wallpaper.jpg)}" \
         "</style><h1>Home Page</h1><ul>"
    for n in HomeObject.objects.all():
        st += "<li>" + HomeObject.__str__(n) + "</li>"
    st += "</ul><a href=""http://127.0.0.1:8000/"">back</a>"
    return HttpResponse(st)
def info(request):
    st="<style> body{background-size:cover;text-align:center;font-size:20px;color:white;background-image:url(http://awallpapershub.com/wp-content/uploads/2018/05/Awesome-Minimalist-HD-Wallpaper.jpg)}a:hover{color:pink;}</style><h1>Info Page</h1><ul>"
    for n in Info.objects.all():
        st+="<li>"+Info.__str__(n)+"</li>"
        print("hello")

    st+="</ul><a href=""http://127.0.0.1:8000/"">back</a>"
    return HttpResponse(st)