it/*
 * hello.cpp
 * 
 * Copyright 2017  <>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char **argv)
{
	

    int a, b, c; // deklaracja i inicjacja zmiennej
    int obwod = 0;
    float p = 0;
    a = b = c = 0;
    cout << "Podaj boki: " <<endl;
    cin >> a >> b >> c;
    //~if (a + b > c) {
        //~if (a + c > b) {
            //~if (b + c > a) {
                //~cout << "Da się utworzyć";
            //~ }
        //~ }
            
    //~ }
    if (a + b > c && a + c > b && b + c > a) {
        obwod = a + b + c;
        cout << "Obwód: " << obwod << endl;
        p = 0.5 * obwod;
        cout << "Współczynnik: " << p << endl;
        cout << "Pole: " << sqrt(p*(p-a)*(p-b)*(p-c));
    } else {
        cout << "Nie da się!";
    }
    
     


    
	return 0; 
}
