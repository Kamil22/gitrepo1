#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szyfr_cezara.py
#  
# 
def szyfruj_cezar(tekst, klucz):
    klucz = klucz % 26
    szyfrogram = ""
    for znak in tekst:
        znak = znak.upper()  # .lower też może być
        ascli =  ord(znak) + klucz
        if ascli > 90:
            ascli -= 26
        szyfrogram += chr(ascli)
    return szyfrogram
    
    def deszyfruj(szyfrogram, klucz):
        tekst = ""
        pass
        return tekst 

def main(args):
    tekst = input("Podaj tekst :")
    klucz = int(input("Klucz: "))

    szyfrogram = szyfruj_cezar(tekst, klucz)
    print(szyfrogram)

    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
