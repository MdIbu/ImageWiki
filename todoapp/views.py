
from django.shortcuts import render
from django.http import HttpResponse
import re,time
import requests
import wikipedia
from bs4 import BeautifulSoup
def index(request):
    return render(request,'base.html')

def getdata(url): 
    r = requests.get(url)
    return r.text 
        

def topic(request):
    if request.GET['submit'] == 'Images':
        img_topic = request.GET["imgtopic"]
        GOOGLE_IMAGE = ('https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q=')
        resultspeak= ("showing images on" + img_topic)
        que = img_topic
        print(que)
        n_images = 19
        print('Start searching...')
        searchurl = (GOOGLE_IMAGE + '+'.join(que))
        ibu = searchurl
        print(searchurl)
        print(ibu)
        htmldata = getdata(ibu) 
        soup = BeautifulSoup(htmldata, 'html.parser') 
        links = soup.find_all('img',limit=n_images)
        i=[]
        for item in links:
            img = (item['src'])
            src = img
            print(img)
            i.append(img)
        i.pop(0)
        return render(request,'images.html',{'res': img_topic,'i': i})
    else:
        wiki_topic = request.GET["imgtopic"]
        wikifulltopic=("what is " + wiki_topic)
        result = wikipedia.summary(wikifulltopic, sentences = 5) 
        print(result)
        return render(request,'wiki.html',{'res': result,'topic': wiki_topic})