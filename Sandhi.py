
"""
@author: user
"""
'''It contains the sandhi rules which are to be applied to concatenate two sanskrit words
   Presently, it don't contains all rules, I will add them in some time
'''
from Tokenize import *

def rule(first,sec):
    ''' if 'न्' is there in sec , it got converted to 'ण्' , if there exist 'र्' or 'ष्' or'ऋ' in first,
        where elements of listA can be present in between them.
    '''
    listA=['','अ','आ' ,'इ','ई','उ','ऊ','ए','ऐ','ओ','औ','अं','अः','ह्','य्','व्','न्','क्','ख्','ग्','घ्','ङ्','प्','फ्','ब्','भ्','म्']
    alphabet=[CONSONANT_GUTTURALS,CONSONANT_PALATALS,CONSONANT_CEREBRALS,CONSONANT_DENTALS,CONSONANT_LABIALS,SEMIVOWEL_CONSONANT, SIBILANT_CONSONANT,SONANT_ASPIRATE ]
    alphabet= list(itertools.chain(*alphabet))
    alphabet = [x+'्' for x in alphabet]
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
                elif item in alphabet:
                    break
        elif sec_n[i] in alphabet:
            break
    first_r.reverse()
    f=join(first_r)
    s=join(sec_n)
    return f,s
    


def rule2(first,sec):
    ''' suchtiv sandhi:  {'स्', 'त्', 'थ्', 'द्', 'ध्', 'न्'} converts to {'श्','च्', 'छ्','ज्', 'झ्', 'ञ्'} respectively ,
        if element of first list comes in any of the two words, and elemnt from second list comes in the other word
    '''
    #print(first, sec)
    first_list=complete_tokenize(first)
    sec_list=complete_tokenize(sec)
    first_list.reverse()
    #print(first_list,sec_list)
    listB={'स्':'श्', 'त्':'च्', 'थ्':'छ्', 'द्':'ज्', 'ध्':'झ्', 'न्':'ञ्'}
    if sec_list[0] in listB.keys() and first_list[0] in listB.values():
        sec_list[0]=listB[sec_list[0]]
    elif sec_list[0] in listB.values() and first_list[0] in listB.keys():
        first_list[0]=listB[first_list[0]]

    first_list.reverse()
    #print(first_list,sec_list)
    s=join(first_list)
    v=join(sec_list)
    #print(s,v)
    return s,v
    
if __name__ == '__main__':
    print(rule('राम','आनाम्'))
    print(rule2('राज्','नभिः '))