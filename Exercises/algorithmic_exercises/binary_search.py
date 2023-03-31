def search(nums,target):
    result = -1
    for i in nums:
        if i == target:
            result = nums.index(i)
    return result

nums = [-3,-1,0,2,3,4,5,6]
target = 5
print(search(nums,target))