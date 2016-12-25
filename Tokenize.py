"""
@author: sourabh garg
"""
from cltk.stem.sanskrit.indian_syllabifier import Syllabifier
from cltk.corpus.sanskrit.itrans.langinfo import *
from cltk.corpus.sanskrit.alphabet import *
import itertools
lang='hindi'
h = Syllabifier(lang)

def complete_tokenize(word):
    '''
        Complete Tokenization of a noun word into smallest unit possible
        for e.g. विद्यार्थी = 'व्'+'इ'+'द्'+'य्'+'आ'+'र्'+'थ्'+'ई'
    '''
    CONSONANT=[CONSONANT_GUTTURALS,
               CONSONANT_PALATALS,
               CONSONANT_CEREBRALS,
               CONSONANT_DENTALS,
               CONSONANT_LABIALS,
               SEMIVOWEL_CONSONANT, 
               SIBILANT_CONSONANT,
               SONANT_ASPIRATE ]
    CONSONANT  = list(itertools.chain(*CONSONANT))
    matraa_to_vowel={'':'अ' , 'ा':'आ' ,'ि':'इ', 'ी':'ई', 'ु':'उ', 'ू':'ऊ','े':'ए' , 'ै':'ऐ' , 'ो':'ओ', 'ौ':'औ', 'ृ':'ऋ', 'ं':'अं','ः':'अः'}
    tokened_list=[]
    word_list = h.orthographic_syllabify(word)
    
    for i in word_list:
        i=list(itertools.chain(*i))
        if len(i)==1:
            if i[0] in CONSONANT:
                tokened_list.append(i[0]+'्')
                tokened_list.append('अ')
            else:
                tokened_list.append(i[0])
        else:
            for j in range(len(i)):
                token=i[j]
                if token in CONSONANT and j==len(i)-1:
                    tokened_list.append(token+'्')
                    tokened_list.append('अ')
                elif token in CONSONANT:
                    tokened_list.append(token+'्')
                elif token in matraa_to_vowel.keys():
                    tokened_list.append(matraa_to_vowel[token])
                   
    return tokened_list
    
if __name__ == '__main__':
    '''
    Illustration with some difficult words'''
    words=['क्लेश','नित्य:','यत्न','स्त्रोत','चक्कर','पुख्ता', 'दुग्गल', 'घग्घर', 'घ्राण','पड्क','सच्चा','स्वच्छ','सज्जा','ज्योतिष','विज्ञान','वञ्चिंत','मिट्टी','गट्ठर','अकाट्य','ट्रस्ट','बुड्ढा','ड्रेस','घण्टा',"कण्ठ",
       'उत्कंठा','कुत्ता','मत्था','उत्फुल्ल','उत्पत्ति','नृत्य','जिद्दी','सिद्धि','विद्यार्थी','द्रवित','द्वारा','द्वेष','आँध्र','संध्या','सिंह','सींग','महन्त','मन्दाकिनी','धन्धा','प्रसन्न','उन्मूलन','अन्य','कन्हैया','गुप्त','ठप्पा','प्यास','प्रणाम','हफ्ता','जब्त','कब्ज','ब्रिटिश','भ्लेच्छ','सहस्र','सहस्त्र','ह्रस्व','आर्य','चक्र','क्षत्रिय']
    for i in words:
        print(i,complete_tokenize(i))