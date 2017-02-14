"""
@author: sourabh garg
"""
import itertools
import re
import words_tagging
from cltk.stem.sanskrit.indian_syllabifier import Syllabifier
from cltk.corpus.sanskrit.alphabet import *

lang='hindi'
h = Syllabifier(lang)

VOWELS=[INDEPENDENT_VOWELS_SIMPLE,
        INDEPENDENT_VOWELS_DIPTHONGS,
        INDEPENDENT_VOWELS]

VOWELS= list(itertools.chain(*VOWELS))     
CONSONANTS=[CONSONANT_GUTTURALS,
            CONSONANT_PALATALS,
            CONSONANT_CEREBRALS,
            CONSONANT_DENTALS,
            CONSONANT_LABIALS,
            SEMIVOWEL_CONSONANT, 
            SIBILANT_CONSONANT,
            SONANT_ASPIRATE ]
CONSONANTS= list(itertools.chain(*CONSONANTS))
CONSONANT_HALANTA = [x+'्' for x in CONSONANTS]
CONS_TO_CONS=dict(zip(CONSONANT_HALANTA, CONSONANTS))
matraa_to_vowel={'':'अ' , 'ा':'आ' ,'ि':'इ', 'ी':'ई', 'ु':'उ', 'ू':'ऊ','े':'ए' , 'ै':'ऐ' , 'ो':'ओ', 'ौ':'औ', 'ृ':'ऋ', 'ं':'अं','ः':'अः','ँ':'अँ' , 'ां':'आं'}
vowel_to_matraa={'अ':'','आ' : 'ा','इ':'ि','ई':'ी','उ':'ु','ऊ':'ू','ए':'े','ऐ':'ै','ओ':'ो','औ':'ौ','ऋ':'ृ','अं':'ं','अः':'ः','अँ':'ँ','आं': 'ां'}
        

ch_to_stem={'अ':'a_stem_','इ':'i_stem_','उ':'u_stem_','आ':'a_stem_','ई':'ii_stem_',
            'ऊ':'uu_stem_','ओ':'o_stem_','औ':'oo_stem_','ऋ':'r_stem_','द्':'d_stem_',
            'अन्':'an_stem_','त्':'t_stem_','स्':'s_stem_','च्':'c_stem_','ज्':'j_stem_',
            'ध्':'dh_stem_','श्':'sh_stem_','ह्':'h_stem_','इन्':'en_stem_','अस्':'as_stem_'}

def complete_tokenize(word):
    '''
        Complete Tokenization of a noun word into smallest possible unit (character)
        for e.g. विद्यार्थी = 'व्'+'इ'+'द्'+'य्'+'आ'+'र्'+'थ्'+'ई'
    '''
    
    tokened_list=[]
    word_list = h.orthographic_syllabify(word)
    for syallable in word_list:
        syallable=list(itertools.chain(*syallable))
       
        if len(syallable)==1:
            if syallable[0] in CONSONANTS:
                tokened_list.append(syallable[0]+'्')
                tokened_list.append('अ')
            elif syallable[0] in VOWELS:
                tokened_list.append(syallable[0])
            elif syallable[0] in matraa_to_vowel.keys():
                tokened_list.append(matraa_to_vowel[syallable[0]])
        else:
            for index in range(len(syallable)):
                token=syallable[index]
                if token in CONSONANTS and index==len(syallable)-1:
                    tokened_list.append(token+'्')
                    tokened_list.append('अ')
                elif token in CONSONANTS:
                    tokened_list.append(token+'्')
                elif token in matraa_to_vowel.keys():
                    tokened_list.append(matraa_to_vowel[token])
                   
    return tokened_list
    
def join(list_char):
    ''' It joins the complete tokenized word'''
    word=''
    length=len(list_char)
    
    for index in range(length):
        if index==0 and list_char[index] in vowel_to_matraa.keys():
            word=word+list_char[index]
        elif list_char[index] in CONS_TO_CONS.keys() and index==length-1:
            word=word+list_char[index]
        elif list_char[index] in CONS_TO_CONS.keys() and list_char [index+1] in vowel_to_matraa.keys():
            word=word+CONS_TO_CONS[list_char[index]]
        elif list_char[index] in CONS_TO_CONS.keys():
            word=word+list_char[index]
        elif list_char[index] in vowel_to_matraa.keys():
            word=word+vowel_to_matraa[list_char[index]]
        else:
            word=word+list_char[index]
    return word
 

def stem_class(word):
    lis=complete_tokenize(word)
    length=len(lis)
    ch=lis[length-1]
    ch2=lis[length-2]
    
    if join([ch2,ch]) in ch_to_stem.keys():
        return ch_to_stem[join([ch2,ch])]
    elif ch in ch_to_stem.keys():
        return ch_to_stem[ch]
 
def gender(word):
    for index in range(len(words_tagging.all_noun)):
        if word in words_tagging.all_noun[index]:
            stem_t=words_tagging.dict_noun[index]
            gen = re.sub(r"^[^_]*_[^_]*_", "", stem_t)
            return gen
            
            
if __name__ == '__main__':
    '''
    Illustration with some difficult words'''
    words=['क्लेश','नित्यः','यत्न','स्त्रोत','चक्कर','पुख्ता', 'दुग्गल', 'घग्घर', 'घ्राण','पड्क','सच्चा','स्वच्छ','सज्जा','ज्योतिष','विज्ञान','वञ्चिंत','मिट्टी','गट्ठर','अकाट्य','ट्रस्ट','बुड्ढा','ड्रेस','घण्टा',"कण्ठ",
       'उत्कंठा','कुत्ता','मत्था','उत्फुल्ल','उत्पत्ति','नृत्य','जिद्दी','सिद्धि','कर्तृणी','विद्यार्थी','द्रवित','द्वारा','द्वेष','आँध्र','संध्या','सिंह','सींग','महन्त','मन्दाकिनी','धन्धा','प्रसन्न','उन्मूलन','अन्य','कन्हैया',
       'गुप्त','ठप्पा','प्यास','प्रणाम','हफ्ता','जब्त','कब्ज','ब्रिटिश','भ्लेच्छ','सहस्र','सहस्त्र','ह्रस्व','आर्य','चक्र','क्षत्रिय','दण्डिन्','राम','नृप','ग्राम्','पुत्र','सूर्य','चन्द्र','शिष्य्','अनार']
    for i in words:
        st=complete_tokenize(i)
        print(i,st,join(st))
    print(stem_class('अम्बु'))
    print(gender('ज्ञातृ'))
    print(join(['भ्', 'ल्', 'ए', 'च्', 'छ्']))