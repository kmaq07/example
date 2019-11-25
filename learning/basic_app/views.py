from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    response = HttpResponse()
    response.write('<h1>DATATECH.IN WEBSITE</h1>')
    response.write('<hr>')
    response.write('<p>This is a training page</p>')
    return response