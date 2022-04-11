#falla por tiempo preguntar a daniel
a =[7,6,4,3,1]
profit=0
i=0
while(i<len(a)):
    diaCompra=a[i]
    diaVenta=i+1
    while(diaVenta<len(a)):
        if(diaCompra<a[diaVenta]):
            if(profit<(a[diaVenta]-diaCompra)):
                profit=a[diaVenta]-diaCompra
        diaVenta+=1
    i+=1
print(profit)
