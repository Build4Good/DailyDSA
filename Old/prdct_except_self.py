nums = [-1,1,0,-3,3]

prd=[1 for x in nums]
mul=1

for i in range(1,len(nums)):
    mul*=nums[i-1]
    prd[i]=mul

print(prd)
suffix=1

for i in range(len(nums)-1,-1,-1):
    prd[i]=prd[i]*suffix
    suffix=nums[i]*suffix
    print(suffix)

print(prd)    
