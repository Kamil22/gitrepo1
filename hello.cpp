/*
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
using namespace std;

int main(int argc, char **argv)
{
	//char imie;// deklaracja zmiennej znakowej
    char imie [10]; //
    int wiek;
    wiek = 0; //inicjacja zmiennej 
    
    
    cout << "Witaj w C++!";
    cout << "Podaj imie: " ;
    // cin >> imie ;
    cin.getline(imie, 10);
    cout << "Cześć, " <<imie<< "!" << endl ;
    cin.ignore();
    cout << "Ile masz lat? ";
    cin>> wiek;
    cout << "Urodziłeś się w roku " << 2017 - wiek << endl;

	return 0; 
}
