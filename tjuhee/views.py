from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#메인 화면 만들기
def test(request):
    path=request.path
    resultstr=''
    if path =='tjuhee/test':
        resultstr='<h1>여기는 home 입니다.</h1>'
    else:
        resultstr= '<h1>여기는 김주희 입니다.</h1>'
    return HttpResponse(resultstr)


#메인화면 test박건욱, test01유설영, test03김주희 테스트 중
def test(request):
    result = {}
    return render(request, 'tjuhee/test.html', context=result)


def test01(request):
    result = {}
    return render(request, 'tjuhee/test01.html', context=result)


def test03(request):
    result = {}
    return render(request, 'tjuhee/test03.html', context=result)

# 맵 보여주기
import folium

# 맵 보여주기
import folium

