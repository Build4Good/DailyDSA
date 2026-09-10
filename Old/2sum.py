nums =[3, 2, 4]
target = 6

val_index_map={}

for idx,val in enumerate(nums):
    complement=target-val
    if complement in val_index_map:
        print(f"[{val_index_map[complement]},{idx}]")
        break
    else:
        val_index_map[val]=idx    

