"""
@author: sourabh garg
"""
"""
It contains different forms of declension  
for e.g.'गुरु'is male and ['गुरु'='ग्'+ 'उ'+ 'र'+ 'उ'] ends with 'उ' means it belongs to ukarant_male declensiontype
"""
from cltk.stem.sanskrit.indian_syllabifier import Syllabifier
import cltk.corpus.sanskrit.alphabet
from Declension_pronoun import *
from words_tagging import *
from Tokenize import *
from Declension_noun_forms import *
from Sandhi import *
lang='hindi'
h = Syllabifier(lang)

class Sanskrit:
    charac=' '
    def __init__(self,charac='अ'):
        self.charac= charac
        
    def __str__(self):
        return self.charac
        
    def __add__(self,vow):
        s,v=rule(self.charac,vow.charac)
        self=Sanskrit(s)
        vow=Sanskrit(v)
        

        ch=''
        self_first, self_last=Sanskrit.last(self)
        vow_first,vow_last =Sanskrit.first(vow)
        vowel_to_matraa={'अ':'','आ' : 'ा','इ':'ि','ई':'ी','उ':'ु','ऊ':'ू','ए':'े','ऐ':'ै','ओ':'ो','औ':'ौ','ऋ':'ृ','अं':'ं','अः':'ः'}
        if vow_first in vowel_to_matraa.keys():
            ch= self_last+vowel_to_matraa[vow_first]
        else:
            self.charac=self.charac+'्'
            s,v=rule2(self.charac,vow.charac)
            self=Sanskrit(s)
            vow=Sanskrit(v)
            self_first, self_last=Sanskrit.last(self)
            vow_first,vow_last =Sanskrit.first(vow)
            ch=self_last+vow_first
                
        return self_first+ch+vow_last
          
    """
    __add__ is a method for most basic sandhi rules
    last is a method to extract the last syllable
    first is a method to extract the first syllable
    """
    def last(self):
        w=''
        current = h.orthographic_syllabify(self.charac)
        for i in range(len(current)-1):
            w+=current[i]
        return w,current[len(current)-1]

    def first(self):
        w=''
        current = h.orthographic_syllabify(self.charac)
        i=1
        for i in range(1,len(current)):
            w+=current[i]
        return current[0],w

"""
These are different forms(sequence of suffixes) to which any noun word belongs to depending on its gender and ending character.
I will add more such forms.
"""
def find_stem(word):
    for i in range(len(all_noun)):
            for stem_type in all_noun[i]:
                if word == stem_type:
                    stem_t=dict_noun[i]
                    #print(stem_t)
                    return stem_t
                    
                    
def Declension_noun(word):
    stem_t=''
    if word in unique:
        return eval(word)
    else:
        stem_t=find_stem(word)
        #print(stem_t)
        w=complete_tokenize(word)
        w2=w[:len(w)-1]
        w2.append('अ')
        #print(w,w2)
        w3=join(w2)
        w4=Sanskrit(w3) 
       # print(w3)
        decl=[]         
    #    for i in range(8):
    #        for j in range(3):
    #            if i==7:
    #                print('हे', end =' ')
    #            print((w4+Sanskrit(eval(stem_t)[i][j])),end='   ')
    #        print('\n')
        for i in range(8):
            case=[]
            for j in range(3):
                case.append(w4+Sanskrit(eval(stem_t)[i][j]))
            decl.append(case)
            
        return decl

def Declension_pronoun(word,gender=''):
    if word in pronoun:
        string=word+"_"+gender
        try:
            return(eval(string))
        except:
            return(eval(word))
            
def Declension(word,gender=''):
    if word in pronoun:
        string=word+"_"+gender
        try:
            dec=eval(string)
        except:
            dec=eval(word)
        for i in range(7):
            for j in range(3):
                print(dec[i][j],end='   ')
            print('\n')
    elif word in unique: 
        dec=eval(word)
        for i in range(8):
            for j in range(3):
                if i==7:
                    print('हे', end =' ')
                print(dec[i][j],end='   ')
            print('\n')
#    elif Declension_noun(word):
#        dec=Declension_noun(word)
#        for i in range(8):
#            for j in range(3):
#                if i==7:
#                    print('हे', end =' ')
#                print(dec[i][j],end='   ')
#            print('\n')
    else:
        
        w=complete_tokenize(word)
        w2=w[:len(w)-1]
        w2.append('अ')
        #print(w,w2)
        w3=join(w2)
        w4=Sanskrit(w3)
        s=stem_class(word)
        s=s+gender
        #print(s)
        try:
            for i in range(8):
                for j in range(3):
                    if i==7:
                        print('हे', end =' ')
                    print((w4+Sanskrit(eval(s)[i][j])),end='   ')
                print('\n')
        except:
            s=s+"_1"
            #print("i")
            for i in range(8):
                for j in range(3):
                    if i==7:
                        print('हे', end =' ')
                    print((w4+Sanskrit(eval(s)[i][j])),end='   ')
                print('\n')
            

        
if __name__ == '__main__':
    print("Declension of 'क्षुध्':")
    Declension('क्षुध्','feminine')
    print("Declension of 'राम':")
    Declension('राम','masculine')
    print("Declension of 'राजन्':")
    Declension('राजन्','masculine')
   
