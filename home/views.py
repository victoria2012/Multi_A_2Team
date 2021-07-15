from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    result = {'first':'Multi',
              'second':'2Team_project'
              }
    return render(request, 'index.html',context=result)

