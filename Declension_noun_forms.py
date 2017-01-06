# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 08:56:21 2017

@author:sourabh
"""

a_stem_masculine=[['अः','औ','आः'],
              ['अम्','औ','आन्'],
              ['एन','आभ्याम्','ऐः'],
              ['आय','आभ्याम्','एभ्यः'],
              ['आत्','आभ्याम्','एभ्यः'],
              ['अस्य','अयोः','आनाम्'],
              ['ए','अयोः','एषु'],
              ['अ','औ','आः']]
        
i_stem_masculine=[['इः','ई','अयः'],
              ['इम्','ई','ईन्'],
              ['इना','इभ्याम्','इभिः'],
              ['अये','इभ्याम्','इभ्यः'],
              ['एः','इभ्याम्','इभ्यः'],
              ['एः','योः','ईनाम्'],
              ['औ','योः','इषु'],
              ['ए','ई','अयः']]
              
u_stem_masculine=[['उः','ऊ','अवः'],
              ['उम्','ऊ','ऊन्'],
              ['उना','उभ्याम्','उभिः'],
              ['अवे','उभ्याम्','उभ्यः'],
              ['ओः','उभ्याम्','उभ्यः'],
              ['ओः','वोः','ऊनाम्'],
              ['औ','वोः','उषु'],
              ['ओ','ऊ','अवः']]
             
r_stem_masculine=[['आ','अरौ','अरः'],
                  ['अरम्','अरौ','ऋन्'],
                  ['रा','ऋभ्याम्','ऋभिः'],
                  ['रे','ऋभ्याम्','ऋभ्यः'],
                  ['उः','ऋभ्याम्','ऋभ्यः'],
                  ['उः','रोः','ऋणाम्'],
                  ['अरि','रोः','ऋषु'],
                  ['अः','अरौ','अरः']]
                  
r_stem_masculine=[['आ','अारौ','अारः'],
                  ['अारम्','अारौ','ऋन्'],
                  ['रा','ऋभ्याम्','ऋभिः'],
                  ['रे','ऋभ्याम्','ऋभ्यः'],
                  ['उः','ऋभ्याम्','ऋभ्यः'],
                  ['उः','रोः','ऋणाम्'],
                  ['अरि','रोः','ऋषु'],
                  ['अः','अरौ','अरः']]
                
o_stem_masculine=[['औः','आवौ','आवः'],
                 ['आम्','आवौ','आः'],
                 ['अवा','ओभ्याम्','ओभिः'],
                 ['अवे','ओभ्याम्','ओभ्यः'],
                 ['ओः','ओभ्याम्','ओभ्यः'],
                 ['ओः','अवोः','अवाम्'],
                 ['अवि','अवोः','ओषु'],
                 ['औः' 'आवौ' 'आवः']]
                 
                 
a_stem_feminine=[['आ','ए','आः'],
                 ['आम्','ए','आः'],
                 ['अया','आभ्याम्','आभिः'],
                 ['आयै','आभ्याम्','आभ्यः'],
                 ['आयाः','आभ्याम्','आभ्यः'],
                 ['आयाः','अयोः','आनाम्'],
                 ['आयाम्','अयोः','आसु'],
                 ['ए','ए', 'आः']]
                 
i_stem_feminine=[['इः','ई','अयः'],
                ['इम्','ई','ईः'],
                ['या','इभ्याम्','इभिः'],
                ['यै','इभ्याम्','इभ्यः'],
                ['याः','इभ्याम्','इभ्यः'],
                ['याः','योः','ईनाम्'],
                ['याम्','योः','इषु'],
                ['ए','ई','अयः']]
                
ii_stem_feminine=[['ई','यौः','यः'],
                 ['ईम्','यौः','ईः'],
                 ['या', 'ईभ्याम्','ईभिः'],
                 ['यै','ईभ्याम्','ईभ्यः'],
                 ['याः','ईभ्याम्','ईभ्यः'],
                 ['याः','योः','ईनाम्'],
                 ['याम्','योः','ईषु'],
                 ['इ','यौ','यः']]

u_stem_feminine=[['उः','ऊ','अवः'],
                 ['उम्','ऊ','ऊः'],
                 ['वा','उभ्याम्','उभिः'],
                 ['वै','उभ्याम्','उभ्यः'],
                 ['वाः','उभ्याम्','उभ्यः'],
                 ['वाः','वोः','ऊनाम्'],
                 ['वाम्','वोः','उषु'],
                 ['ओ','ऊ','अवः']]
                 
uu_stem_feminine=[['ऊः','वौ','वः'],
                  ['ऊम्','वौ','ऊः'],
                  ['वा','ऊभ्याम्','ऊभिः'],
                  ['वै','ऊभ्याम्','ऊभ्यः'],
                  ['वाः','ऊभ्याम्','ऊभ्यः'],
                  ['वाः','वोः','ऊनाम्'],
                  ['वाम्','वोः','ऊषु'],
                  ['उ','वौ','वः']]
                  
r_stem_feminine=[['आ','अरौ','अरः'],
                 ['अरम्','अरौ','ऋः'],
                 ['रा','ऋभ्याम्','ऋभिः'],
                 ['रे','ऋभ्याम्','ऋभ्यः'],
                 ['उः','ऋभ्याम्','ऋभ्यः'],
                 ['उः','रोः','ऋृणाम्'],
                 ['अरि','रोः','ऋषु'],
                 ['अः','अरौ','अरः']]
                 
oo_stem_feminine=[['औः','आवौ','आवः'],
                  ['आवम्','आवौ','आवः'],
                  ['आवा','औभ्याम्','औभिः'],
                  ['आवे','औभ्याम्','औभ्यः'],
                  ['आवः','औभ्याम्','औभ्यः'],
                  ['आवः','आवोः','आवाम्'],
                  ['आवि','आवोः','औषु'],
                  ['औः','आवौ','आवः']]  
                  
c_stem_feminine=[['अक्-ग्','अचौ','अचः'],
                 ['अचम्','अचौ','अचः'],
                 ['अचा','अग्भ्याम्','अग्भिः'],
                 ['अचे','अग्भ्याम्','अग्भ्यः'],
                 ['अचः','अग्भ्याम्','अग्भ्यः'],
                 ['अचः','अचोः','अचाम्'],
                 ['अचि','अचोः','अक्षु'],
                 ['अक्-ग्','अचौ','अचः']]
                 
t_stem_feminine=[['त','अतौ','अतः'],
                 ['अतम्','अतौ','अतः'],
                 ['अता','दभ्याम्','दभिः'],
                 ['अते','दभ्याम्','दभ्यः'],
                 ['अतः','दभ्याम्','दभ्यः'],
                 ['अतः','अतोः','अताम्'],
                 ['अति','अतोः','तसु'],
                 ['त','अतौ','अतः']]
                 
sh_stem_feminine=[['अक्-ग्','अशौ','अशः'],
                 ['अशम्','अशौ','अशः'],
                 ['अशा','अग्भ्याम्','अग्भिः'],
                 ['अशे','अग्भ्याम्','अग्भ्यः'],
                 ['अशः','अग्भ्याम्','अग्भ्यः'],
                 ['अशः','अशोः','अशाम्'],
                 ['अशि','अशोः','अक्षु'],
                 ['अक्-ग्','अशौ','अशः']]
                 
h_stem_feminine=[['अत्','अहौ','अहः'],
                 ['अहम्','अहौ','अहः'],
                 ['अहा',' अद्भ्याम्','अद्भिः'],
                 ['अहे','अद्भ्याम्','अद्भ्यः'],
                 ['अहः','अद्भ्याम्','अद्भ्यः'],
                 ['अहः','अहोः','अहाम्'],
                 ['अहि','अहोः','अत्सु'],
                 ['अत्','अहौ','अहः']]
           
dh_stem_feminine=[['अत्','अधौ','अधः'],
                 ['अधम्','अधौ','अधः'],
                 ['अधा','द्भ्याम्','द्भिः'],
                 ['अधे','द्भ्याम्','द्भ्यः'],
                 ['अधः','द्भ्याम्','द्भ्यः'],
                 ['अधः','अधोः','अधाम्'],
                 ['अधि','अधोः','त्सु'],
                 ['अत्','अधौ','अधः']]
                 
a_stem_neuter=[['अम्','ए','आनि'],
                ['अम्','ए','आनि'],
                ['एन','आभ्याम्','ऐः'],
                ['आय','आभ्याम्','एभ्यः'],
                ['आत्','आभ्याम्','एभ्यः'],
                ['अस्य','अयोः','आनाम्'],
                ['ए','अयोः','एषु'],
                ['अ','औ','आः']]
                
all_D_forms=[a_stem_masculine,i_stem_masculine,u_stem_masculine,r_stem_masculine,o_stem_masculine,
          a_stem_feminine,i_stem_feminine,ii_stem_feminine,u_stem_feminine,uu_stem_feminine,r_stem_feminine,oo_stem_feminine,
          t_stem_feminine,c_stem_feminine,h_stem_feminine,dh_stem_feminine,sh_stem_feminine,a_stem_neuter]
#          i_stem_neuter,u_stem_neuter,r_stem_neuter,n_stem_masculine,t_stem_masculine,s_stem_masculine,
#          t_stem_feminine,c_stem_feminine,t_stem_neuter,s_stem_neuter]
dict_forms={0:'a_stem_masculine',
           1:'i_stem_masculine',
           2:'u_stem_masculine',
           3:'r_stem_masculine',
           4:'o_stem_masculine',
           5:'a_stem_feminine',
           6:'i_stem_feminine',
           7:'ii_stem_feminine',
           8:'u_stem_feminine',
           9:'uu_stem_feminine',
           10:'r_stem_feminine',
           11:'oo_stem_feminine',
           12:'t_stem_feminine',
           13:'c_stem_feminine',
           14:'sh_stem_feminine',
           15:'h_stem_feminine',
           16:'dh_stem_feminine',
           17:'a_stem_neuter',
           18:'i_stem_neuter',
           19:'u_stem_neuter',
           20:'r_stem_neuter',
           21:'n_stem_masculine',
           22:'t_stem_masculine',
           23:'s_stem_masculine',
           24:'t_stem_neuter',
           25:'s_stem_neuter'}
