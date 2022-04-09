a =[1,1,2,3,4,5]
b=[3,4,5,6]
#https://python-reference.readthedocs.io/en/latest/docs/sets/
#zip tiene como entradas dos arreglos y regresa tuplas.
# dict recibe las tuplas y las transforma ne elementos de los diccionario
diccionario1 = dict(zip(a,a))
diccionario2 = dict(zip(b,b))
b =diccionario1.keys() & diccionario2.keys() #se pueden usar operaciones entre diccionarios & en este caos es la intewrseccion
print(sorted(b))#sorted regres una lista ordenada d elso elementos, lo use solo porque retorna uan lista