import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"


r = requests.get(url)
htmlContent = r.content
print(htmlContent)


soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

title = soup.title

print(type(title.string))
print(type(soup))
print(type(title))
print(type(title.string))

paras = soup.find_all('p')
print(paras)


anchors = soup.find_all('a')
print(anchors)


print(soup.find('p')['class'])
print(soup.find('p')['id'])                                                       


print(soup.find_all('p',class_='lead'))
print(soup.find('p').get_text())
print(soup.get_text())


anchors = soup.find_all('a')
all_links = set()

for link in anchors:
    if(link.get('href') != '#'):
        linkText = 'https://codewiy.com' + link.get('href')
        all_links.add(link)
        print(linkText)



markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))


imgpreview2 = soup.find(id="imgpreview2")
print(imgpreview2.contents)
for elem in imgpreview2.contents:
    print(elem)


