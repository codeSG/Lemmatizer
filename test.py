# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:09:25 2017

@author: user
"""

from words_tagging import all_noun
from Declension import Declension_noun
from Stemming import stem
correct=0
incorrect=0
incorrect_words=[]
for s_type in all_noun:
    for noun in s_type:
        dec=Declension_noun(noun)
        print(dec)
        for row in dec:
            for col in row:
                if stem(col)==noun:
                    correct=correct+1
                else:
                    incorrect=incorrect+1
                    incorrect_words.append(col)
        print(correct,incorrect)

print(correct,incorrect)
print (incorrect_words)
incorrect_words=['अजाः', 'अजाभ्याम्', 'अजाभ्याम्', 'अजाभ्याम्', 
'अजानाम्', 'अजे', 'हे अजाः', 'विधौ', 'नरौ', 'नरः',
 'नरम्', 'नरौ', 'हे नरौ', 'श्रोत्रे', 'नेत्रे', 'कमले',
 'कमले', 'कमलयोः', 'कमलयोः', 'अजयोः', 'अजयोः',
 'कमलाभ्याम्','कमलाभ्याम्', 'कमलाभ्याम्', 'कमलानाम्', 'हे कमलाः']
for item in incorrect_words:
    print(item, stem(item))
    print("\n")