#include <iostream>
#include <algorithm>
#include <locale>
#include <iterator>

int alcuadrado(int a)
{
    return a*a;
}

std::string soloLetras(const std::string& str)
{
    std::locale loc("");

    std::string res;
    std::copy_if(str.begin(), str.end(), std::back_inserter(res),
                 [&loc](char c) { return std::isalpha(c, loc); });
    return res;
}

std::string  misoloLetras( std::string hola)
{
    std::cout << hola << std::endl;
    std::string copia = "";
    int i=0;
    while(i < hola.length())
    {
        if(std::isalnum(hola[i]))
        {
            copia.push_back(std::tolower(hola[i]));
        }
        i++;
    }
    std::cout << copia;
    return copia;
}

bool isPalindromo(std::string a)
{   bool pali= true;
    int i=0,j= a.length()-1;
    while (i<j)
    {
        if(a[i]!=a[j])
        {
            pali=false;
            i+=j;
        }
        i++;
        j--;
    }
    return pali;
}

bool isPalindromo2(std::string a)
{
    bool pali= true;
    int i=0,j = int(a.size()-1);
    while (i<=j)
    {
        if(!std::isalnum(a[i]))
        {
            i++;
        }
        else if (!std::isalnum(a[j]))
        {
            j--;
        }
        else
        {
            if(std::tolower(a[i])!= std::tolower(a[j]))
            {
                pali=false;
                i+=j;
            }
            i++;
            j--;
        }
    }
    return pali;
}

int main() {
    char a[40];
    /*
     * std::cout es el print de c++
     */
    std::cout << "ingrese una palabra: ";
    std::cin.getline(a,40);
    std::string  b (a);

    //std::cout << isPalindromo(misoloLetras(b)) << std::endl;
    std::cout << isPalindromo2(b);
    /*
     * por otra parte el std::cin permite leer elementos desde entrada estandar
     */
    std::cout << a << "\n";
    /*
     * recordar que std::endl limpia el buffer de salida
     * https://stackoverflow.com/questions/213907/stdendl-vs-n
    */
    std::string c = "bb";
    int j = std::isalnum(c[1]);
    return 0;
}
