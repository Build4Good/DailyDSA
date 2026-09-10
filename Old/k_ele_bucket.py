
nums = [1,1,1,2,2,3]
k = 2
count_dict={}
freq = [[] for i in range(len(nums) + 1)]
for num in nums:

    count_dict[num]=count_dict.get(num,0)+1

for n, c in count_dict.items():
    freq[c].append(n)


print(freq)
res=[]

for i in range(len(freq)-1,0,-1):
    
    for n in freq[i]:
       
        res.append(n)
        
        if len(res) == k:
            break
    if len(res) == k:
        break

print(res)            