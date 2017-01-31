# -*- coding: utf-8 -*-
"""
@author: sourabh garg
"""
from Declension import Declension
from Stemming import stem,case_number

#Declension
print("Declension of 'नदी':")
Declension('नदी','feminine')

print("Declension of 'पोतृ':")
Declension('पोतृ','masculine')

print("Declension of 'युष्मद्':")
Declension('युष्मद्')   # no gender required

print("Declension of 'तद्':")
Declension('तद्','neuter') 

print("Declension of 'विद्वस्':")
Declension('विद्वस्','masculine')

#stem lookup
print(stem('क्षु्त्सु'))
print(stem('युष्मान्'))
print(stem('पोत्रोः'))
print(stem('अस्य'))
print(stem('विद्वद्भ्यः'))

#case & number
print(case_number('पोतृन्','eng'))
print(case_number('अस्य','hi'))
print(case_number('विद्वांसौ','hi'))
print(case_number('राज्ञे','eng'))
