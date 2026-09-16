list_test=[-1,2,0,1,2,3,-1,-2,5,0]


def tsum(nums:list[int]):
    list_triplets=[]
    nums.sort()
    for i,val in enumerate(nums):

        if i>0 and nums[i]==nums[i-1]:
            continue
        l=i+1
        r=len(nums)-1

        while l<r:
            s=nums[i]+nums[l]+nums[r]

            if s==0:
                list_triplets.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r+1]:
                    r-=1 
            elif s>0:
                r-=1
            else:
                l+=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
    return list_triplets    

print(tsum(list_test))            
