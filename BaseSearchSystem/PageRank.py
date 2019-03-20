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

for link in links:
    html = urllib.request.urlopen(link.split()[1], context=ctx).read()
    soup = BeautifulSoup(html, features="html5lib")
    try:
        all_links = [el['href'] for el in soup.findAll('a')]
    except KeyError:
        pass

    matrix.append(list(map(lambda link: 1 if all_links.__contains__(link) else 0, links)))

pagerank_file = open('pagerank.txt', "w")

for row in matrix:
    pagerank_file.write(''.join(map(str, row))+'\n')

pagerank_file.close()