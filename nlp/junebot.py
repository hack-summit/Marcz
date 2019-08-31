#Web Scraping and Processing 

from googlesearch import search
import requests
from bs4 import BeautifulSoup
import wikipedia as wp

def cmethod(query):

    him=""

    try:
        him=wp.summary(query,sentences=100)
    except:
        b =search(query,num=1,stop=1)
        c=list(b)
        d=requests.get(c[0])
        e=BeautifulSoup(d.content,'html.parser')
        f=e.find_all('p')
        for i in f:
            him+=i.get_text()
    return him                 