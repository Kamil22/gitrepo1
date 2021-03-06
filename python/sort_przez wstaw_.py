#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sort_przez wstaw_.py


def sort_przez_wstaw(lista):
    for i in range(1, len(lista)):
        el = lista[i]
        k = i - 1
        while k >= 0 and lista[k] > el:
            lista[k+1] = lista[k]
            k -= 1
        lista [k + 1] = el
    return lista

def sort_przez_wstaw_bin(lista):
     for i in range(1, len(lista)):
        el = lista[i]
        k = i - 1
        while k >= 0 and lista[k] > el:
            lista[k+1] = lista[k]
            k -= 1
        lista [k + 1] = el
    return lista

def main(args):
    lista = [4, 3, 7, 0, 3, 4, 1, 9]
    print(lista)
    print(sort_przez_wstaw(lista))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
