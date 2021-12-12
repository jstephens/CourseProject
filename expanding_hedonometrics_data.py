# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 19:17:55 2021

Functions to expand the hedonometrics dataset

Function 1: evaluateindividualbooks
Input: unprocessed novel text
Output: synonyms for manual addition to hedonometer dataset

Function 2: expandwordlist
Input: hedonometer word list
Output: most similar words, based on Wu-Palmer similarity, that don't apear in the dataset already

@author: Jamie Stephens
"""
import nltk
import pandas as pd
from nltk.corpus import wordnet
from nltk import pos_tag
synonyms = []

hedonometerdf = pd.read_csv("Inputs/Hedonometer.csv", index_col=0)


def evaluateindividualbooks():
    bookname='Lion_Witch_Wardrobe'
    
    rawfilepath= 'Inputs/Novels/'+bookname+'.txt'
    
    with open(rawfilepath, encoding='utf8') as f:
        booktext = list(f)
        
    booktext = ' '.join(booktext)
    
    booktext = booktext.replace('\n',' ')
    booktext = booktext.replace(',','')
    booktext = booktext.replace('-',' ')
    booktext = booktext.replace('?','')
    booktext = booktext.replace('!','')
    booktext = booktext.replace('—',' ')
    booktext = booktext.replace(':',' ')
    booktext = booktext.replace("”","")
    booktext = booktext.replace("'s","")
    booktext = booktext.replace("'ve","")
    booktext = booktext.replace("“"," ")
    booktext = booktext.replace("’s","")
    booktext = booktext.replace("’ve","")
    booktext = booktext.replace(';','')
    booktext = booktext.replace('I’ll','I will')
    booktext = booktext.replace(')','')
    booktext = booktext.replace('(','')
    booktext=booktext.replace(' The ',' ')
    booktext=booktext.replace(' I ',' ')
    booktext=booktext.replace(' the ',' ')
    booktext=booktext.replace(' A ','')
    booktext=booktext.replace(' a ',' ')
    booktext=booktext.replace('She','')
    booktext=booktext.replace(' she ',' ')
    booktext=booktext.replace(' he ',' ')
    booktext=booktext.replace(' his ',' ')
    booktext=booktext.replace(' him ',' ')
    booktext=booktext.replace(' Mr. ',' ')
    booktext=booktext.replace(' Mrs. ',' ')
    booktext=booktext.replace(' Lady ','')
    booktext=booktext.replace(' to ',' ')
    booktext=booktext.replace(' from ',' ')
    booktext=booktext.replace(' said ',' ')
    booktext=booktext.replace('"',' ')
    booktext=booktext.replace(' Miss ',' ')
    booktext = booktext.replace(" single ",' ')
    booktext = booktext.replace(" but ",' ')
    booktext=booktext.replace(' ’d ','')
    booktext = booktext.split("Chapter ")
    
    tagstolookat = ['JJ','JJR','JJS']
    
    wordstolookat = []
    for i in booktext:
        x = i.split(".")
        for j in x:
            j1 = j.split()
            tokens_tag = pos_tag(j1)
            for k in tokens_tag:
                if k[0] not in hedonometerdf.values:
                    if len(k[0]) > 3:
                        if k[1] in tagstolookat:
                            if k[0].lower() not in wordstolookat:
                                wordstolookat.append(k[0].lower())              
    
    for i in wordstolookat:
        greatestwordsimilarity = 0
        mostsimilarword = ""
        
        for j in hedonometerdf.values:
            try:
                syn1 = wordnet.synsets(i)[0]
                syn2 = wordnet.synsets(j[0])[0]
                if syn1.wup_similarity(syn2) > greatestwordsimilarity:
                    greatestwordsimilarity = syn1.wup_similarity(syn2)
                    mostsimilarword = syn2  
            except:
                pass
        if greatestwordsimilarity > 0:
            print("---------------")
            print("evaluating word ",i)
            print(greatestwordsimilarity)
            print(mostsimilarword)
            
        
def expandwordlist():
    for i in hedonometerdf.values:
        synonyms=[]
        for syn in wordnet.synsets(i[0]):
            for l in syn.lemmas():
                if l.name() not in hedonometerdf.values:
                    synonyms.append(l.name())
        if len(synonyms) > 0:
            print(i[0], " ",synonyms)

expandwordlist()

