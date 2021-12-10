# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:09:12 2021

@author: Jamie Stephens
"""

import pandas as pd
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os
from nltk.corpus import wordnet

hedonometerdf = pd.read_csv("Inputs/Hedonometer2.csv", index_col=0)

hedonometerdf2 = hedonometerdf[~hedonometerdf['Happiness_Score'].between(4.5, 6.5, inclusive=False)]

with open('Inputs/Novels/Crime_and_Punishment.txt', encoding="utf8") as f:
    mylist = list(f)

mylist1 = ' '.join(mylist)

mylist1 = mylist1.replace('\n','')
mylist1 = mylist1.replace('.','')
mylist1 = mylist1.replace(',','')
mylist1 = mylist1.replace('-',' ')
mylist1 = mylist1.replace('?','')
mylist1 = mylist1.replace('!','')
mylist1 = mylist1.replace('—',' ')
mylist1 = mylist1.replace(':','')
mylist1 = mylist1.replace("”","")
mylist1 = mylist1.replace("'s","")
mylist1 = mylist1.replace("'ve","")
mylist1 = mylist1.replace("“","")
mylist1 = mylist1.replace("’s","")
mylist1 = mylist1.replace("’ve","")
mylist1 = mylist1.replace(';','')
mylist1 = mylist1.replace('I’ll','I will')
mylist1 = mylist1.replace(')','')
mylist1 = mylist1.replace('(','')


x = mylist1.split("CHAPTER ")

for i in range(0,len(x)-1):
    if len(x[i]) < 40:
        del x[i]

for i in range(0,len(x)-1):
    score = 0
    count = 0
    x1 = x[i].split(" ")
    
    print("Chapter number: ",i)
    print("Chapter word count: ",len(x1))
    for j in range(0,len(x1)-1):
        if x1[j].lower() in hedonometerdf.values:
            score += hedonometerdf.loc[hedonometerdf['Word'] == x1[j].lower(), 'Happiness_Score'].iloc[0]
            count += 1
    print("Average score: ",score/count)
    print("Count is: ",count)
    print("-------------")
    print(x1)

# new hedonometer word generation
# for i in range(0,len(x)-1):
#     x1 = x[i].split(" ")
#     for j in range(0,len(x1)-1):
#         if x1[j].lower() not in hedonometerdf.values:
#             synonyms = []
#             for syn in wordnet.synsets(x1[j].lower()):
#                 for l in syn.lemmas():
#                     synonyms.append(l.name())
#             print(x1[j].lower())
#             print("-----")
#             print(synonyms)