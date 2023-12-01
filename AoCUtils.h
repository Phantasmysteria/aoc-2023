#ifndef AOCUTIL
#define AOCUTIL

#define varName(v) (#v)

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <typeinfo>
#include <unordered_set>

using namespace std;

// Basic Read Lines, modify type whenever
vector<string> readLines(string filename)
{
    ifstream file(filename);
    string line;
    vector<string> result;

    while (getline(file, line)) {result.push_back(line);}

    return result;
}

template <typename T>
void print1Dcontainer(T input)
{
    cout << "\n=======================\n";
    cout << "Printing " << typeid(input).name() << "\n\n";
    cout << varName(input) << ": ";
    for (auto i : input) {cout << i << " ";}
    cout << "\n=======================\n";
}

template <typename T>
void print2Dcontainer(T input)
{
    cout << "\n=======================\n";
    cout << "Printing " << typeid(input).name() << "\n\n";
    cout << varName(input) << ": \n";
    for (auto i : input) {for (auto j : i) {cout << j << " ";} cout << "\n";} 
    cout << "\n=======================\n";
}

template <typename T>
vector<T> readLinewithComma(string input)
{
    istringstream iss(input);
    string line;
    vector<T> result;

    while (getline(iss, line, ',')) {result.push_back(line);}

    return result;
}


#endif