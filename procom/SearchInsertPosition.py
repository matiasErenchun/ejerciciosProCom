
##wip()
nums = [1,3,5,6,7,8,9,10,11,33,44,66,77]
target = 5
#olvide como implementar esta wea XDXDXD
inferior=0
superior = len(nums)-1
index = int(superior/2)
i=0
continuar = True
while continuar:
    if(nums[index]==target):
        continuar = False
    elif(nums[index]>=target):
        if (nums[index] == target):
            print("dawn", index)
            continuar = False
        else:
            superior = index
            index = int((inferior + superior)/2)
    elif(nums[index]<=target):
        if (nums[index] == target):
            print("upp", index)
            continuar = False
        else:
            inferior = index
            index = int((inferior + superior) / 2)
    print("inferior: ", inferior,"superior: ",superior)
    if(i==4):
        continuar=False
    i+=1

print(index)