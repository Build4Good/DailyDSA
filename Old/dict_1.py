def is_anagram(s,t):
    if len(s)!=len(t):
        return False
    
    count_map={}
    
    for char in s:
        count_map[char]=count_map.get(char,0)+1

    for char in t:

        if char not in count_map:
            return False

        count_map[char]-=1

        if count_map[char]==0:
            del count_map[char]   
    
    return(len(count_map)==0)        

print(is_anagram(s = "anagram", t = "naaaram"))