#!/usr/bin/env python
# coding: utf-8
import requests
import bs4
from multiprocessing.dummy import Pool
import os

def handler(img):
    if img['src'].split('.')[-1].lower() not in new_picture_formats: return
    fname=os.path.join(".","imgs",img['src'].split('/')[-1])
    with open(fname, 'wb') as handle:
        try:
            response = requests.get(base_url+img['src'], stream=True)
        except Exception as err:
            return str(err)
        if not response.ok: print(response)
        for block in response.iter_content(1024):
            if not block:break
            handle.write(block)
    return fname

base_url = 'http://www.herdofwy.com/'

request = requests.get('http://www.herdofwy.com/adopteddogs.html')

soup = bs4.BeautifulSoup(request.text, 'html.parser')
imgs = soup.findAll('img')
imgs = set(imgs)

picture_formats = set()

for img in imgs:
    picture_formats.add(img['src'].split('.')[-1].lower())

new_picture_formats = picture_formats.copy()
for pic_format in picture_formats:
    if pic_format not in ['gif', 'jpg', 'png', 'jpeg']: 
        new_picture_formats.remove(pic_format)

if not os.path.exists('./imgs'): os.makedirs('./imgs')

pool=Pool(16)
for name in pool.imap(handler,imgs):
    print(name)