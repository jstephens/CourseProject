# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 00:41:16 2021

@author: Administrator
"""
import pandas as pd
from nltk.corpus import words
from nltk.corpus import wordnet as wn
import csv

def attempt1():
    hedonometerdf = pd.read_csv("Inputs/Hedonometer.csv", index_col=0)
    collection = pd.Series(hedonometerdf['Word'], index=hedonometerdf.index)
    
    print(type(collection))
    
    
    suffixes = ['ingly','ing','ed','ism','ist','s']
    
    
    # for word in collection:
    #     if len(word) > 4:
    #         for x in suffixes:
    #             suffixlength = len(x)
    #             if word.endswith(x):
    #                 tryoutword = word[:-suffixlength]
    #                 if tryoutword in words.words():
    #                     if tryoutword not in collection:
    #                         print(tryoutword)


def attempt2():
    d = []
    hedonometerdf = pd.read_csv("Inputs/Hedonometer.csv", index_col=0)
  #  hedonometerdf = hedonometerdf[~hedonometerdf['Happiness_Score'].between(2.5, 8.5, inclusive=False)]
    collection = pd.Series(hedonometerdf['Word'], index=hedonometerdf.index)
    csv_file = "Words.csv"
    for i in collection:
        if len(str(i))>4:
            try:
                test = wn.synsets(i)
                test2 = test[0].name()
                test1 = test2[:-5]
                if "_" not in test1:
                    if test1 not in collection.values:
                        #print(wn.synset(i).path_similarity(test))
                        f = [test1,hedonometerdf.loc[hedonometerdf['Word'] == i, 'Happiness_Score'].iloc[0],i]
                        d.append(f)
            except:
                pass
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(d)
            

def attempt3(sourcetext):
    d = []
    sourcetext = 'Inputs/Novels/' + sourcetext + '.txt'
    csv_file = sourcetext+'wordgen.csv'
    
    hedonometerdf = pd.read_csv("Inputs/Hedonometer.csv", index_col=0)
    collection = pd.Series(hedonometerdf['Word'], index=hedonometerdf.index)   
    with open(sourcetext, encoding="utf8") as f:
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
    mylist1 = mylist1.replace("“","")
    mylist1 = mylist1.replace("’","")
    mylist1 = mylist1.replace("’","")
    mylist1 = mylist1.replace(';','')
    mylist1 = mylist1.replace('(','')
    mylist1 = mylist1.replace(")",'')
    mylist1 = mylist1.replace('À','')
    mylist1 = mylist1.replace('‘','')    
    mylist1 = mylist1.replace('é','e')


    li = list(mylist1.split(" "))
    li = list(set(li))

    for i in li:
        if i not in collection.values:
            print(i)
            if len(str(i))>4:
                try:
                    test = wn.sysets(i)
                    test2= test[0].name
                    test1 = test2[:-5]
                    if "_" not in test1:
                        if test1 not in li:
                            f = [test1,hedonometerdf.loc[hedonometerdf['Word'] == i, 'Happiness_Score'].iloc[0],i]
                            d.append(f)
                except:
                    pass
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(d)
    
attempt3('Anna_Karenina')