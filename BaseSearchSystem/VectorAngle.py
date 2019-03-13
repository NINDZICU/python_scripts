import Utilits
import os
import pymorphy2
import math

morph = pymorphy2.MorphAnalyzer()
filename = "/TfIdf/TfIdf.txt"
words = [] 
indexs = []

def readWordsFromFile(filename):
    global words
    docs = Utilits.get_by_single_lines(filename)
    for doc in docs:
        words.append(doc[0])

def readIndexsByNumberStr(filename):
    global indexs
    with open(os.getcwd() + filename, "r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            #if i == number_str:
            indexs.append(line.split()[1:])

def calculateTfIdfRequestVector(search_string, setPositionInFile):
    idfVector = []
    words_search = search_string.split()
    idfCofs = Utilits.get_by_single_lines("/TfIdf/Idf.txt")
    maxCount = 0
    for word in words_search:
        count = words_search.count(word)
        if(count>maxCount):
            maxCount = count

    for position in setPositionInFile:
        word = idfCofs[position][0]
        idfCoef = idfCofs[position][1]
        idfVector.append((words_search.count(word)/maxCount)*float(idfCoef))
    return idfVector

def calculateLenghtVector(vector):
    length = 0.0
    for coord in vector:
        length += math.sqrt(float(coord)*float(coord))
    return length


#*idfCofs[number_str][1]
def calculateAngle(indexs, vector, setPositionInFile):
    lengthVectors = []
    for i in range(0, len(indexs[0])):
        lengthVectors.append(calculateLenghtVector(Utilits.column(indexs, i)))
    lengthIdfVector = calculateLenghtVector(vector)

    similarity = []
    for i in range(0, len(indexs[0])):
        cos = 0.0
        for j, position in enumerate(setPositionInFile):
            #print(indexs[position][i])
            #print(vector[j])
            cos += float(indexs[position][i]) * vector[j]
        if(lengthVectors[i] != 0 and lengthIdfVector != 0):
            similarity.append(cos/(lengthVectors[i]*lengthIdfVector))
    print(similarity)
    return similarity

def printSimilarityDocs(similarityMatrix):
    maxCos = similarityMatrix.index(max(similarityMatrix))
    print("doc " + str(maxCos+1))

def handleRequest(search_string, filename):
    global indexs
    positionInFile = set()
    words_search = search_string.split()
    for word in words_search:
        lematWord = morph.parse(word)[0].normal_form
        number_str = Utilits.find(words, lematWord)
        if(len(number_str)>0):
            positionInFile.add(number_str[0])
    readIndexsByNumberStr(filename)
    idfVector = calculateTfIdfRequestVector(search_string, positionInFile)
    similarity = calculateAngle(indexs, idfVector, positionInFile)
    if(len(similarity)>0):
        printSimilarityDocs(similarity)
    else: print("Ничего не найдено")

readWordsFromFile(filename)

while True:
    print("Введите строку поиска")
    search_string = str(input()).strip()
    handleRequest(search_string, filename)
