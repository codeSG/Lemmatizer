"""
@author: sourabh garg
Some noun words classied according to their declension type
"""
import itertools
a_stem_masculine=['राम','देव','बाल','बालक','नर','सिंह','जन','गज','अश्व','घट','कूप','भ्रमर',
                  'खग','छात्र','सागर','रोष','रन','ज्वर','व्याघ्र','वृक्ष','भ्रम','धीवर','क्रोध','देह',
                  'नापित','मूषक','सुत','सर्प','ऋक्ष','शूकर','वृक','शृगाल','शशक','वानर',
                  'वृषभ','उष्ट्र','गर्दभ','कुक्कर','मार्जार','अज','प्रासाद','यव','क्षेत्र-पालक','मूर्ख','चोर','मोक्ष'
                  'जनक','पुत्र','उपाध्याय','सूर्य','चन्द्र','प्राज्ञ','वर्ण','लोभ','मार्ग','प्रश्न']
i_stem_masculine=['गिरि','हरि','रवि','कवि','अरि','असि','निधि','कपि','पाणि','विधि','अतिथि','भूपति','अग्नि',
                  'रश्मि','तिथि','सारथि','अद्रि','पति','कवि','मुनि','सुरपति','नृपति','श्रीपति','महीपति','ऋषि','व्याधि','यति']
u_stem_masculine=['गुरु','साधु','शिशु','शम्भु','विष्णु','अभिमन्यु','पशु','केतु','सिन्धु','मन्यु','विधु','भानु','सूनु','वायु',
                  'प्रभु','जानु','वाहु','सेतु','तरु','इषु','सुधांशु','शुभ्रांशु','ऋतु','इक्षु','शत्रु','तन्तु','बिन्धु','बन्धु','इन्दु','तरु']
r_stem_masculine_1=['पितृ','भ्रातृ','जामातृ','पोतृ','नप्तृ','देवृ','दुहितृ','नृ']
r_stem_masculine_2=['कर्तृ','दातृ','वक्तृ','भर्तृ','होतृ','हर्तृ','धर्तृ','श्रोतृ','गन्तृ','द्रष्टृ','नेतृ','भोक्तृ','जेतृ','द्रष्टृ','स्रष्टृ','धातृ','सवितृ']
o_stem_masculine=['गो','द्यो']
a_stem_feminine=['रमा','बालिका','लता','कमला','सरला','निर्मला','आशा','दुर्गा','विद्या','दया','कृपा',
                 'गंगा','कथा','माला','कोकिला','वाटिका','नासिका','प्रभा','शाला','कन्या','कला',
                 'अजा','वसुधा','सुधा','लज्जा','प्रजा','शिला','यमुना','क्षमा','निशा','जटा','आज्ञा','सुधा']
i_stem_feminine=['मति','भक्ति','बुद्धि','प्रीति','स्तुति','श्रुति','धृति','स्मृति','कीर्ति','कान्ति',
                 'जाति','मुक्ति','शक्ति','आकृति','हानि','रीति','भूमि','रूचि','दृष्टि','सृष्टि',
                 'संपत्ति','वृद्धि','नीति','शुद्धि','रात्रि','वृष्टि','गति','कृति','भूति','उक्ति','युक्ति','शान्ति','प्रवृत्ति','प्रणति','समृद्धि','अंगुलि']
ii_stem_feminine=['नदी','काशी','गौरी','पार्वती','लक्ष्मी','काली','भवानी','तरी','तन्त्री','कुमारी',
                  'नारी','जननी','नगरी','दासी','पृथ्वी','मैत्री','श्रेणी','पुत्री','धात्री','भागीरथी',
                  'स्त्री','श्री','सिंही','वाणी','पत्नी','सखी','देवी','वाराणसी','भगिनी','मही','रजनी','पुरी','सरस्वती','बुद्धिमती','ब्राह्मणी','सर्पिणी',
                  'राज्ञी','श्रीमती','भवती','कौमुदी','कमलिनी','इन्द्राणी']
u_stem_feminine=['धेनु','तनु','हनु','रज्जु','रेणु','चञ्चु']
uu_stem_feminine=['वधू','जम्बू','श्मश्रू']
r_stem_feminine=['मातृ','स्वसृ','दुहितृ','यातृ','ननान्दृ']
oo_stem_feminine=['नौ']
a_stem_neuter=['फल','गृह','नगर','पुस्तक','सुख','खान','नेत्र','मुख','श्रोत्र','चिबुक','उदर','नेपथ्य','कपूर','धन',
               'वन','जल','मित्र','शरीर','वस्त्र','पुष्प','पाप','पुण्य','चक्र','कार्य','पत्र','सत्य','ज्ञान','नवनीत',
               'विष','गीत','कमल','आम्र','मुख']
