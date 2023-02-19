from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 

def hello(request):
    passwords_url = reverse('muie')  # this returns the string `/passwords/`
    return HttpResponse(str(passwords_url))
    #return HttpResponse('hi')