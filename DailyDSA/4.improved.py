def product_except_self_optimized(nums: list[int]) -> list[int]:
    output=[1]*len(nums)
    left_product=1
    right_product=1

    for i in range(len(nums)):
        output[i]=left_product
        left_product = nums[i]*left_product

    for i in range(len(nums)-1,-1,-1):
        output[i]=output[i]*right_product
        right_product=right_product*nums[i]

    return output    

  


print(product_except_self_optimized([1, 2, 3, 4]))