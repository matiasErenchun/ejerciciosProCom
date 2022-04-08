dijitos = '2'
diccionario = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
i = 0
arreglosalida = []
while i < len(dijitos):
    arreglo = []
    digitoactual = diccionario[dijitos[i]]
    if (len(arreglosalida) == 0):
        for j in digitoactual:
            arreglosalida.append(j)
    else:
        for k in arreglosalida:
            for l in digitoactual:
                arreglo.append(k + l)
        arreglosalida = arreglo
    i += 1
print(arreglosalida)
