from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def test(request):
#     path=request.path
#     resultstr=''
#     if path =='tjuhee/test':
#         resultstr='<h1>여기는 home 입니다.</h1>'
#     else:
#         resultstr= '<h1>여기는 김주희 입니다.</h1>'
#     return HttpResponse(resultstr)

def test(request):
    result = {}
    return render(request, 'tjuhee/test.html', context=result)


def test01(request):
    result = {}
    return render(request, 'tjuhee/test01.html', context=result)


def test03(request):
    result = {}
    return render(request, 'tjuhee/test03.html', context=result)

def movie_link(request):
    result = {'section':'movie_link.html'}
    return render(request, ' tjuhee/test03.html', context=result)