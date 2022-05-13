a = "1010"
b = "1011"
aux=0
i=len(a)-1
j=len(b)-1
resultado=""
while(i>=0 and j>=0):
    if(a[i]=='1' and b[j]=='1'):

        if(aux==0):
            resultado='0'+resultado
            aux=1
        else:
            resultado='1'+resultado
            aux=1
    elif(a[i]=='0' and b[j]=='0'):
        if(aux==1):
            resultado='1'+resultado
            aux=0
        else:
            resultado='0'+resultado
    else:
        if (aux == 1):
            resultado = '0' + resultado
            aux=1
        else:
            resultado = '1' + resultado
    i-=1
    j-=1
if(i>=0):
    while i>=0:
        if(a[i]=='1' and aux==1):
            resultado='0'+resultado
        elif(a[i]=='0' and aux==0):
            resultado='0'+resultado
        else:
            resultado='1'+resultado
            aux=0
        i-=1
if(j>=0):
    while j >=0:
        if (a[j] == '1' and aux == 1):
            resultado = '0' + resultado
        elif (a[j] == '0' and aux == 0):
            resultado = '0' + resultado
        else:
            resultado = '1' + resultado
            aux = 0
        j -= 1
if(aux==1):
    resultado='1'+resultado
print(resultado)



