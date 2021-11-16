# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 00:41:16 2021

@author: Administrator
"""
import pandas as pd
from nltk.corpus import words

hedonometerdf = pd.read_csv("Inputs/Hedonometer.csv", index_col=0)
collection = pd.Series(hedonometerdf['Word'], index=hedonometerdf.index)

print(type(collection))


suffixes = ['ingly','ing','ed','ism','ist','s']


for word in collection:
    if len(word) > 4:
        for x in suffixes:
            suffixlength = len(x)
            if word.endswith(x):
                tryoutword = word[:-suffixlength]
                if tryoutword in words.words():
                    if tryoutword not in collection:
                        print(tryoutword)