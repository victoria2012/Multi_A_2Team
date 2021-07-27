from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def green_home(request):
    result={}
    return render(request, 'green_home.html', context=result)

def projects(request):
    result = dict()
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row  # 컬럼 사용하게해줘
    curs = conn.cursor()

    # economics
    curs.execute('select * from main.polls_moviereview where id=')
    data = curs.fetchall()
    for row in data:
        print(row['title'], ':', row['code'])
    result['rows'] = data
    return render(request, 'projects.html', result)

def machine(request):
    context={
        'section':'machine.html'
    }
    return render(request, 'green_home.html', context)
 # result = {'title':request.GET['title'],
    #           'code':request.GET['code'],
    #           'genre':request.GET['genre'],
    #           'nation':request.GET['nation'],
    #           'director':request.GET['director'],
    #           'actor': request.GET['actor']
    #           }

# request.GET['first']

def scrapping(request):
    result = {}
    return render(request, 'scrapping.html', context=result)

def machine(request):
    result = {}
    return render(request, 'machine.html', context=result)