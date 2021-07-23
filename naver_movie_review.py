from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import pandas as pd


def get_movie_reviews(mcode, page_num=10):
    movie_review_df = pd.DataFrame(columns=("Title", "Score", "User"))
    url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=" + str(mcode) + "&target=after"
    idx = 0

    for _ in range(0, page_num):
        movie_page = urllib.request.urlopen(url).read()
        movie_page_soup = BeautifulSoup(movie_page, 'html.parser')

        review_list = movie_page_soup.find_all('td', {'class': 'title'})
        for review in review_list:
            title = review.find('a', {'class': 'movie color_b'}).get_text()
            score = review.find('em').get_text()
            user = review.find('a').get_text()
            # 유저 아이디를 찾아야 함!
            # review_text = review.find('a', {'class':'report'}).get('href').split(',')[2]
            movie_review_df.loc[idx] = [title, score, user]
            idx += 1
            print("#", end="")
        try:
            url = "https://movie.naver.com" + movie_review_soup.find('a', {'class': 'pg_next'}).get('href')
        except:
            break

    return movie_review_df
