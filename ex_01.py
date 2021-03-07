from bs4 import BeautifulSoup
from requests import get

URL='http://www.pythonscraping.com/pages/page3.html'
page=get(URL)
bs= BeautifulSoup(page.content, 'html.parser')
a=bs.find_all('span')[1].text
b=bs.find_all('span')[2].text
c=bs.find_all('span')[3].text
d=bs.find_all('span')[4].text
print(a+' '+b+' '+c+' '+d)

page=get(URL)
bs= BeautifulSoup(page.content, 'html.parser')
c=bs.find_all('td')[16].text
print(c)

page=get(URL)
bs= BeautifulSoup(page.content, 'html.parser')
c=bs.find_all('div')[2].text
print(c)