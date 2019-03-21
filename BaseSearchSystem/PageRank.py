import ssl
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import os
import Utilits

##base ssl config for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

matrix = []

links = Utilits.get_all_lines('\\BaseSearchSystem\\web_pages\\links.txt')
for i in range(0, len(links)):
    links[i] = links[i].split()[1]

for link in links:
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, features="html5lib")
    
    links_in_link = soup.findAll('a')
    all_links = set()
    for link in links_in_link:
        try:
            href = link.attrs['href']
            if not href.startswith('http'):
                href = 'https://ria.ru' + href
            all_links.add(href)
        except KeyError:
            continue
    matrix.append(list(map(lambda l: 1 if all_links.__contains__(l) else 0, links)))

pagerank_file = open('pagerank.txt', "w")



for row in matrix:
    pagerank_file.write(''.join(map(str, row))+'\n')

pagerank_file.close()