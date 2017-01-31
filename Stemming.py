# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 09:11:08 2016

@author:sourabh garg
"""

from Declension import *
from Declension_noun_forms import *
from words_tagging import *
from Trie import *
from Tokenize import *

def search_noun(word,noun):
    ''' Searches word in the declension of the noun'''
    declension=Declension_noun(noun)
    #print(declension)
    for case in declension:
        for number in case:
            if word==number:
                return True

def search_pronoun(word):
    ''' Searches word in the declension of the pronoun'''
    for pro in pronoun:
        declension=Declension_pronoun(pro,'masculine')
        for case in declension:
            for number in case:
                if word==number:
                    return pro
        declension=Declension_pronoun(pro,'feminine')
        for case in declension:
            for number in case:
                if word==number:
                    return pro
        declension=Declension_pronoun(pro,'neuter')
        for case in declension:
            for number in case:
                if word==number:
                    return pro
def search_unique(word):
    ''' Searches word in the declension of the unique noun words'''
    for u in unique:
        declension=eval(u)
        for case in declension:
            for number in case:
                if word==number:
                    return u
def find_stem(word):
    for i in range(len(all_noun)):
        if word in all_noun[i]:
            stem_t=dict_noun[i]
            #print(stem_t)
            return stem_t
            
def stem(word):
    '''it returns the stem for any inflected word provided'''
    if search_pronoun(word) != None:
        return search_pronoun(word)
    elif search_unique(word)!=None:
        return search_unique(word)
    else:
        mytrie=Trie()
        for stem_cls in words_tagging.all_noun:
            for noun in stem_cls:
                mytrie.insert(complete_tokenize(noun))
        lis=complete_tokenize(word)
        #print(lis)
        length=len(lis)
        #print(length)
        
        
        for i in range(length):
            serch=lis[:length-i]
            #print(serch)
            for trie_word in mytrie.find(serch):
                joined_word=join(trie_word)
                #print(joined_word)
                if search_noun(word,joined_word)==True:
                    found=True
                    return joined_word
        #print("   \n")

def case_number(word,lang):
    '''it returns the case and number of the inflected word provided, by lookup in its declension '''
    s=stem(word)
    cases_e=['Nominative', 'Accusative', 'Instrumental', 'Dative', 'Ablative', 'Genitive', 'Locative' ,'Vocative']
    numbers_e=['Singular', 'Dual', 'Plural']
    cases_h=['प्रथमा','द्वितीया','तृतीया','चर्तुथी','पन्चमी','षष्ठी','सप्तमी','सम्बोधन']
    numbers_h=['एकवचन','द्विवचन','बहुवचन']
    if lang=='hi':
        cases=cases_h
        numbers=numbers_h
    elif lang== 'eng':
        cases=cases_e
        numbers=numbers_e
    if search_pronoun(word) != None:
        d=Declension_pronoun(s,'masculine')
        for i in range(7):
            for j in range(3):
                if d[i][j]==word:
                    return cases[i],numbers[j]
        d=Declension_pronoun(s,'feminine')
        for i in range(7):
            for j in range(3):
                if d[i][j]==word:
                    return cases[i],numbers[j]
        d=Declension_pronoun(s,'neuter')
        for i in range(7):
            for j in range(3):
                if d[i][j]==word:
                    return cases[i],numbers[j]
        
    elif search_unique(word)!=None:
        d=eval(s)
        for i in range(8):
            for j in range(3):
                if d[i][j]==word:
                    return cases[i],numbers[j]
    else:
        d=Declension_noun(s)
        for i in range(8):
            for j in range(3):
                if d[i][j]==word:
                    return cases[i],numbers[j]

   
if __name__ == '__main__':
#    print(search_noun('नद्योः','नदी'))    
#    find_stem('कर्तृ')
    print(case_number('राज्ञे','hi'))
    print(case_number('विद्वांसौ','eng')) 
