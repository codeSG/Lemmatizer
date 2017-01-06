"""
@author: sourabh garg
"""
"""
It contains different forms of declension  
for e.g.'गुरु'is male and ['गुरु'='ग्'+ 'उ'+ 'र'+ 'उ'] ends with 'उ' means it belongs to ukarant_male declensiontype
"""
from cltk.stem.sanskrit.indian_syllabifier import Syllabifier
import cltk.corpus.sanskrit.alphabet
from words_tagging import *
from Tokenize import *
from Declension_noun_forms import *
lang='hindi'
h = Syllabifier(lang)

class Sanskrit:
    charac=' '
    def __init__(self,charac='अ'):
        self.charac= charac
        
    def __str__(self):
        return self.charac
        
    def __add__(self,vow):
        ch=''
        self_first, self_last=Sanskrit.last(self)
        vow_first,vow_last =Sanskrit.first(vow)
        vowel_to_matraa={'अ':'','आ' : 'ा','इ':'ि','ई':'ी','उ':'ु','ऊ':'ू','ए':'े','ऐ':'ै','ओ':'ो','औ':'ौ','ऋ':'ृ','अं':'ं','अः':'ः'}
        if vow_first in vowel_to_matraa.keys():
            ch= self_last+vowel_to_matraa[vow_first]
        else:
            self_last=self_last+'्'
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

                 
tat_masculine=[['सः','तौ','ते'],
          ['तम्','तौ','तान्'],
          ['तेन','ताभ्याम्','तैः'],
          ['तस्मै','ताभ्याम्','तेभ्यः'],
          ['तस्मात्','ताभ्याम्','तेभ्यः'],
          ['तस्य','तयोः','तेषाम्'],
          ['तस्मिन्','तयोः','तेषु']]
tat_feminine=[['सा','ते','ताः'],
            ['ताम्','ते','ताः'],
            ['तया','ताभ्याम्','ताभिः'],
            ['तस्यै','ताभ्याम्','ताभ्यः'],
            ['तस्याः','ताभ्याम्','ताभ्यः'],
            ['तस्याः','तयोः','तासाम्'],
            ['तस्याम्','तयोः','तासु']]
tat_neuter=[['तत्','ते','तानि'],
            ['तत्','ते','तानि'],
            ['तेन','ताभ्याम्','तैः'],
            ['तस्मै','ताभ्याम्','तेभ्यः'],
            ['तस्मात्','ताभ्याम्','तेभ्यः'],
            ['तस्य','तयोः','तेषाम्'],
            ['तस्मिन्','तयोः','तेषु']]
            
atat_masculine=[['एषः','एतौ','एते'],
          ['एतम्','एतौ','एतान्'],
          ['एतेन','एताभ्याम्','एतैः'],
          ['एतस्मै','एताभ्याम्','एतेभ्यः'],
          ['एतस्मात्','एताभ्याम्','एतेभ्यः'],
          ['एतस्य','एतयोः','एतेषाम्'],
          ['एतस्मिन्','एतयोः','एतेषु']]
atat_feminine=[['एषा','एते','एताः'],
            ['एताम्','एते','एताः'],
            ['एतया','एताभ्याम्','एताभिः'],
            ['एतस्यै','एताभ्याम्','एताभ्यः'],
            ['एतस्याः','एताभ्याम्','एताभ्यः'],
            ['एतस्याः','एतयोः','एतासाम्'],
            ['एतस्याम्','एतयोः','एतासु']]
atat_neuter=[['एतत्','एते','एतानि'],
            ['एतत्','एते','एतानि'],
            ['एतेन','एताभ्याम्','एतैः'],
            ['एतस्मै','एताभ्याम्','एतेभ्यः'],
            ['एतस्मात्','एताभ्याम्','एतेभ्यः'],
            ['एतस्य','एतयोः','एतेषाम्'],
            ['एतस्मिन्','एतयोः','एतेषु']]
            

            
