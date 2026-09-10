nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
res=[]
for i in range (0,len(nums)-1,1):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    target = -nums[i]
    l=i+1
    r=len(nums)-1

    while l<r:
        if nums[l]+nums[r]==target:
            triplet=[nums[i],nums[l],nums[r]]
            res.append(triplet)
            r-=1
            l+=1
        else:
            if (nums[l]+nums[r])>target:
                r-=1
            else:
                l+=1

print(res)



###Gemini Sol below ####
nums = [-1, 0, 1, 2, -1, -4]
nums.sort()  # Sorted: [-4, -1, -1, 0, 1, 2]
res = []

for i in range(len(nums)):
    # 1. Skip outer loop duplicates
    # If this is not the first number, and it's same as previous, skip.
    if i > 0 and nums[i] == nums[i-1]:
        continue

    # 2. Fix Left pointer to start AFTER i
    l = i + 1
    r = len(nums) - 1
    
    while l < r:
        total = nums[i] + nums[l] + nums[r]
        
        if total == 0:
            res.append([nums[i], nums[l], nums[r]])
            
            # 3. Move pointers inward after finding a match
            l += 1
            r -= 1
            
            # 4. Skip inner loop duplicates (The crucial step!)
            # While l is still valid AND value is same as previous, move it again
            while l < r and nums[l] == nums[l-1]:
                l += 1
                
        elif total > 0:
            r -= 1
        else:
            l += 1

print(res)