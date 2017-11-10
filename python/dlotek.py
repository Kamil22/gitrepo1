#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dlotek.py


import random


def losuj(ileliczb, maksliczb):
    liczby = []  # zbiór pusty

    ile = 0
    # for i in range(ileliczb):
    while ile < ileliczb:
        liczba = random.randint(0, maksliczb)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            ile += 1


    return liczby




def pobierz_typy(ileliczb):
    typy = set()
    ile = 0
    while ile < ileliczb:
        typ = int(input('Podaj typ: '))
        if typ not in typy:
            typy.add(typ)
        ile += 1

    print(typy)
    return typy

    print(liczby)
    return liczby



def main(args):
    ileliczb = int(input("Ile liczb chcesz zgadywać?"))
    maksliczb = int(input("Maksymalna losowana liczba: "))


    while ileliczb > maksliczb or ileliczb < 1:
        ileliczb = int(input("Ile liczb chcesz zgadnąć z %s liczb?" % maksliczb))

    liczby = losuj(ileliczb, maksliczb)
    typy = pobierz_typy(ileliczb)

    trafione = set(liczby) & typy
    print ("Trafiłeś", len(trafione), 'liczby.')

    liczby = losuj(ileliczb, maksliczb)

    # pobieranie typów użytkownika
    typy = set()  # pusty zbiór
    # for i in range(ileliczb):
    ile = 0
    while ile < ileliczb:
        typ = input("Podaj typ: ")
        if typ not in typy:
            typy.add(typ)
            ile += 1

    print(typy)


    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
