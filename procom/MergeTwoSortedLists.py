a=[]
b=[0]
resultado=[]
i=0
j=0
while(len(a)>i and len(b)>j):
    c=a[i]
    d=b[j]
    if(c<=d):
        resultado.append(c)
        i+=1
    else:
        resultado.append(d)
        j+=1
if(i==len(a) and j<len(b)):
    while(len(b)>j):
        resultado.append(b[j])
        j+=1
if(j==len(b) and i<len(a)):
    while (len(a) > i):
        resultado.append(a[i])
        i += 1
print(resultado)