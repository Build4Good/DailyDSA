nums = [100, 4, 200, 1, 3, 2]

set_num=set(nums)
print(set_num)
seq_start=""
i=0
longest_len=0
while i < len(nums):
    seq_start=nums[i]
    if (seq_start-1) in set_num:

        i+=1
    else:
        max_length=1
        numb=seq_start+1
        while numb in set_num:
            max_length+=1
            numb+=1
        if max_length>longest_len:
            longest_len=max_length
        i+=1    

print(longest_len)




nums = [100, 4, 200, 1, 3, 2]
set_num = set(nums)
longest_len = 0

# Iterate directly over the set (removes duplicates automatically)
for num in set_num:
    # Check if 'num' is the start of a sequence
    if (num - 1) not in set_num:
        current_num = num
        current_len = 1
        
        # Count consecutive numbers
        while (current_num + 1) in set_num:
            current_num += 1
            current_len += 1
            
        longest_len = max(longest_len, current_len)

print(longest_len)
