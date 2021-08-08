#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# 06-COMB-P06.py
#
# Author: Covarrubias Minez Brandon Iván
# License: MIT
# GitHub: https://github.com/okatro/Programa-6
#
# Convert numbers from the decimal system to the roman system
#
# ## ###############################################################
import sys
from collections import OrderedDict

def main(argv):
    #Check the input
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage "+argv[0]+" d")
        exit(0)

    dec= int(argv[1])
    #Conversion limit
    if dec > 1999999:
        print("Max: 1999999")
        exit(0)

    print(DetoRo(dec))
	

#Decimal to Roman
def DetoRo(dec):
    Res="";
    #Dictionary
    R=[
        (1000000 , "M\u0305"),
        (900000 , "C\u0305M\u0305"),
        (800000 , "D\u0305C\u0305C\u0305C\u0305"),
        (700000 , "D\u0305C\u0305C\u0305"),
        (600000 , "D\u0305C\u0305"),
        (500000 , "D\u0305"),
        (400000 , "C\u0305D\u0305"),
        (300000 , "C\u0305C\u0305C\u0305"),
        (200000 , "C\u0305C\u0305"),
        (100000 , "C\u0305"),
        (90000 , "X\u0305C\u0305"),
        (80000 , "L\u0305X\u0305X\u0305X\u0305"),
        (70000 , "L\u0305X\u0305X\u0305"),
        (60000 , "L\u0305X\u0305"),
        (50000 , "L\u0305"),
        (40000 , "X\u0305L\u0305"),
        (30000 , "X\u0305X\u0305X\u0305"),
        (20000 , "X\u0305X\u0305"),
        (10000 , "X\u0305"),
        (9000 , "I\u0305X\u0305"),
        (8000 , "V\u0305I\u0305I\u0305I\u0305"),
        (7000 , "V\u0305I\u0305I\u0305"),
        (6000 , "V\u0305I\u0305"),
        (5000 , "V\u0305"),
        (4000 , "I\u0305V\u0305"),
        (3000 , "MMM"),
        (2000 , "MM"),
        (1000 , "M"),
        (900 , "CM"),
        (800 , "DCCC"),
        (700 , "DCC"),
        (600 , "DC"),
        (500 , "D"),
        (400 , "CD"),
        (300 , "CCC"),
        (200 , "CC"),
        (100 , "C"),
        (90 , "XC"),
        (80 , "LXXX"),
        (70 , "LXX"),
        (60 , "LX"),
        (50 , "L"),
        (40 , "XL"),
        (30 , "XXX"),
        (20 , "XX"),
        (10 , "X"),
        (9 , "IX"),
        (8 , "VIII"),
        (7 , "VII"),
        (6 , "VI"),
        (5 , "V"),
        (4 , "IV"),
        (3 , "III"),
        (2 , "II"),
        (1 , "I")
    ]

    #Conversion
    while dec > 0:
        for d,r in R:
            if dec/d >= 1:
                Res+=r
                dec-=d
    #returns 0 if input is 0
    return Res if len(Res)!=0 else "0"

if __name__ == '__main__':
	main(sys.argv)
