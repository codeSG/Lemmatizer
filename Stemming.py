# -*- coding: utf-8 -*-
"""
@author:sourabh garg
"""

import Trie 
import words_tagging 
from Declension import Declension_noun
from Tokenize import complete_tokenize,join

def search_noun(word,noun):
    ''' Searches word in the declension of the noun'''
    dec=Declension_noun(noun)
    for row in dec:
        for col in row:
            if word==col:
                return True


        
def stem(word):
    '''it returns the stem for any inflected word provided'''
    mytrie=Trie.Trie()
    for stem_cls in words_tagging.all_noun:
        for noun in stem_cls:
            mytrie.insert(complete_tokenize(noun))
            
    lis=complete_tokenize(word)
    if ' ' in word:
        lis=lis[2:]   #for vocative case , as they include 'हे' at initial, while searching it must be removed

    length=len(lis)
    
    for i in range(length):
        serch=lis[:length-i]
        for trie_word in mytrie.find(serch):
            joined_word=join(trie_word)
            
            if search_noun(word,joined_word)==True:
                found=True
                return joined_word
            

if __name__ == '__main__':
    print(stem('नद्योः'))  

    print(stem('पोत्रोः'))
    
    print(stem('हे क्षुधः'))