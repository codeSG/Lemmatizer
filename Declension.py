"""
@author: sourabh garg
"""
"""
It contains different forms of declension  
for e.g.'गुरु'is male and ['गुरु'='ग्'+ 'उ'+ 'र'+ 'उ'] ends with 'उ' means it belongs to ukarant_male declensiontype
"""
from cltk.stem.sanskrit.indian_syllabifier import Syllabifier
import cltk.corpus.sanskrit.alphabet
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
akarant_male=[['अः','औ','आः'],
              ['अम्','औ','आन्'],
              ['एन','आभ्याम्','ऐः'],
              ['आय','आभ्याम्','एभ्यः'],
              ['आत्','आभ्याम्','एभ्यः'],
              ['अस्य','अयोः','आसाम्'],
              ['ए','अयोः','एषु'],
              ['अ','औ','आः']]
        
ekarant_male=[['इः','ई','अयः'],
              ['इम्','ई','ईन्'],
              ['इना','इभ्याम्','इभिः'],
              ['अये','इभ्याम्','इभ्यः'],
              ['एः','इभ्याम्','इभ्यः'],
              ['एः','योः','ईनाम्'],
              ['औ','योः','इषु'],
              ['ए','ई','अयः']]
              
ukarant_male=[['उः','ऊ','अवः'],
              ['उम्','ऊ','ऊन्'],
              ['उना','उभ्याम्','उभिः'],
              ['अवे','उभ्याम्','उभ्यः'],
              ['ओः','उभ्याम्','उभ्यः'],
              ['ओः','वोः','ऊनाम्'],
              ['औ','वोः','उषु'],
              ['ओ','ऊ','अवः']]
              
akarant_neuter=[['अम्','ए','आनि'],
                ['अम्','ए','आनि'],
                ['एन','आभ्याम्','ऐः'],
                ['आय','आभ्याम्','एभ्यः'],
                ['आत्','आभ्याम्','एभ्यः'],
                ['अस्य','अयोः','आसाम्'],
                ['ए','अयोः','एषु'],
                ['अ','औ','आः']]        
                
aakarant_female=[['आ','ए','आः'],
                 ['आम्','ए','आः'],
                 ['अया','आभ्याम्','आभिः'],
                 ['आये','आभ्याम्','आभ्यः'],
                 ['आयाः','आभ्याम्','आभ्यः'],
                 ['आयाः','अयोः','आनाम्'],
                 ['आयाम्','अयोः','आसु'],
                 ['ए','ए', 'आः']]
                 
ekarant_female=[['इः','ई','अयः'],
                ['इम्','ई','ईः'],
                ['या','इभ्याम्','इभिः'],
                ['यै','इभ्याम्','इभ्यः'],
                ['याः','इभ्याम्','इभ्यः'],
                ['याः','योः','ईनाम्'],
                ['याम्','योः','इषु'],
                ['ए','ई','अयः']]
                
eekarant_female=[['ई','यौः','यः'],
                 ['ईम्','यौः','ईः'],
                 ['या', 'ईभ्याम्','ईभिः'],
                 ['यै','ईभ्याम्','ईभ्यः'],
                 ['याः','ईभ्याम्','ईभ्यः'],
                 ['याः','योः','ईनाम्'],
                 ['याम्','योः','ईषु'],
                 ['इ','यौ','यः']]
def Declension_noun(word):
    w=Sanskrit(word)
    for i in range(8):
        for j in range(3):
            if i==7:
                print('हे', end =' ')
            print((w+Sanskrit(ekarant_male[i][j])) ,end="     ")
        print("\n")
   
if __name__ == '__main__':
    print( "Declension of 'कव':")
    Declension_noun('कव')
    print("Declension of बालक:")
    Declension_noun('बालक')
    
    """ This is just illustration , presently it works for akarant_male words """