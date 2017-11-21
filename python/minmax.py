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


def main(args):
    lista = losuj(20, 50)
    print (lista)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