asmad=[['अहम्','आवाम्','वयम्'],
       ['माम्','आवाम्','अस्मान्'],
       ['मया','आवाभ्याम्','अस्माभिः'],
       ['मह्यम्','आवाभ्याम्','अस्मभ्यम्'],
       ['मत्','आवाभ्याम्','अस्मत्'],
       ['मम','आवयोः','अस्माकम्'],
       ['मयि','आवयोः','अष्मासु']]
yushmad=[['त्वम्','युवाम्','यूयम्'],
         ['त्वाम्','युवाम्','युष्मान्'],
         ['त्वया','युवाभ्याम्','युष्माभिः'],
         ['तुभ्यम्','युवाभ्याम्','युष्मभ्य'],
         ['त्वत्','युवाभ्याम्','युष्मत्'],
         ['तव','युवयोः','युष्माकम्'],
         ['त्वयि','युवयोः','युष्मासु']]
  
kim_masculine=[['कः','कौ','के'],
          ['कम्','कौ','कान्'],
          ['केन','काभ्याम्','कैः'],
          ['कस्मै','काभ्याम्','केभ्यः'],
          ['कस्मात्','काभ्याम्','केभ्यः'],
          ['कस्य','कयोः','केषाम्'],
          ['कस्मिन्','कयोः','केषु']]
kim_feminine=[['का','केे','काः'],
            ['काम्','के','काः'],
            ['कया','काभ्याम्','काभिः'],
            ['कस्यै','काभ्याम्','काभ्यः'],
            ['कस्याः','काभ्याम्','काभ्यः'],
            ['कस्याः','कयोः','कासाम्'],
            ['कस्याम्','कयोः','कासु']]
kim_neuter=[['किम्','के','कानि'],
            ['किम्','के','कानि'],
            ['केन','काभ्याम्','कैः'],
            ['कस्मै','काभ्याम्','केभ्यः'],
            ['कस्मात्','काभ्याम्','केभ्यः'],
            ['कस्य','कयोः','केषाम्'],
            ['कस्मिन्','कयोः','केषु']]

idam_masculine=[['अयम्','इमौ','इमे'],
           ['इमम्','इमौ','इमान्'],
           ['अनेन','आभ्याम्','एभिः'],
           ['अस्मै','आभ्याम्','एभ्यः'],
           ['अस्मात्','आभ्याम्','एभ्यः'],
           ['अस्य','अनयोः','एषाम्'],
           ['अस्मिन्','अनयोः','एषु']]
idam_feminine=[['इयम्','इमे','इमाः'],
             ['इमम्','इमे','इमाः'],
             ['अनया','आभ्याम्','आभिः'],
             ['अस्यै','आभ्याम्','आभ्यः'],
             ['अस्याः','आभ्याम्','आभ्यः'],
             ['अस्याः','अनयोः','आसाम्'],
             ['अस्याम्','अनयोः','आसु']]
idam_neuter=[['इदम्','इमे','इमानि'],
             ['इदम्','इमे','इमानि'],
             ['अनेन','आभ्याम्','एभिः'],
             ['अस्मै','आभ्याम्','एभ्यः'],
             ['अस्मात्','आभ्याम्','एभ्यः'],
             ['अस्य','अनयोः','एषाम्'],
             ['अस्मिन्','अनयोः','एषु']]
             
bhavat_masculine=[['भवान्','भवन्तौ','भवतः'],
             ['भवन्तम्','भवन्तौ','भवतः'],
             ['भवता','भवद्भ्याम्','भवद्भिः'],
             ['भवते','भवद्भ्याम्','भवद्भ्यः'],
             ['भवतः','भवद्भ्याम्','भवद्भ्यः'],
             ['भवतः','भवतोः','भवताम्'],
             ['भवति','भवतोः','भवत्सु']]
