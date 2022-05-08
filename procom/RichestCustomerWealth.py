a = [[2,8,7],[7,1,3],[1,9,5]]
max=0
for i in a:
    subTotal=0
    for j in i:
        subTotal+=j
    if subTotal>max:
        max=subTotal
print(max)