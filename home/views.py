from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def green_home(request):
    result={}
    return render(request, 'green_home.html', context=result)

def projects(request):
    result={}
    return render(request, 'projects.html', result)

# request.GET['first']
def maps(request):
    mf = folium.Map([35.3369, 127.7306], zoom_start= 10)
    mf = mf._repr_html_()
    first = 'hwasa'
    result = {'mapfolium':mf, 'f01':first}
    return render(request, templates_name='maps.html',context=result)
