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
import matplotlib.pyplot as plt

hedonometerdf = pd.read_csv("Inputs/Hedonometer.csv", index_col=0)

hedonometerdf = hedonometerdf[~hedonometerdf['Happiness_Score'].between(4.44, 6.17, inclusive=False)]

bookname='Pride_and_Prejudice'

rawfilepath= 'Inputs/Novels/'+bookname+'_processed.txt'
rawfilepathcharacters = 'Inputs/Novels/'+bookname+'_characters.csv'

with open(rawfilepath, encoding='cp1252') as f:
    booktext = list(f)
    
booktext = ' '.join(booktext)

textlength = len(booktext)

booktext = booktext.split("CHAPTER ")
character_df = pd.read_csv(rawfilepathcharacters)
    
print(character_df)

maxword = ""
maxwordrating = 0
minword = ""
minwordrating = 8

scores = []
counts = []
chapters = []
bookarrofarrs = []

for i in range(1,len(booktext)):
    score = 0
    count = 0
    chapterarr=[]
    booktext1 = booktext[i].split(" ")
    print("Chapter number: ",i)
    print("Chapter word count: ",len(booktext1))
    chapters.append(i)
    for j in range(0,len(booktext1)-1):
        if booktext1[j].lower() in hedonometerdf.values:
            individscore = hedonometerdf.loc[hedonometerdf['Word'] == booktext1[j].lower(), 'Happiness_Score'].iloc[0]
            score += individscore
            count += 1
            chapterarr.append(individscore)
            if individscore > maxwordrating:
                maxword = booktext1[j].lower()
                maxwordrating = individscore
            if minwordrating > individscore:
                minword = booktext1[j].lower()
                minwordrating = individscore
    bookarrofarrs.append(chapterarr)
            
    if score > 0 and count > 0:
        avgscore = score/count
    else:
        avgscore = 0
    print("Average score: ",avgscore)
    print("Count of all included words is: ",count)
    print("Average amongst all words",str(score/len(booktext1)))
    print("-------------")
    scores.append(avgscore)
    counts.append(count)
        
print(scores)
print(counts)

print(maxword, " ",maxwordrating)
print(minword," ",minwordrating)

for x in bookarrofarrs:
    for y in x:
        print(y)

plt.plot(chapters, scores)
plt.title('Book Sentiment')
plt.xlabel('Chapter')
plt.ylabel('Score')
plt.show()

