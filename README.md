# Stemmer


##About
Stemming is a core task for NLP which relates different inflected(or sometimes derived forms) of a given word to their word stem, base or root. For example, In english,A stemming algorithm reduces the words "fishing", "fished", and "fisher" to the root word, "fish" by removing the corresponding suffixes. But For highly inflected languages like *Sanskrit*, the task is even more ambiguous as words often have more than two dozen possible forms which also varies depending on various criteria like gender, their ending character etc.
Our algorithm tags all possible inflected words to their word stem/main noun for sanskrit language.


##How to use?
To use the funtionality of this stemmer , First you have to import the module named, Stemming, Then, there is a method called stem which takes any sanskrit inflected word(presently only for nominal class) in 'Devanagari script' and outputs its word stem .

In [1]:from Stemming import stem

In [2]: stem('नद्योः') 

Out [2]: नदी 


##How it works?
Our stemming algorithm is based on two conventional approaches searching in lookup tables and longest matching algorithm.
 
###Matching algorithms
We use a stem database (word_tagging module which contain stem words). These stems, as mentioned above, are  valid noun stem themselves. In order to stem a word the algorithm tries to match it with stems from the database, using various methods:First it complete tokenize the given inflected word as phoneme(consonants and vowel) sequence, for e.g. ['गुरवे'='ग्'+ 'उ'+ 'र'+ 'व'+'ए'].  Then, it find most likely match for it in the stem database using trie, if it found a approximate matching noun word , it searches the inflected word in its declension, if there exist an exact match, it returns the noun word as stem, otherwise it truncates the inputed word and repeat the above procedure till its actual word stem is found. 

###Lookup tables(Declension)
Generally, A simple stemmer looks up the inflected form in a lookup table where all the inflected forms are explicitly listed, hence the table becomes large. For languages with simple morphology, like English, table sizes are modest, but highly inflected languages like Sanskrit have many potential inflected forms for each word stem.So, for this I use a production technique which produced declension table when required.For example, if the word is "'रामः'", then the Declension_noun method will automatically generate all the forms [['रामः', 'रामौ', 'रामाः'], ['रामम्', 'रामौ', 'रामाण्'], ['रामेण', 'रामाभ्याम्', 'रामैः'], ['रामाय', 'रामाभ्याम्', 'रामेभ्यः'], ['रामात्', 'रामाभ्याम्', 'रामेभ्यः'], ['रामस्य', 'रामयोः', 'रामाणाम्'], ['रामे', 'रामयोः', 'रामेषु'], ['हे राम', 'हे रामौ', 'हे रामाः']].
for complete flow chart of the algorithm, visit [Sanskrit_Stemmer](https://github.com/codeSG/Stemmer/blob/master/Sanskrit_Stemmer.pdf)

###Supplimentary modules:
######Sandhi(Joint)

The Sandhi module is use to concatenate two sanskrit string by applying several rules. It takes two phoneme streams (in devanagari script) and gives as result their sandhi euphonic composition.
It presently contains:
**स्वर संधि**-दो स्वरों के मेल से होने वाले विकार (परिवर्तन) को स्वर-संधि कहते हैं। जैसे - विद्या + आलय = विद्यालय।
स्वर-संधि पाँच प्रकार की होती हैं -

1.)दीर्घ संधि

2.)गुण संधि

3.)वृद्धि संधि

4.)यण संधि

5.)अयादि संधि

In [1]: from Sandhi import sandhi

In [2]: sandhi('विधु' ,'उदयः') 

Out [2]: विधूदयः  

######Declension of any noun

It produces Declension table for any noun/ pronoun depending on its gender and ending character.for e.g.'गुरु'is male and ['गुरु'='ग्'+ 'उ'+ 'र'+ 'उ'] ends with 'उ' means it belongs to "u_stem_m"(<stem_type>+<gender>) declension form.
It takes noun and gender('m' for masculine, 'f' for feminine and 'n' for neuter word)as arguments and outputs its declension table where the case sequence is ['प्रथमा','द्वितीया','तृतीया','चर्तुथी','पन्चमी','षष्ठी','सप्तमी','सम्बोधन'].

In [1]: from Declension import Declension

In [2]: Declension('नामन्','m')

Out [2]: [['नाम', 'नामनी', 'नामानि'],

['नाम', 'नामनी', 'नामानि'], 

['नाम्ना', 'नामभ्याम्', 'नामभिः'],

['नाम्ने', 'नामभ्याम्', 'नामभ्यः'],

['नाम्नः', 'नामभ्याम्', 'नामभ्यः'], 

['नाम्नः', 'नाम्नोः', 'नाम्नाम्'],

['नाम्नि', 'नाम्नोः', 'नामसु'], 

['हे नाम', 'हे नामनी', 'हे नामानि']]

##Gratitute
I am greatly thankful to The Sankrit Heritage Site for the provided guidance.

##Author
* Sourabh Garg sourabh.8.june.1996@gmail.com @codeSG