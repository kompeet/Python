def gem_stones(arr):
    dct = {}
    for i in range(len(arr)):
        x = set(list(arr[i]))
        for j in x:
            dct[j] = dct.get(j, 0) + 1

    gem = 0
    for value in dct.values():
        if value == len(arr):
            gem += 1
    return gem

arr = ["aabc", "aabt", "aabx"]
print(gem_stones(arr))



