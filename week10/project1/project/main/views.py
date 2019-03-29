from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Student


def index(request):
    return HttpResponse("Hello, Alexandra! Good luck! Avengers 4 are coming!!!")
def students_list(request):
    st='<div style="background-size:cover;background-image:url(https://photos.smugmug.com/Site-Backgrounds/Backgrounds/i-ZXFGmhw/0/38bf3e7c/L/41478616_xl-L.jpg)"><h1 style="color:blue; ">Our Students:<h1><ol>'
    for n in Student.objects.all():
        st+="<li style=""color:white;"">"+Student.__str__(n)+"</li>"
    st+="</ol></div>"
    return HttpResponse(st)