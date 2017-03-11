# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:09:25 2017

@author: user
"""
import Trie
from words_tagging import all_noun
from Declension import Declension_noun
from Stemming import stem,initialize
mytrie=Trie.Trie()
mytrie=initialize()

if __name__ == '__main__':
    correct=0
    incorrect=0
    total=0
    incorrect_words=[]
    for s_type in all_noun:
        for noun in s_type:
            dec=Declension_noun(noun)
            print(noun)
            #print(dec)
            for row in dec:
                for col in row:
                    total=total+1
                    if stem(col)==noun:
                        correct=correct+1
                    else:
                        incorrect=incorrect+1
                        incorrect_words.append(col)
            
    
    print("Correct stemming=",correct)
    print("Accuracy=",correct/total)
    print (incorrect_words)
 
    for item in incorrect_words:
        st.append(stem(item))
    print(st)