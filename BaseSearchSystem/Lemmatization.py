import pymorphy2
import re

morph = pymorphy2.MorphAnalyzer()
dir = "lem_pages\\"

def readFromFile(name):
    f = open(name, encoding="utf-8")
    return clean_text(f.read())

def writeToFile(text, nameFile):
    with open(nameFile, "a", encoding="utf-8") as file:
        file.write(text +'\n')

def clean_text(text):
    text = re.sub("^\s+|\n|\r|\s+$", ' ', text)
    text = re.sub('[^\w\s]', '', text)
    text = re.sub('^M', '', text)
    text = re.sub(r'\s+', ' ', text)
    rus = re.compile(u'[^а-яА-Я ]')
    text = rus.sub('', text).strip()
    return text

def lemmatization():
    for i in range(1, 101):
        list1 = readFromFile("web_pages/"+ str(i) +".txt").split()
        for item in list1:
            lematText = morph.parse(item)[0].normal_form
            partOfSpeech = morph.parse(item)[0].tag.POS 
            # PRCL - частицы(бы, не) NPRO - местоимения CONJ - PREP -
            if(partOfSpeech != "CONJ" and partOfSpeech !="PREP" and partOfSpeech !="PRCL" and partOfSpeech !="NPRO"):
                writeToFile(lematText, dir + str(i) + "_lem.txt")
 
lemmatization()

print(morph.parse('items')[0].normal_form)