i_stem_neuter_1=['वारि','शुचि']
i_stem_neuter_2=['दधि','अस्थि','अक्षि']
u_stem_neuter=['मधु','अश्रु','वसु','जानु','वस्तु','दारु','श्यश्रु','दारु','अम्बु']
r_stem_neuter=['कर्तृ','धातृ','ज्ञातृ']

n_stem_masculine_1=['राजन्','मूर्धन्','तक्षन्']
n_stem_masculine_2=['आत्मन्']
en_stem_masculine=['करिन्','पक्षिन्','दण्डिन्','विद्यार्थिन्','स्वामिन्','मन्त्रिन्','ज्ञानिन्','योगिन्','त्यागिन्','धनिन्','पथिन्']
t_stem_masculine_1=['भगवत्','भवत्','श्रीमत्','बुद्धिमत्','धनवत्','बलवत्','महत्']
t_stem_masculine_2=['गतवत्','गच्छत्','कुर्वत्','गायत्', 'तिष्ठत्', 'धावत्', 'नृत्यत्', 'पश्यत्', 'पिवत्', 'भवत्', 'गमिष्यत्', 'करिष्यत्', 'हसत्']
t_stem_masculine_3=['भूभृत्']
s_stem_masculine=['विद्वस्','चन्द्रमस्']
c_stem_masculine=['पयोमुच्','प्राच्', 'प्रत्यच्', 'उदच्', 'अवाच्', 'तोर्यच्', 'जलमुच्', 'सत्यवाच्']
j_stem_masculine=['भिषज्','वणिज्']
t_stem_feminine=['सरित्']
c_stem_feminine=['वाच्']
sh_stem_feminine=['दिश्']
h_stem_feminine=['उपानह्']
dh_stem_feminine=['क्षुध्']
d_stem_feminine=['विपद्','मुद्', 'आपद्', 'सम्पद्', 'शरद्', 'परिषद्', 'उपनिषद्']
t_stem_neuter=['जगत्']
s_stem_neuter=['पयस्','चेतस्', 'स्रोतस्',  'वचस्', 'अम्भस्', 'वक्षस्','यशस्','शिरस्','सरस्','मनस्','तमस्']
n_stem_neuter=['नामन्','अहन्','प्रेमन्','व्योमन्','धामन्','लोमन्','कर्मन्','चर्मन्','भस्मन्', 'जन्मन्', 'वेश्मन्', 'शर्मन्', 'वर्मन्']


all_noun=[a_stem_masculine,i_stem_masculine,u_stem_masculine,r_stem_masculine_1,r_stem_masculine_2,o_stem_masculine,
          a_stem_feminine,i_stem_feminine,ii_stem_feminine,u_stem_feminine,uu_stem_feminine,r_stem_feminine,oo_stem_feminine,
          a_stem_neuter,i_stem_neuter_1,i_stem_neuter_2,u_stem_neuter,
          en_stem_masculine,t_stem_masculine_1,t_stem_masculine_2,t_stem_masculine_3,
          n_stem_masculine_1,n_stem_masculine_2,c_stem_masculine,j_stem_masculine,
          t_stem_feminine,c_stem_feminine,h_stem_feminine,dh_stem_feminine,d_stem_feminine,sh_stem_feminine,
          t_stem_neuter,s_stem_neuter,n_stem_neuter]
dict_noun={0:'a_stem_masculine',
           1:'i_stem_masculine',
           2:'u_stem_masculine',
           3:'r_stem_masculine_1',
           4:'r_stem_masculine_2',
           5:'o_stem_masculine',
           6:'a_stem_feminine',
           7:'i_stem_feminine',
           8:'ii_stem_feminine',
           9:'u_stem_feminine',
           10:'uu_stem_feminine',
           11:'r_stem_feminine',
           12:'oo_stem_feminine',
           13:'a_stem_neuter',
           14:'i_stem_neuter_1',
           15:'i_stem_neuter_2',
           16:'u_stem_neuter',
           17:'en_stem_masculine',
           18:'t_stem_masculine_1',
           19:'t_stem_masculine_2',
           20:'t_stem_masculine_3',
           21:'n_stem_masculine_1',
           22:'n_stem_masculine_2',
           23:'c_stem_masculine',
           24:'j_stem_masculine',
           25:'t_stem_feminine',
           26:'c_stem_feminine',
           27:'h_stem_feminine',
           28:'dh_stem_feminine',
           29:'d_stem_feminine',
           30:'sh_stem_feminine',
           31:'t_stem_neuter',
           32:'s_stem_neuter',
           33:'n_stem_neuter'}
pronoun=['अस्मद्','युष्मद्','यत्','तत्','एतत्','किम्','भवत्','सर्व','इदम्']
unique=['स्त्री','विद्वस्','पथिन्','सम्राज्']