nums = [0,0,1,1,1,2,2,3,3,4]
i=0
eliminados=0
while i<len(nums) and i+eliminados<len(nums):
    j=i+1
    if(j<len(nums)):
        while nums[i]==nums[j]:
            nums.pop(j)
            nums.append('_')
            eliminados+=1
    i+=1
print(len(nums)-eliminados)
