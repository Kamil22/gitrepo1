

def nwd(a,b):

    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
            return a

def main (args):

    a=int(input('Podaj liczbę naturalną: '))
    b=int(input('Podaj liczbe naturalną: '))

print ('Największy wspolny dzielnik', nwd(a,b) )

return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
