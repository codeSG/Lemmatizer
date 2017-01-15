# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 09:11:08 2016

@author: user
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

def search_pronoun(word,pro):
    if word in pronoun:
        declension=Declension_pronoun(pro,masculine)
        for case in declension:
            for number in case:
                if word==number:
                    return True
        declension=Declension_pronoun(pro,feminine)
        for case in declension:
            for number in case:
                if word==number:
                    return True
        declension=Declension_pronoun(pro,neuter)
        for case in declension:
            for number in case:
                if word==number:
                    return True
def find_stem(word):
    for i in range(len(all_noun)):
        if word in all_noun[i]:
            stem_t=dict_noun[i]
            return stem_t
            
def stem(word):
    mytrie=Trie()
    for stem_cls in words_tagging.all_noun:
        for noun in stem_cls:
            mytrie.insert(complete_tokenize(noun))
    for pro in words_tagging.pronoun:
        mytrie.insert(complete_tokenize(pro))
    
    lis=complete_tokenize(word)
    print(lis)
    length=len(lis)
    print(length)
    found=False
    
    for i in range(length):
        serch=lis[:length-i]
        #print(serch)
        for trie_word in mytrie.find(serch):
            joined_word=join(trie_word)
            #print(joined_word)
            if search_pronoun(word,joined_word)==True:
                return joined_word
            elif search_noun(word,joined_word)==True:
                return joined_word
        #print("   \n")
        
#print(stem1('प्रीत्योः'))
print(Declension_noun('फल') ) 
print(search_noun('नद्योः','नदी'))     
print(stem('क्षु्द्भ्यः'))    
#if __name__ == '__main__':
#    print(stem1('प्रीत्योः'))
#    print(stem1('नद्योः'))
