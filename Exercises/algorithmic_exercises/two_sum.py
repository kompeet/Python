def two_sum(nums, target):
    for i in range(len(nums)):
        x = target - nums[i]
        if x in nums and nums.index(x) != i:
            return [i, nums.index(x)]

a = [2,7,11,15]
b = 9
print(two_sum(a,b))
