import requests
import sqlite3
from bs4 import BeautifulSoup

path = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&date=20210721'
req = requests.get(path)
req.status_code
soup = BeautifulSoup(req.content, 'html.parser')

connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()

ranks = soup.select('img[width="14"]')

ranking1 = list()

for rank in ranks:
    ranking1.append(int(rank['alt'].strip()))

ranking1.insert(23, int('24'))

movies = soup.select('div.tit3 > a')

title1 = list()
for movie in movies:
    title1.append(movie.text.strip())

data = list(zip(ranking1,title1))
import pandas as pd
pd_data = pd.DataFrame(data, columns=['Ranking','Title'])

for index, row in pd_data.iterrows():
    ranking = row[0]
    title = row[1]
    try:
        cursor.execute("insert into dbapp_movieranking(ranking, title) values(?, ?)", (ranking, title))
        print(ranking, ' : ', title)
    except:
        pass

connect.commit()
connect.close()

