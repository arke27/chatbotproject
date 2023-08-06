from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.t

def index(r):
    return HttpResponse('<h1> welcome in chatboat project')
