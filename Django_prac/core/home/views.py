from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):

    people=[
        {'name': 'Archisha ','age': 19},
        {'name': 'Khushi ','age': 19},
        {'name': 'Mysha ','age': 7}
    ]
    return render(request,"index.html",context = {"people":people})

