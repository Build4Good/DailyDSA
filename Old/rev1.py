nums = [2, 7, 11, 15]
target = 9
trg_dict={}

for idx, num in enumerate(nums):
    complement = target - num
    if complement in trg_dict:
        print(f"[{trg_dict[complement]},{idx}]")
        break

    else:
        trg_dict[num]=idx    

            