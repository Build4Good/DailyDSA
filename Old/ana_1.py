strs = ["eat","tea","tan","ate","nat","bat"]
default_dict={}


for x in strs:

    word_key="".join(sorted(x))
    print(x)
    if word_key in default_dict:
        default_dict[word_key].append(x)
    else:
        default_dict[word_key]= [x]


print(default_dict.values())