from collections import defaultdict
tg_dict=defaultdict(list)
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

for s in strs:
  
    word_key="".join(sorted(s))
    if word_key in tg_dict:
        tg_dict[word_key].append(s)
    else:
        tg_dict[word_key]=[s]
print(tg_dict.values())        
