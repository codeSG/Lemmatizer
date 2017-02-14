
"""
@author: user
"""
'''It contains the sandhi rules which are to be applied to concatenate two sanskrit words
   Presently, it don't contains all rules, I will add them in some time
'''
from Tokenize import complete_tokenize, join
from cltk.corpus.sanskrit.alphabet import *
import itertools

consonant=[CONSONANT_GUTTURALS,CONSONANT_PALATALS,CONSONANT_CEREBRALS,CONSONANT_DENTALS,CONSONANT_LABIALS,SEMIVOWEL_CONSONANT, SIBILANT_CONSONANT,SONANT_ASPIRATE ]
consonant= list(itertools.chain(*consonant))
consonant = [x+'्' for x in consonant]

def sandhi(first,second):
    f=complete_tokenize(first)
    first,second=rule2(first,second)
    if f[-1] in consonant:
        return rule1(first,second)
    else:
        return rule0(first,second)
        
def rule0(first,second):
    f=complete_tokenize(first)
    s=complete_tokenize(second)
    f_last=f[-1]
    s_start=s[0]
    f.pop()
    s.pop(0)
    add=[]
    if f_last in ['अ','आ'] and s_start in ['अ','आ']:
        add=['आ']
    elif f_last in ['इ','ई'] and s_start in ['इ','ई']:
        add=['ई']
    elif f_last in ['उ','ऊ'] and s_start in ['उ','ऊ']:
        add=['ऊ']
    elif f_last in ['ऋ'] and s_start in ['ऋ']:
        add=['ऋ']
 
    elif f_last in ['अ','आ'] and s_start in ['इ','ई']:
        add=['ए'] 
    elif f_last in ['अ','आ'] and s_start in ['उ','ऊ']:
        add=['ओ']
    elif f_last in ['अ','आ'] and s_start in ['ऋ']:
        add=['अ','र्']
    elif f_last in ['अ','आ'] and s_start in ['ऌ']:
        add=['अ','ल्']
   
    elif f_last in ['अ','आ'] and s_start in ['ए','ऐ']:
        add=['ऐ'] 
    elif f_last in ['अ','आ'] and s_start in ['ओ','औ']:
        add=['औ']

    elif f_last in ['इ','ई'] and s_start in ['अ','आ','उ','ऊ','ए','ऐ','ओ','औ']:
        add=['य्',s_start]
    elif f_last in ['उ','ऊ'] and s_start in ['अ','आ','इ','ई','ए','ऐ','ओ','औ']:
        add=['ऊ',s_start]
    elif f_last in ['ऋ'] and s_start in ['अ','आ','इ','ई','उ','ऊ','ए','ऐ','ओ','औ']:
        add=['र्',s_start]
    elif f_last in ['ऌ'] and s_start in ['अ','आ','इ','ई','उ','ऊ','ए','ऐ','ओ','औ']:
        add=['ल्',s_start]

    elif f_last in ['ए'] and s_start in ['अ','आ','इ','ई','उ','ऊ','ए','ऐ','ओ','औ']:
        add=['अ','य्',s_start]
    elif f_last in ['ऐ'] and s_start in ['अ','आ','इ','ई','उ','ऊ','ए','ऐ','ओ','औ']:
        add=['अा','य्',s_start]
    elif f_last in ['ओ'] and s_start in ['अ','आ','इ','ई','उ','ऊ','ए','ऐ','ओ','औ']:
        add=['अ','व्',s_start]
    elif f_last in ['औ'] and s_start in ['अ','आ','इ','ई','उ','ऊ','ए','ऐ','ओ','औ']:
        add=['आ','व्',s_start]
    else:
        add=[f_last,s_start]

    result=f+add+s
    
    return join(result)


def rule1(first,second):
    ''' suchtiv sandhi:  {'स्', 'त्', 'थ्', 'द्', 'ध्', 'न्'} converts to {'श्','च्', 'छ्','ज्', 'झ्', 'ञ्'} respectively ,
        if element of first list comes in any of the two words, and element from second list comes in the other word at the point of concatenation
    '''
    f=complete_tokenize(first)
    s=complete_tokenize(second)
    f_last=f[-1]
    s_start=s[0]
    listB={'स्':'श्', 'त्':'च्', 'थ्':'छ्', 'द्':'ज्', 'ध्':'झ्', 'न्':'ञ्'}
    if s_start in listB.keys() and f_last in listB.values():
        s[0]=listB[s_start]
    elif s_start in listB.values() and f_last in listB.keys():
        f[-1]=listB[f_last]
    result=f+s
    return join(result)
    
def rule2(first,sec):
    ''' if 'न्' is there in sec , it got converted to 'ण्' , if there exist 'र्' or 'ष्' or'ऋ' in first,
        where elements of listA can be present in between them.
    '''
    listA=['','अ','आ' ,'इ','ई','उ','ऊ','ए','ऐ','ओ','औ','अं','अः','ह्','य्','व्','न्','क्','ख्','ग्','घ्','ङ्','प्','फ्','ब्','भ्','म्']
    
    sec_n=complete_tokenize(sec)
    first_r=complete_tokenize(first)
    first_r.reverse()
    
    for i in range(len(sec_n)):
        if sec_n[i]=='न्':
            for item in first_r:
                if item in listA:
                    continue
                elif item =='र्' or item == 'ष्' or item=='ऋ':
                    sec_n[i]='ण्'
                    break
                elif item in consonant:
                    break
        elif sec_n[i] in consonant:
            break
    first_r.reverse()
    f=join(first_r)
    s=join(sec_n)
    return f,s
    

if __name__ == '__main__':
    print(sandhi('राज्','नभिः '))
    print(sandhi('विधु' ,'उदयः'))