nums = [1, 2, 3, 4]
mul=1
prd_lst=[1 for x in (nums)]

for i in range(1,len(nums),1):
    mul*=nums[i-1]
    prd_lst[i]=mul

print(prd_lst)

suffix=1

for i in range(len(nums)-1,-1,-1):
    prd_lst[i]*=suffix
    suffix*=nums[i]

print(prd_lst)    
