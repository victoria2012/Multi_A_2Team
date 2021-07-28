import bs4
import pandas as pd
import numpy as np
import requests
import csv
from web_config.settings import DATA_DIRS

class Naver:
    def n1(self):
        df = pd.read_csv(DATA_DIRS[0] + '\\pd_data.csv')
        print(df)

if __name__ == '__main__':
     Naver().n1();