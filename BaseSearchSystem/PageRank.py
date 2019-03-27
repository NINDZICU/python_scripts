import ssl
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import os
import Utilits

##base ssl config for https
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# matrix = []

# links = Utilits.get_all_lines('\\BaseSearchSystem\\web_pages\\links.txt')
# for i in range(0, len(links)):
#     links[i] = links[i].split()[1]

# for link in links:
#     html = urllib.request.urlopen(link, context=ctx).read()
#     soup = BeautifulSoup(html, features="html5lib")
#     print(link)
#     links_in_link = soup.findAll('a')
#     all_links = set()
#     for link in links_in_link:
#         try:
#             href = link.attrs['href']
#             if not href.startswith('http'):
#                 href = 'https://ria.ru' + href
#             all_links.add(href)
#         except KeyError:
#             continue
#     matrix.append(list(map(lambda l: 1 if all_links.__contains__(l) else 0, links)))

# pagerank_file = open('pagerank.txt', "w")



# for row in matrix:
#     pagerank_file.write(''.join(map(str, row))+'\n')

# pagerank_file.close()

# def calculatePageRank(matrixTransition, links):
#     pageRankMatrix = {}
#     for i in range(0, len(matrixTransition)):
#         sumTransition = 0
#         for transition in Utilits.column(matrixTransition, i):
#             sumTransition += transition
#             pageRankMatrix.update({links[i]: sumTransition})
#         #pageRankMatrix.append(map (links[i], sumTransition))
#     print(pageRankMatrix)

# calculatePageRank(matrix, links)

def calculatePageRank2():
    d = 0.85
    pageLinks = Utilits.get_all_lines('\\BaseSearchSystem\\pagerank.txt')
    pageRankMatrix = {i : 1/100 for i in range(100)}
    for j in range(1000):
        for i in range(0, len(pageLinks)):
            dictLinks = Utilits.getIndexLink(pageLinks, i)
            sum = 0
            for key in dictLinks.keys():
                sum += pageRankMatrix[key] / dictLinks[key].count("1")
            pageRankMatrix[i] = ((1 - d) / len(pageLinks)) + d * sum

    data_sorted = {k: v for k, v in sorted(pageRankMatrix.items(), key = lambda x: x[1], reverse = True)}
    links = Utilits.get_all_lines("/BaseSearchSystem/web_pages/links.txt")    

    with open(os.getcwd() + "/BaseSearchSystem/TruePageRank.txt", "a", encoding="utf-8") as file:
        for l in data_sorted.keys():        
            file.write(links[l] + ": " + str(data_sorted[l]) + "\n")

calculatePageRank2()
