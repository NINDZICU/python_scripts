import os

words = []

def get_all_lines(fileName):
    with open(os.getcwd() + fileName, "r", encoding="utf-8") as file:
        content = file.readlines()
    return [x.strip() for x in content]

for number in range(1, 100):
    doc = get_all_lines("/BaseSearchSystem/lem_pages/" + str(number) + "_lem.txt")
    words = words + doc

words_set = list(set(words))

print(words_set)

for lem in words_set:
    