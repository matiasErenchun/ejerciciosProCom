

def inttoroman(i:int):

    def agregarValor(entero, valor, signo):
        veces=int(entero/valor)
        resto=entero%valor
        string =''
        i=0
        print(veces)
        while(i<veces):
            string=string+signo
            i+=1
        return  resto, string

    string =''
    while (i>0):
        if(i>=1000):
            valor, stringg = agregarValor(i,1000, 'M')
            i=valor
            string+=stringg
        elif(i>=900):
            valor, stringg = agregarValor(i,900, 'CM')
            i=valor
            string+=stringg
        elif (i >= 500):
            valor, stringg = agregarValor(i, 500, 'D')
            i = valor
            string += stringg
        elif (i >= 400):
            valor, stringg = agregarValor(i, 400, 'CD')
            i = valor
            string += stringg
        elif (i >= 100):
            valor, stringg = agregarValor(i, 100, 'C')
            i = valor
            string += stringg
        elif (i >= 90):
            valor, stringg = agregarValor(i, 90, 'XC')
            i = valor
            string += stringg
        elif (i >= 50):
            valor, stringg = agregarValor(i, 50, 'L')
            i = valor
            string += stringg
        elif (i >= 40):
            valor, stringg = agregarValor(i, 40, 'XL')
            i = valor
            string += stringg
        elif (i >= 10):
            valor, stringg = agregarValor(i, 10, 'X')
            i = valor
            string += stringg
        elif (i >= 9):
            valor, stringg = agregarValor(i, 9, 'IX')
            i = valor
            string += stringg
        elif (i >= 5):
            valor, stringg = agregarValor(i, 5, 'V')
            i = valor
            string += stringg
        elif (i >= 4):
            valor, stringg = agregarValor(i, 4, 'IV')
            i = valor
            string += stringg
        elif (i >= 1):
            valor, stringg = agregarValor(i, 1, 'I')
            i = valor
            string += stringg
    return string


a=int(input("entero"))
print(inttoroman(a))

