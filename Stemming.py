# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 09:11:08 2016

@author: user
"""

from Declension import *
import Declension_noun_forms
from Declension_noun_forms import *
from words_tagging import *
from Trie import *
from Tokenize import *

def search(word,noun):
    declension=Declension(noun)
#    print(declension)
    for case in declension:
        for number in case:
            if word==number:
                return True
            
def stem1(word):
    mytrie=Trie()
    for stem_cls in words_tagging.all_noun:
        for noun in stem_cls:
            mytrie.insert(complete_tokenize(noun))
        
    lis=complete_tokenize(word)
    length=len(lis)
#    print(lis)

    found=False
    for i in range(length):
        serch=lis[:length-i]
        for noun in mytrie.find(serch):
            joined_noun=join(noun)
            if search(word,joined_noun) == True:
                return joined_noun

            
if __name__ == '__main__':
    print(stem1('प्रीत्योः'))
    print(stem1('नद्योः'))
