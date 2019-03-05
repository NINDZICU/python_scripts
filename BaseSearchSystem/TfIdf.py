import os
import math
from collections import Counter

words = []
lemms = []

def get_all_lines(fileName):
    with open(os.getcwd() + fileName, "r", encoding="utf-8") as file:
        content = file.readlines()
    return [x.strip() for x in content]

for number in range(1, 100):
    doc = get_all_lines("/BaseSearchSystem/lem_pages/" + str(number) + "_lem.txt")
    words = words + doc
    lemms.append(doc)

word_dict = Counter(words) 

results = []

for word in word_dict:
    result = word + " :"
    for doc_words in lemms:
       word_count = doc_words.count(word)
       tf = word_count / len(doc_words)
       idf = math.log(len(lemms) / word_dict[word])
       res = tf * idf
       result += str(res) + " "
    results.append(result)

with open(os.getcwd() + "/BaseSearchSystem/TfIdf/TfIdf.txt", "a", encoding="utf-8") as file:
    for line in results:
        file.write(line + "\n")



