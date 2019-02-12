from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from collections import deque
import re

startLink = "https://ria.ru/"
q = deque()
links = [startLink]

compareText = ""

def saveFromInternet(link, number):
	global compareText
	
	nameFile = "web_pages/"+ str(number) + ".txt"
	with open(nameFile, "a", encoding="utf-8") as file:
		req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
		with urlopen(req) as url:
			content = url.read().decode()
			soup = BeautifulSoup(content, 'html.parser')
			file.write(link + '\n')
			for par in soup.find_all(['p','h1', 'h2', 'span', 'strong', 'em']):
				text = par.get_text()
				isTime = re.match(r'^\d{2}:\d{2}$', text)
				if(not(text.isspace() or len(text) == 0) and isTime == None and compareText != text):
					compareText = text
					file.write(par.get_text() + '\n')
					
			for par in soup.find_all ('div' , class_='article__text'):
				text = par.get_text()
				if(not(text.isspace() or len(text) == 0)):
						file.write(par.get_text() + '\n')
			if len(links) <150:
				parseLink(soup)
	if(number<100):
		saveFromInternet(q.popleft(), number+1)

def parseLink(soup):
	for link in soup.find_all('a', href=True):
		href = link['href']
		if(href not in links and re.match(startLink, href) != None):
			print(href)
			q.append(href)
			links.append(href)
	
saveFromInternet(startLink, 1)