bhavat_feminine=[['भवती','भवत्यौ','भवत्यः'],
               ['भवतीम्','भवत्यौ','भवतीः'],
               ['भवत्या','भवद्भ्याम्','भवद्भिः'],
               ['भवत्यै','भवद्भ्याम्','भवद्भ्यः'],
               ['भवत्याः','भवद्भ्याम्','भवद्भ्यः'],
               ['भवत्याः','भवत्योः','भवताम्'],
               ['भवत्याम्','भवत्योः','भवत्सु']]
bhavat_neuter=[['भवत्','भवती','भवन्ति'],
               ['भवत्','भवती','भवन्ति'],
               ['भवता','भवद्भ्याम्','भवद्भिः'],
               ['भवते','भवद्भ्याम्','भवद्भ्यः'],
               ['भवतः','भवद्भ्याम्','भवद्भ्यः'],
               ['भवतः','भवतोः','भवताम्'],
               ['भवति','भवतोः','भवत्सु']]
               
sarv_masculine=[['सर्वः','सर्वौ','सर्वे'],
                ['सर्वम्','सर्वौ','सर्वान्'],
                ['सर्वेण','सर्वाभ्य़ाम्','सर्वैः'],
                ['सर्वस्मै','सर्वाभ्य़ाम्','सर्वेभ्यः'],
                ['सर्वस्मात्','सर्वाभ्याम्','सर्वेभ्यः'],
                ['सर्वस्य','सर्वयोः','सर्वेषाम्'],
                ['सर्वस्मिन्','सर्वयोः','सर्वेषु']]
               
sarv_feminine=[['सर्वा','सर्वे','सर्वाः'],
                ['सर्वाम्','सर्वे','सर्वाः'],
                ['सर्वेया','सर्वाभ्य़ाम्','सर्वाभिः'],
                ['सर्वस्यै','सर्वाभ्य़ाम्','सर्वाभ्यः'],
                ['सर्वस्याः','सर्वाभ्याम्','सर्वाभ्यः'],
                ['सर्वस्याः','सर्वयोः','सर्वासाम्'],
                ['सर्वस्याम्','सर्वयोः','सर्वासु']]  
               
sarv_masculine=[['सर्वम्','सर्वे','सर्वाणि'],
                ['सर्वम्','सर्वे','सर्वाणि'],
                ['सर्वेण','सर्वाभ्य़ाम्','सर्वैः'],
                ['सर्वस्मै','सर्वाभ्य़ाम्','सर्वेभ्यः'],
                ['सर्वस्मात्','सर्वाभ्याम्','सर्वेभ्यः'],
                ['सर्वस्य','सर्वयोः','सर्वेषाम्'],
                ['सर्वस्मिन्','सर्वयोः','सर्वेषु']]  
                
def Declension(word):
    
    for i in range(len(all_noun)):
        for stem_type in all_noun[i]:
            if word == stem_type:
                stem_t=dict_noun[i]
                break;
   # print(stem_t)
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
def Declension_noun(word,gender):
    w=complete_tokenize(word)
    w2=w[:len(w)-1]
    w2.append('अ')
    #print(w,w2)
    w3=join(w2)
    w4=Sanskrit(w3)
    s=stem_class(word)
    s=s+gender
    #print(s)
    for i in range(8):
        for j in range(3):
            if i==7:
                print('हे', end =' ')
            print((w4+Sanskrit(eval(s)[i][j])),end='   ')
        print('\n')

        
if __name__ == '__main__':
    print("Declension of 'बालक':")
    Declension_noun('बालक','masculine')
    
    print("Declension of 'कवि':")
    Declension_noun('कवि','masculine')
    
    print("Declension of 'साधु':")
    Declension_noun('साधु','masculine')
    
    print("Declension of 'पितृ':")
#    Declension_noun('पितृ','masculine')
    
    print("Declension of 'बालिका':")
    Declension_noun('बालिका','feminine')
    
    print("Declension of 'मति':")
    Declension_noun('मति','feminine')
    
    print("Declension of 'नदी':")
    Declension_noun('नदी','feminine')
    
    print("Declension of 'फल':")
    Declension_noun('फल','neuter')
    
   
    """ This is just illustration , presently it works for akarant_male words """
