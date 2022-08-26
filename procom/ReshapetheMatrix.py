mat=[[1,2,3,4]]
newMat=[]
newlist=[]
r=2
c=2
if(r*c == len(mat)*len(mat[0])):
    i=0
    while i<len(mat):
        j=0
        while j<len(mat[i]):
            newlist.append(mat[i][j])
            print(newlist)
            if(len(newlist)==c):
                newMat.append(newlist)
                print(newMat)
                newlist=[]
            j+=1
        i+=1
else:
    newMat=mat
print(newMat)