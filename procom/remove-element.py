nums = [0,1,2,2,3,0,4,2]
val = 2
i=0
count=0
j=len(nums)-1
while(i<len(nums)):
    print("hola", i, j)
    if(nums[i]==val):
        nums[i]=nums[j]
        nums[j]='_'
        j-=1
        count+=1
    else:
        i+=1
print(nums, len(nums)-count )
