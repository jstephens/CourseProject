# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:07:08 2021

@author: Jamie Stephens
Evaluates positive/negative sentiment of text, broken down by chapter

Input: novel text containing chapters beginning with 'Chapter __', hedonometer word list
Output: heat map with character sentiment, by chapter

"""
import pandas as pd
from nltk.corpus import wordnet

hedonometerdf = pd.read_csv("Inputs/Hedonometer.csv", index_col=0)

bookname='The_Great_Gatsby'

rawfilepath= 'Inputs/Novels/'+bookname+'_processed.txt'
rawfilepathcharacters = 'Inputs/Novels/'+bookname+'_characters.csv'

with open(rawfilepath, encoding='cp1252') as f:
    booktext = list(f)
    
booktext = ' '.join(booktext)

booktext = booktext.split("CHAPTER ")
character_df = pd.read_csv(rawfilepathcharacters)
    
print(character_df)

for i in range(0,len(booktext)-1):
    if len(booktext[i]) < 40:
        del booktext[i]

scores = []
counts = []
for i in range(0,len(booktext)-1):
    score = 0
    count = 0
    booktext1 = booktext[i].split(" ")
    print("Chapter number: ",i)
    print("Chapter word count: ",len(booktext1))
    if len(booktext1) > 100:
        for j in range(0,len(booktext1)-1):
            if booktext1[j].lower() in hedonometerdf.values:
                score += hedonometerdf.loc[hedonometerdf['Word'] == booktext1[j].lower(), 'Happiness_Score'].iloc[0]
                count += 1
        print("Average score: ",score/count)
        print("Count of all included words is: ",count)
        print("Average amongst all words",str(score/len(booktext1)))
        print("-------------")
        scores.append(score)
        counts.append(count)
        
print(scores)
print(counts)


