/*
 * sumuj.cpp
 * Program pobiera liczby od użytkownika aż ich suma przekroczy 100. 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    // int i;
    int suma = 0;
    int liczba = 0;
    int ilosc = 0;
    cout << "Wprowadzaj kolejne liczby" <<endl;
    // for (;;)
    while (1) //pętla nieskończona 
    {
         cin >> liczba;
         cout << " Podano: " << liczba << endl;
         ilosc++;
         suma += liczba;
         if (suma > 100)
            break;
    }
    cout <<"Suma liczb: " << suma << endl;
    cout << "Wprowadzono liczb: " << ilosc << endl;
   
    return 0;
}       
