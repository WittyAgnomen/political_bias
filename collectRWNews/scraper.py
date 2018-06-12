from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.keys import Keys
# import time
# import itertools
# import csv
from random import randint
import pandas as pd
import requests
import datetime

# get collection date
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
sname = now.strftime("%Y%m%d")


def get_article_contents(url):
    try:
        r = requests.get(url)
        return r.text
    except:
        return "error with url"


df = pd.DataFrame(columns=['date_collected', 'source', 'article_reference', 'article'])

driver = webdriver.Chrome()

# load sites to try
sites = list(pd.read_csv('sites.csv')['sites'])


for s in sites:
    try:
        driver.get(s)
        articles = driver.find_elements_by_css_selector('article')

        # loop through articles
        for a in articles:
            v = date
            w = s
            x = a.find_element_by_css_selector('a').get_attribute('href')
            y = get_article_contents(x)
            df.loc[len(df)] = [v, w, x, y]

    except:
        df.loc[len(df)] = [date, s, 'E: error with scraper', '']

df.to_csv(sname + ".csv")

driver.close()
