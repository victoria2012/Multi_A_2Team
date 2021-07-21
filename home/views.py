from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    path=request.path
    resultstr=''
    if path =='/home':
        resultstr='<h1>여기는 home 입니다.</h1>'
    else:
        resultstr= '<h1>여기는 main 입니다.</h1>'
    return HttpResponse(resultstr)

# def index01(request):
#     result = {'first':'Multi',
#               'second':'2Team_project'
#               }
#     return render(request, 'index.html',context=result)

def index02(request):
    result = {'first':request.GET['first'],'second':request.GET['second']}
    return render(request, 'index.html',context=result)

def index01(request):
    mf = folium.Map([35.3369, 127.7306], zoom_start= 10)
    mf = mf._repr_html_()
    first = 'hwasa'
    result = {'mapfolium':mf, 'f01':first}
    return render(request, templates_name='index.html',context=result)

def index01(request):
    mf = folium.Map([35.3369, 127.7306], zoom_start= 10)
    mf = mf._repr_html_()
    first = 'hwasa'
    result = {'mapfolium':mf, 'f01':first}
    return render(request, templates_name='index.html',context=result)