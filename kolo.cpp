#include <cstdlib>
#include <iostream>
#include <math.h>

using namespace std;

int main(int arge, char *argv[])
{
    double pole_kola, PI, R;
    PI = 3.14;
    cout << "podaj promien kola: ";
    cin >> R;
    pole_kola = PI * R * R;
    cout << "pole kola o promieniu R wynosi: ";
    cout << pole_kola << endl;
    system("PAUSE");
    double obwod_kola, P, r ;
    P = 3.14;
    cout << "podaj promien: ";
    cin >> r;
    obwod_kola = 2 * P * r;
    cout << "obwod kola wynosi: ";
    cout << obwod_kola<< endl;

    system("PAUSE");
}

