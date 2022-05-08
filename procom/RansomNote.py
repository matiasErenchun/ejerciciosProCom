

a="aaaz"
b="aabj"
'''
if a in b:
    print(True)
else:
    print(False)
'''
letras ={}
for i in b:
    if i in letras:
        contenedor = letras[i]
        contenedor.append(i)
        letras[i]=contenedor
    else:
        contenedor =[]
        contenedor.append(i)
        letras[i]=contenedor
print(letras.values())
existe=True
for i in a:
    if i in letras:
        contenedor = letras[i]
        if(len(contenedor)>0):
            contenedor.pop()
            letras[i] = contenedor
        else:
            existe=False
            break
    else:
        existe = False
        break
print(existe)

