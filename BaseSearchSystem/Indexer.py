import os
import pymorphy2

words = []

lemms = []

def get_all_lines(fileName):
    with open(os.getcwd() + fileName, "r", encoding="utf-8") as file:
        content = file.readlines()
    return [x.strip() for x in content]

# for number in range(1, 100):
#     doc = get_all_lines("/BaseSearchSystem/lem_pages/" + str(number) + "_lem.txt")
#     words = words + doc
#     lemms.append(doc)

# words_set = list(set(words))

# # print(words_set)

# results = []

# for lem in words_set:
#     result = lem + ":"
#     for i in range(0, 99):
#         if lem not in lemms[i]:
#             result = result + "0"
#             continue
        
#         result = result + "1"

#     results.append(result)

# # print(results)

# with open(os.getcwd() + "/BaseSearchSystem/index/index.txt", "a", encoding="utf-8") as file:
#     for line in results:
#         file.write(line + "\n")

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
    
morph = pymorphy2.MorphAnalyzer()

while True:
    res = ""
    words = str(input()).strip()
    all_links = []
    for search_string in words.split():
        lematText = morph.parse(search_string)[0].normal_form
        lines = get_all_lines("/BaseSearchSystem/index/index.txt")
        find_result = [l for l in lines if l.startswith(lematText)]
        string = find_result[0]
        if string is None:
            continue
        
        index = string.index(":")
        string = string[index+1:]
        all_links.append(string)
        #
    
    for i in range(0, 99):
        boolean = False
        for lem in all_links:
            if (lem[i] == "0"):
                boolean = False
                break
            boolean = True
        if boolean:
            res = res + "1"
        else:
            res = res + "0"

    indexes = find(res, "1")
    links = get_all_lines("/BaseSearchSystem/web_pages/links.txt")
    for l in indexes:
        print(links[l])

