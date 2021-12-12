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

hedonometerdf = hedonometerdf[~hedonometerdf['Happiness_Score'].between(3.8, 6.9, inclusive=False)]

bookname='Stranger_in_a_Strange_Land'

bookfilepath= 'Inputs/novels/'+bookname+'.txt'
#charactersfilepath = 'Inputs/novels/'+bookname+'_characters.csv'

with open(bookfilepath, encoding='utf8') as f:
    booktext = list(f)
    
# with open(bookfilepath, encoding='cp1252') as f:
#     booktext = list(f)    
    
booktext = ' '.join(booktext)

textlength = len(booktext)

booktext = booktext.split("Chapter ")
#booktext = booktext.split("CHAPTER ")
#character_df = pd.read_csv(charactersfilepath)
    
#print(character_df)

maxword = ""
maxwordrating = 0
minword = ""
minwordrating = 8

scores = []
counts = []
chapters = []
bookarrofarrs = []
arrofdictionaries = []

for i in range(1,len(booktext)-1):
    score = 0
    count = 0
    chapterwords = {}
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
            chapterwords[booktext1[j].lower()] = individscore
            chapterarr.append(individscore)
            if individscore > maxwordrating:
                maxword = booktext1[j].lower()
                maxwordrating = individscore
            if minwordrating > individscore:
                minword = booktext1[j].lower()
                minwordrating = individscore
    bookarrofarrs.append(chapterarr)
    
    chapterwords1 = dict(sorted(chapterwords.items(), key=lambda item: item[1]))
    
    arrofdictionaries.append(chapterwords1)
            
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

totalscores=0
totalcounts=0

scores1 = scores
scores1.pop(0)
for i in scores1:
    totalscores+=i
counts1 = counts
counts1.pop(0)
for k in counts1:
    totalcounts+=1
    
print(maxword, " ",maxwordrating)
print(minword," ",minwordrating)

chapters1 = chapters
chapters1.pop(0)

arrofdictionaries.pop(0)

print(arrofdictionaries)
bookwideavgscore = totalscores/totalcounts


finaldataframecols = ['chapterno','score','words']
finaldataframe = pd.DataFrame(columns=finaldataframecols)

print("Average score across book: ",bookwideavgscore)
for i in range(0,len(chapters)-1):
    if scores[i] > bookwideavgscore:  # find the associated words for positive chapters
        print("yes: ",i," ",scores[i])
        specificchaptersdict = list(arrofdictionaries[i].items())
        themostestwords = specificchaptersdict[-5:]
    else:
        specificchaptersdict = list(arrofdictionaries[i].items())
        themostestwords = specificchaptersdict[0:5]
        
    dataframearr = [i+1,scores[i],themostestwords]
    finaldataframe.loc[len(finaldataframe)] = dataframearr
        
finaldataframe = finaldataframe.set_index('chapterno')
print(finaldataframe)

dfbookpath='./Inputs/novels/'+bookname+'_df.csv'

finaldataframe.to_csv(dfbookpath)















