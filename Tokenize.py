"""
@author: sourabh garg
"""
from cltk.stem.sanskrit.indian_syllabifier import Syllabifier
from cltk.corpus.sanskrit.itrans.langinfo import *
from cltk.corpus.sanskrit.alphabet import *
import itertools
lang='hindi'
h = Syllabifier(lang)

CHAR=[INDEPENDENT_VOWELS_SIMPLE,
      INDEPENDENT_VOWELS_DIPTHONGS,
      INDEPENDENT_VOWELS,
      CONSONANT_GUTTURALS,
      CONSONANT_PALATALS,
      CONSONANT_CEREBRALS,
      CONSONANT_DENTALS,
      CONSONANT_LABIALS,
      SEMIVOWEL_CONSONANT, 
      SIBILANT_CONSONANT,
      SONANT_ASPIRATE ]
CHAR  = list(itertools.chain(*CHAR))
matraa_to_vowel={'':'अ' , 'ा':'आ' ,'ि':'इ', 'ी':'ई', 'ु':'उ', 'ू':'ऊ','े':'ए' , 'ै':'ऐ' , 'ो':'ओ', 'ौ':'औ', 'ृ':'ऋ', 'ं':'अं','ः':'अः'}
vowel_to_matraa={'अ':'','आ' : 'ा','इ':'ि','ई':'ी','उ':'ु','ऊ':'ू','ए':'े','ऐ':'ै','ओ':'ो','औ':'ौ','ऋ':'ृ','अं':'ं','अः':'ः'}
        
def complete_tokenize(word):
    '''
        Complete Tokenization of a noun word into smallest unit possible
        for e.g. विद्यार्थी = 'व्'+'इ'+'द्'+'य्'+'आ'+'र्'+'थ्'+'ई'
    '''
    
    tokened_list=[]
    word_list = h.orthographic_syllabify(word)
   # print(word_list)
    for i in word_list:
        i=list(itertools.chain(*i))
       # print(i)
        if len(i)==1:
            if i[0] in CHAR:
                tokened_list.append(i[0]+'्')
                tokened_list.append('अ')
            else:
                tokened_list.append(i[0])
        else:
            for j in range(len(i)):
                token=i[j]
                if token in CHAR and j==len(i)-1:
                    tokened_list.append(token+'्')
                    tokened_list.append('अ')
                elif token in CHAR:
                    tokened_list.append(token+'्')
                elif token in matraa_to_vowel.keys():
                    tokened_list.append(matraa_to_vowel[token])
                   
    return tokened_list
    
def stem_class(word):
    lis=complete_tokenize(word)
    length=len(lis)
    ch=lis[length-1]
    ch2=lis[length-2]
    

    ch_to_stem={'अ':'a_stem_','इ':'i_stem_','उ':'u_stem_','आ':'a_stem_','ई':'ii_stem_',
                'ऊ':'uu_stem_','ओ':'o_stem_','औ':'oo_stem_','ऋ':'r_stem_',
                'न्':'n_stem_','त्':'t_stem_','स्':'s_stem_','च्':'c_stem_',
                'ध्':'dh_stem_','श्':'sh_stem_','ह्':'h_stem_','द्':'d_stem',}
    
    if ch in ch_to_stem.keys():
        if ch_to_stem[ch] =='n_stem_' and ch2 =='इ':
            return 'en_stem_'
        else:
            return ch_to_stem[ch]
    

def join(list_char):
    ''' It joins the complete tokenized word'''
    word=''
    CONSONANT_HALANTA = [x+'्' for x in CHAR]
    CONS_TO_CONS=dict(zip(CONSONANT_HALANTA, CHAR))
    length=len(list_char)
    
    for i in range(length):
        if i==0 and list_char[i] in vowel_to_matraa.keys():
            word=word+list_char[i]
        elif list_char[i] in CONS_TO_CONS.keys() and i==length-1:
            word=word+list_char[i]
        elif list_char[i] in CONS_TO_CONS.keys() and list_char [i+1] in vowel_to_matraa.keys():
            word=word+CONS_TO_CONS[list_char[i]]
        elif list_char[i] in CONS_TO_CONS.keys():
            word=word+list_char[i]
        elif list_char[i] in vowel_to_matraa.keys():
            word=word+vowel_to_matraa[list_char[i]]
        else:
            word=word+list_char[i]
    return word
    
if __name__ == '__main__':
    '''
    Illustration with some difficult words'''
    words=['क्लेश','नित्यः','यत्न','स्त्रोत','चक्कर','पुख्ता', 'दुग्गल', 'घग्घर', 'घ्राण','पड्क','सच्चा','स्वच्छ','सज्जा','ज्योतिष','विज्ञान','वञ्चिंत','मिट्टी','गट्ठर','अकाट्य','ट्रस्ट','बुड्ढा','ड्रेस','घण्टा',"कण्ठ",
       'उत्कंठा','कुत्ता','मत्था','उत्फुल्ल','उत्पत्ति','नृत्य','जिद्दी','सिद्धि','कर्तृणी','विद्यार्थी','द्रवित','द्वारा','द्वेष','आँध्र','संध्या','सिंह','सींग','महन्त','मन्दाकिनी','धन्धा','प्रसन्न','उन्मूलन','अन्य','कन्हैया',
       'गुप्त','ठप्पा','प्यास','प्रणाम','हफ्ता','जब्त','कब्ज','ब्रिटिश','भ्लेच्छ','सहस्र','सहस्त्र','ह्रस्व','आर्य','चक्र','क्षत्रिय','दण्डिन्','राम','नृप','ग्राम','पुत्र','सूर्य','चन्द्र','शिष्य']
    print(complete_tokenize('नः'))
    for i in words:
        print(i,complete_tokenize(i))
    print(stem_class('दण्डिन्'))
    print(join(['भ्', 'ल्', 'ए', 'च्', 'छ्']))