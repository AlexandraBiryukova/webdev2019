from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Student


def index(request):
    return HttpResponse("Hello, Alexandra! Good luck! Avengers 4 are coming!!!")
def students_list(request):
    st='  <link href="https://fonts.googleapis.com/css?family=Gruppo" rel="stylesheet">' \
       '<style> li{white-space:nowrap;margin:10px;}ol{ width:700px;box-shadow:0px 0px 20px white;border-radius:20px; border:2px solid white;}' \
       'body{background-size:cover;font-family:Gruppo;color:white;'\
       'background-image:url(https://photos.smugmug.com/Site-Backgrounds/Backgrounds/i-ZXFGmhw/0/38bf3e7c/L/41478616_xl-L.jpg);}</style><h1>Our Students:<h1><ol>'
    for n in Student.objects.all():
        st+="<li>"+Student.__str__(n)+"</li>"
    st+="</ol></div>"
    return HttpResponse(st)