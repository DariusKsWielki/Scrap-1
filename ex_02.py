URL1='https://en.wikipedia.org/wiki/Pawe%C5%82_Domaga%C5%82a'

page1=get(URL1)
bs1= BeautifulSoup(page1.content, 'html.parser')

a=bs1.find_all('span')[1].text
print(a)

b=bs1.find_all('li')[0].text
c=bs1.find_all('li')[1].text
d=bs1.find_all('li')[2].text
print(b+' '+c+' '+d)

lista=[]
for i in range(24, 44):
    e=bs1.find_all('li')[i].text
    lista.append(e)
print(lista)