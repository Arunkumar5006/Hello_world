# -*- coding: utf-8 -*-
"""Shopping Assistant.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XrgqGbWMdxA3XazjsTeX0A6CfFm5WWG1
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

name=input("Enter Product Name :  ")
query=name.replace(" ","%20")                            
my_url = 'https://www.flipkart.com/search?q='+query+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uClient = urlopen(my_url)
page_html=uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"_30jeq3 _1_WHN1"})
for i in containers:
  print(i)