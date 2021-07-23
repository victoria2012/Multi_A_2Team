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

def maps(request):
    result = {}
    return render(request, 'maps.html', context=result)


# def index(request):
#     path=request.path
#     resultstr=''
#     if path =='/home':
#         resultstr='<h1>여기는 home 입니다.</h1>'
#     else:
#         resultstr='<h1>여기는 main 입니다</h1>'
#
#     return HttpResponse(resultstr)

# def index01(request):
#     result = {'first':'Multi',
#               'second':'2Team_project'
#               }
#     return render(request, 'index.html',context=result)
#
# def index02(request):
#     result = {'first':request.GET['first'],'second':request.GET['second']}
#     return render(request, 'index.html',context=result)

