# -*- coding: utf-8 -*-
"""
@author: sourabh garg
"""
from Declension import Declension
from Stemming import stem

#Declension
print("Declension of 'नदी':")
Declension('नदी','f')

print("Declension of 'पोतृ':")
Declension('पोतृ','m')

print("Declension of 'विद्वस्':")
Declension('विद्वस्','m')

#stem lookup
print(stem('क्षुत्सु'))

print(stem('पोत्रोः'))

print(stem('विद्वद्भ्यः'))

