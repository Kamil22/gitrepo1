import random

def losuj(ileliczb, maksliczb):
    liczby = []

    ile = 0
    # for i in range(ileliczb):
    while ile < ileliczb:
        liczba = random.randint(0, maksliczb)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            ile += 1

    #  print(liczby)
    return liczby
    
    
def minimum(lista):
    min = lista[0]
    for i, el in enumerate(lista):
        print(i, el)
    return 0
    
def main(args):
    lista = losuj (20, 50)
    print ("Min:", minimum(lista))
    print (lista)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
