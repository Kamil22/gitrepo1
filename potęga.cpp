/*
 * potęga.cpp
 * a0 = 1
 * a1 = a
 * an = a*...*a (n-czynników) dla n zaw. N+ - {1}
 */


#include <iostream>

using namespace std;

float potega_it(float x, int n) {
    
    float wynik = 1;
    for(int i = n ; n*n ; ) {
        // testuje ilość powtórzeń pętli
        cout << i << endl;
        
    }
    return wynik;
}

int main(int argc, char **argv)
{
	//pobierz od użytkownika podstawę i wykładnik
    int a = 0;
    int b = 0;
    cout << "Podaj podstawę: " << a << endl;
    cin >> a;
    cout << "Podaj wykładnik: " << b << endl;
    cin >> b;
    int x=0;
    int n=0;
     
    cout << "Potęga:" << potęga_it(x, n) <<endl;
	return 0;
}

