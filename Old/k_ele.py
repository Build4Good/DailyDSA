from itertools import islice
nums = [1,1,1,2,2,3]
k = 2
count_dict={}
for num in nums:

    count_dict[num]=count_dict.get(num,0)+1

sorted_count_dic= dict(sorted(count_dict.items(),key=lambda item: item[1], reverse=True))

first_k_items = dict(islice(sorted_count_dic.items(), k))
print(list(first_k_items.keys()))
