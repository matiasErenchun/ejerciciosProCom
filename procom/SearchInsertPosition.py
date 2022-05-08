
##wip()
nums = [1]
target = 1
#olvide como implementar esta wea XDXDXD
inferior=0
superior = len(nums)-1
index = int(superior/2)
continuar = True
while continuar:
    print("inferior: ", inferior, " superior:", superior, " index:", index)
    if(nums[index]==target):
        continuar=False
    elif(nums[inferior]==target):
        index = inferior
        continuar=False
    elif(nums[superior]==target):
        index = superior
        continuar = False
    elif(nums[index]>target):
        superior=index
        index=int((inferior+superior)/2)
    elif(nums[index]<target):
        inferior = index
        index = int((inferior + superior) / 2)
    if(index==inferior or index==superior):
        continuar=False
        if(nums[inferior]<target and nums[superior]>target):
            index=superior
        elif(nums[inferior]>target):
            index=inferior
        elif(nums[superior]<target):
            index=superior+1
print(index)