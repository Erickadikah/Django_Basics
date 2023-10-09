from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Takes a request and returns a response
# request handler

def say_hello(request):
    return render(request, 'index.html', { 'name': 'John'})