# -*- coding: utf-8 -*-
"""
@author: sourabh garg
"""
from Declension import Declension


print("Declension of 'नदी':")
Declension('नदी','feminine')

print("Declension of 'पोतृ':")
Declension('पोतृ','masculine')

print("Declension of 'युष्मद्':")
Declension('युष्मद्')   # no gender required


print("Declension of 'तत्':")
Declension('तत्','neuter') 

print("Declension of 'विद्वस्':")
Declension('विद्वस्','masculine')


from Stemming import stem
print(stem('क्षु्त्सु'))
print(stem('युष्मान्'))
print(stem('पोत्रोः'))
print(stem('अस्य'))
print(stem('विद्वद्भ्यः'))
''' see above declensions'''