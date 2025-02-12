# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:04:27 2021

@author: Jamie Stephens

Locates named entities, minimizing duplicates and surnames 

Input: raw text of novel containing chapters beginning with 'Chapter __'
Output: character list and modified novel text

"""

import time
import re
import spacy
import neuralcoref
import csv

start = time.time()

nlp = spacy.load('en_core_web_sm')  # load the model

bookname='Les_Miserables'

rawfilepath= 'Inputs/novels/'+bookname+'.txt'
# with open(rawfilepath, encoding="utf8") as f:
#     booktext = list(f)

with open(rawfilepath, encoding="cp1252") as f:
    booktext = list(f)    

booktext = ' '.join(booktext)
booktext = booktext.replace("Chapter",'CHAPTER')
booktext = booktext.replace("'s","")
booktext = booktext.replace("’s","")
booktext = booktext.replace("——"," ")
booktext = booktext.replace("-"," ")
booktext = booktext.replace("—"," ")
booktext = booktext.replace("\n"," ")
x = booktext.split("CHAPTER ")
    
def findlastnames():
    titles = ['mr.','miss','mr','mister','monsieur','mistress','master','missus','ms.','mrs.','mrs','ms','lord']

    suspectedsurnamesdict = {}
    
    for i in x:
        individualchapterwords = i.lower().split(" ")
        for j in titles:
            for k in individualchapterwords:
                if k == j:
                    next_word = individualchapterwords[individualchapterwords.index(j) + 1].strip()
                    next_word = re.sub(r'[^\w\s]','',next_word)
                    if next_word in suspectedsurnamesdict:
                        suspectedsurnamesdict[next_word] += 1
                    elif next_word not in suspectedsurnamesdict:
                        suspectedsurnamesdict[next_word] = 1

    definitelastnamesarr = []
    
    for i in suspectedsurnamesdict:
        if str(i) + "es" in suspectedsurnamesdict or str(i) + "s" in suspectedsurnamesdict:
            print(i, " yes")
            for n in x:
                individualchapterwords = n.lower().split(" ")
                for p in individualchapterwords:
                    if p.lower() == str(i)+"es" or p.lower() == str(i)+"s":
                        previous_words = [individualchapterwords[individualchapterwords.index(p)-3].strip(),individualchapterwords[individualchapterwords.index(p)-2].strip(),individualchapterwords[individualchapterwords.index(p)-1].strip()]
                        print(previous_words, " ",p)
                        if "the" in previous_words:
                            if i not in definitelastnamesarr:
                                definitelastnamesarr.append(i)
                                
    return definitelastnamesarr

def neuralco():
    neuralcoref.add_to_pipe(nlp)
    newx = ""
    
    j = 1
    for i in x:
        doc = nlp(i)  # get the spaCy Doc (composed of Tokens)
        newtext = doc._.coref_resolved
        text = "CHAPTER "+str(j)+"\n"
        newx = newx + text + newtext
        j += 1
        
    exportfilename = './Inputs/novels/'+bookname+'_processed.txt'
    text_file = open(exportfilename, "wt")
    text_file.write(newx)
    text_file.close()
    
    print("Processed version of ",bookname," completed.")
    
    dict1={}
    
    newx = booktext.replace("'s","")
    newx = booktext.replace("’s","")
    newx = booktext.replace("——","")
    newx = booktext.replace("-"," ")
    newx = booktext.replace("—"," ")
    newx = booktext.replace("'s","")
    newx = newx.replace("——"," ")
    newx = newx.replace("-"," ")
    newx = newx.replace("—"," ")
    newx = newx.split("CHAPTER ")
    
    for z in newx:
        y1 = z.split(" ")
        for mn in y1:
            nlpped = nlp(mn)
            for word in nlpped.ents:
                if word.label_ == 'PERSON':
                    if word.text in dict1.keys():
                        dict1[word.text] += 1
                    elif word.text not in dict1.keys():
                        dict1[word.text] = 1
                
    sorted_keys = sorted(dict1, key=dict1.get)
    
    sorted_dict = {}
    for w in sorted_keys:
        sorted_dict[w] = dict1[w]
    
    for k, v in sorted_dict.items():
        print(k, " ",v)
   
    characterfilepath = './Inputs/novels/'+bookname+'_characters.csv'
    characterfile = open(characterfilepath, "w")

    writer = csv.writer(characterfile)
    
    for key, value in sorted_dict.items():
        writer.writerow([key, value])
    
    characterfile.close()
    return sorted_dict

def sort_entities(dict1):
    loop = True
    while loop == True:
        for k, v in dict1.items():
            print(list(dict1.keys()).index(k), " ",k, v)
        userinput = input("Type the numbers of character1, character2 and press enter to consolidate.\nCharacter1 here means the primary character.\nPress S to save character list.\n")
    
neuralco()

#sort_entities(dict1)

    
end = time.time()
print(bookname," took ",end - start," time to complete")

