import os

def get_all_lines(fileName):
    with open(os.getcwd() + fileName, "r", encoding="utf-8") as file:
        content = file.readlines()
    return [x.strip() for x in content]

def get_by_single_lines(fileName):
    with open(os.getcwd() + fileName, "r", encoding="utf-8") as file:
        arr = []
        for line in file:
            arr.append(line.split())
        return arr


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def column(matrix, i): 
    return [row[i] for row in matrix]

def getIndexLink(matrix, i):
    return {a : row for a, row in enumerate(matrix) if row[i] == "1"}
