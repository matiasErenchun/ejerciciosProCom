import random

def movimientoValido( matriz,i,j):
    if(i>=0 and i<len(matriz) and j>=0 and j<len(matriz)):
        if(matriz[i][j]!='x'):
            return True
    return False

def movimientos():
    cuadros = random.randint(1,3)
    return cuadros

def moverArriva(matriz,i,j):
    mover = movimientos()
    contador=0
    while contador<mover:
        print(i)
        if(movimientoValido(matriz,i-1,j)):
            matriz[i-1][j]='A'
            matriz[i][j] ='_'
            i-=1
        contador+=1
    return matriz,i,j

def moverAbajo(matriz,i,j):
    mover = movimientos()
    contador=0
    while contador<mover:
        if(movimientoValido(matriz,i+1,j)):
            matriz[i+1][j]='A'
            matriz[i][j] ='_'
            i+=1
        contador+=1
    return matriz,i,j

def moverDerecha(matriz,i,j):
    mover = movimientos()
    contador=0
    while contador<mover:
        if(movimientoValido(matriz,i,j+1)):
            matriz[i][j+1]='A'
            matriz[i][j] ='_'
            j+=1
        contador+=1
    return matriz,i,j

def moverIzquierda(matriz,i,j):
    mover = movimientos()
    contador=0
    while contador<mover:
        if(movimientoValido(matriz,i,j-1)):
            matriz[i][j-1]='A'
            matriz[i][j] ='_'
            j-=1
        contador+=1
    return matriz,i,j

def printMatriz(matriz):
    i=0
    while i<len(matriz):
        print(matriz[i])
        i+=1



matriz=[['_','x','_'],['_','x','_'],['_','_','_']]
i=0
j=0
matriz[i][j]='A'
continuar=True
while continuar:
    printMatriz(matriz)
    print("0 arriba, 1 abajo, 2 izquierda y 3 derecha ")
    opcion=int(input("ingrese su Opcion:"))
    if(opcion==0):
        matriz,i,j=moverArriva(matriz,i,j)
    elif(opcion==1):
        matriz,i,j=moverAbajo(matriz,i,j)
    elif(opcion==2):
        matriz,i,j=moverIzquierda(matriz,i,j)
    elif(opcion==3):
        matriz,i,j=moverDerecha(matriz,i,j)
    else:
        print("opciona erronea")
    printMatriz(matriz)
    seguir=int(input("si desea continuar ingrese 1"))
    if(seguir!=1):
        continuar=False

print("Bye Bye Bro")
