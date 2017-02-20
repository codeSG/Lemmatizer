"""
@author: sourabh garg
"""
"""
It produces Declension table for any noun/ pronoun depending on its gender and ending character
for e.g.'गुरु'is male and ['गुरु'='ग्'+ 'उ'+ 'र'+ 'उ'] ends with 'उ' means it belongs to u_stem_m declensiontype
"""
import words_tagging
from Tokenize import complete_tokenize,join,gender,stem_class
from Sandhi import sandhi
from Declension_noun_forms import *

def Declension_noun(word):
    ''' 
    This function inputs only the noun word(no gender is required) present in our database,and 
    it returns the declension of the noun word by adding suffix sequence(from Declension_noun_form module) to the noun.'''
    if word in words_tagging.unique:
        return eval(word)
    else:
        special_stem=['as_stem_','an_stem_','en_stem_']
        stem_c=stem_class(word)
        gen=gender(word)
        stem_type=stem_c+gen
        word_list=complete_tokenize(word)
        if stem_c in special_stem:
            word_prefix=word_list[:-2]
        else:
            word_prefix=word_list[:-1]
        word=join(word_prefix)
        
        decl=[]         
        for row in range(8):
            case=[]
            for col in range(3):
                if row==7:
                    case.append('हे '+sandhi(word,eval(stem_type)[row][col]))
                else:
                    case.append(sandhi(word,eval(stem_type)[row][col]))
            decl.append(case)
            
        return decl

          
def Declension(word,gender=''):
    ''' 
    It is the main method which produce Declension of any noun word 
    provided, its gender. 
    '''
    cases=['प्रथमा','द्वितीया','तृतीया','चर्तुथी','पन्चमी','षष्ठी','सप्तमी','सम्बोधन']
    if word in words_tagging.unique:
        Dec=eval(word)
    else:
        special_stem=['as_stem_','an_stem_','en_stem_']
        stem_c=stem_class(word)
        stem_type=stem_c+gender
        word_list=complete_tokenize(word)
        if stem_c in special_stem:
            print("special")
            word_prefix=word_list[:-2]
        else:
            word_prefix=word_list[:-1]
    
        word=join(word_prefix)
        if stem_type not in words_tagging.dict_noun.values():
            stem_type=stem_type+'_1'
        Dec=[]         
        for row in range(8):
            case=[]
            for col in range(3):
                if row==7:
                    case.append('हे '+sandhi(word,eval(stem_type)[row][col]))
                else:
                    case.append(sandhi(word,eval(stem_type)[row][col]))
            Dec.append(case)
    print(Dec)
        
if __name__ == '__main__':
     
     wordd=['राम','गिरि','गुरु',
            'पितृ','कर्तृ','गो','रमा','मति','नदी','धेनु','वधू','मातृ','नौ','फल','वारि','दधि','मधु','भगवत्','गतवत्','करिन्',
            'भूभृत्','राजन्','आत्मन्','पयोमुच्','भिषज्','सरित्','वाच्','उपानह्','क्षुध्','विपद्','दिश्','जगत्','पयस्','नामन्','विद्वस्','ज्ञातृ']
     for i in wordd:
         print(i)
         print(Declension_noun(i))
         