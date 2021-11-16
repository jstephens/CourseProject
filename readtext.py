# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:09:12 2021

@author: Jamie Stephens
"""

import pandas as pd
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os

hedonometerdf = pd.read_csv("Inputs/Hedonometer.csv", index_col=0)

hedonometerdf = hedonometerdf[~hedonometerdf['Happiness_Score'].between(3.5, 7.5, inclusive=False)]

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

for i, j in hedonometerdf.iterrows():
    print(i, j)


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
    