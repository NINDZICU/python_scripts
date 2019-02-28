import os

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

words_set = list(set(words))

# print(words_set)

results = []

for lem in words_set:
    result = ""
    for i in range(0, 99):
        if lem not in lemms[i]:
            result = result + "0"
            continue
        
        result = result + "1"

    results.append(result)

# print(results)

with open(os.getcwd() + "/BaseSearchSystem/index/index.txt", "a", encoding="utf-8") as file:
    for line in results:
        file.write(line + "\n")
    