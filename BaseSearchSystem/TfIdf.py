import os
import math

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

for word in word_set:
    result = word + ": "
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



