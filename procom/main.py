# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''''
def inlens(s: str, i: int):
    if(i>=0 and i<len(s)):
        return True
    return False

def definirvalor(caracterOpcional, lista, indexCaracterctual, sumandoValorActual, sumandoValorOpconal):
    acumulado = sumandoValorActual
    avance=1
    if(inlens(lista, indexCaracterctual-1)):
        if(lista[indexCaracterctual-1] == caracterOpcional):
            acumulado-=sumandoValorOpconal
            avance+=1
    return acumulado, avance
'''''

def romanToInt(s: str):
    def inlens(s: str, i: int):
        if (i >= 0 and i < len(s)):
            return True
        return False

    def definirvalor(caracterOpcional, lista, indexCaracterctual, sumandoValorActual, sumandoValorOpconal):
        acumulado = sumandoValorActual
        avance = 1
        if (inlens(lista, indexCaracterctual - 1)):
            if (lista[indexCaracterctual - 1] == caracterOpcional):
                acumulado -= sumandoValorOpconal
                avance += 1
        return acumulado, avance

    valor = 0
    i = len(s)-1
    while (i >= 0):
        n = s[i]
        print(n =='I')
        if(n == 'I'):
            valor+=1
            i-=1
        elif(n == 'V'):
            acumulado, avance = definirvalor('I', s, i,5, 1)
            valor+= acumulado
            i-=avance
        elif(n == 'X'):
            acumulado, avance = definirvalor('I', s, i,10, 1)
            valor += acumulado
            i -= avance
        elif (n == 'L'):
            acumulado, avance = definirvalor('X', s, i,50, 10)
            valor += acumulado
            i -= avance
        elif (n == 'C'):
            acumulado, avance = definirvalor('X', s, i,100, 10)
            valor += acumulado
            i -= avance
        elif (n == 'D'):
            acumulado, avance = definirvalor('C', s, i,500, 100)
            valor += acumulado
            i -= avance
        elif (n == 'M'):
            acumulado, avance = definirvalor('C', s, i,1000, 100)
            valor += acumulado
            i -= avance

    return valor








def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a=input("cadena")
    valor=romanToInt(a)
    print("valor: %4d"% valor)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
