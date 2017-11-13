#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potęga.py



def potega_it(x, n):

    i = 1
    wynik = 1
    while 1 <= n:
        wynik = wynik * x
        i = i + 1
        
    return wynik


def main(args):
    x = float(input("Podaj podstawe potęgi: "))
    n = int(input("Podaj wykładnik potęgi: "))
    print("Wynik: ", potega_it(x, n))
    return 0

if _name_ == '_main_':
    import sys
    sys.exit(main(sys.argv))
