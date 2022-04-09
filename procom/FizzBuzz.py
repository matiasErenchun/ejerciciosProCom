lista=[]
n=15
i=1
while i<=n:
    agregar=""
    if(i%3==0):
        agregar+="Fizz"
    if(i%5==0):
        agregar+="Buzz"
    if(len(agregar)==0):
        agregar=str(i)
    lista.append(agregar)
    i+=1
print(lista)
