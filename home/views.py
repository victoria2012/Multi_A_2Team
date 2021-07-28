from django.shortcuts import render
import pandas as pd

# Create your views here.

from django.http import HttpResponse

def green_home(request):
    result={}
    return render(request, 'green_home.html', context=result)

def projects(request):
    df=pd.read_csv('machinelearning/saves/result.csv')
    recommend_result = recommend({}, matrix, 10, similar_genre=True)
    pd.DataFrame(recommend_result, columns = ['Title', 'Correlation', 'Genre'])
    result={}
    return render(request, 'projects.html', result)

# request.GET['first']

def scrapping(request):
    df = pd.read_csv('/scrapping/saves/pd_data.csv')
    result = {df}
    return render(request, 'scrapping.html', context=result)


def machine(request):
    xArray = [0.46,0.39,0.38,0.35,0.32,0.31,0.29,0.29,0.28,0.27];
    yArray = ['이스케이프 룸 2: 노 웨이 아웃','미드나이트','명탐정 코난: 비색의 탄환','꽃다발 같은 사랑을 했다',
              '라야와 마지막 드래곤','보스 베이비 2','루카','오필리아','컨저링 3: 악마가 시켰다','랑종'];
    result = {'x_array':xArray, 'y_array':yArray}
    return render(request, 'machine.html', context=result)

