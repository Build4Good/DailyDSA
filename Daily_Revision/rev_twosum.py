"""Given an array of integers and a target, return
  the indices of the two numbers that add up to
  the target. Exactly one valid pair exists, and
  you can't use the same element twice."""


def two_sum(nums:list[int],target:int)->list[int]:
    dict_comp={}

    for i in range(len(nums)):
        complement=target-nums[i]
        if complement in dict_comp:
            return [dict_comp[complement],i]
        else:
            dict_comp[nums[i]]=i


print(two_sum([2, 7, 11, 15], 9))   
print(two_sum([3, 2, 4], 6))    
print(two_sum([-1, -2, -3, -4, -5], -8))             