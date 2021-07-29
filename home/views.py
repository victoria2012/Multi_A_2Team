from django.shortcuts import render
import pandas as pd
import csv
import sqlite3
# from ssapp.models import Stock

# Create your views here.

from django.http import HttpResponse

def green_home(request):
    result={}
    return render(request, 'green_home.html', context=result)

def projects(request):
    result={}
    return render(request, 'projects.html', result)

# request.GET['first']

def scrapping(request):
    result = {}
    return render(request, 'scrapping.html', context=result)

def machine(request):
    xArray = [0.46,0.39,0.38,0.35,0.32,0.31,0.29,0.29,0.28,0.27];
    yArray = ['이스케이프 룸 2: 노 웨이 아웃','미드나이트','명탐정 코난: 비색의 탄환','꽃다발 같은 사랑을 했다',
              '라야와 마지막 드래곤','보스 베이비 2','루카','오필리아','컨저링 3: 악마가 시켰다','랑종'];
    result = {'x_array':xArray, 'y_array':yArray}
    return render(request, 'machine.html', context=result)


    # df=pd.read_csv('scrapping/df_movie.csv')
    # s = pd.DataFrame(df,columns=['Title','Correlation','Genre'] )
    # ss = []
    # for i in range(len(s)):
    #     st = (s['Title'][i], s['Correlation'][i], s['Genre'][i])
    #     ss.append(st)
    # #     for i in range(len(s)):
    # #         Stock.objects.create(Title=ss[i][0], Correlation=ss[i][1], Genre=ss[i][2])

    # conn = sqlite3.connect('saves/movie.db')
    # data.to_sql('test', conn)
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM test")
    # rows = cursor.fetchone()
    # for row in rows:
    #     print(row)