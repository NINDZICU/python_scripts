import os
import math
import Utilits

words = []
lemms = []

for number in range(1, 100):
    doc = Utilits.get_all_lines("/lem_pages/" + str(number) + "_lem.txt")
    words = words + doc
    lemms.append(doc)

word_set = set(words) 
word_dict = {}

for word in word_set:
    doc_counter = 0
    for doc_words in lemms:
        if word in doc_words:
            doc_counter += 1
        continue
    word_dict[word] = doc_counter

results = []
idf_results = []

for word in word_set:
    result = word + " "
    idf = math.log(len(lemms) / word_dict[word])
    idf_result = word + " " + str(idf)
    for doc_words in lemms:
       word_count = doc_words.count(word)
       tf = word_count / len(doc_words)
       res = tf * idf
       result += str(res) + " "
       
    results.append(result)
    idf_results.append(idf_result)

with open(os.getcwd() + "/TfIdf/TfIdf.txt", "a", encoding="utf-8") as file:
    for line in results:
        file.write(line + "\n")

with open(os.getcwd() + "/TfIdf/Idf.txt", "a", encoding="utf-8") as file:
    for line in idf_results:
        file.write(line + "\n")



