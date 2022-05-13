nums = [0,1,0,3,12]
i=0
ceros=0
while i<len(nums) and i+ceros<len(nums):
    if(nums[i]==0):
        num=nums.pop(i)
        nums.append(num)
        ceros+=1
    else:
        i+=1
print(nums)