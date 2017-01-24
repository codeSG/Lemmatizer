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
    declension=Declension_noun(noun)
    #print(declension)
    for case in declension:
        for number in case:
            if word==number:
                return True

def search_pronoun(word):
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
            
   
if __name__ == '__main__':
#    print(search_noun('नद्योः','नदी'))    
#    find_stem('कर्तृ')
    print(stem('फलम्'))
    print(stem('सर्वासु')) 
