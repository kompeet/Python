def find_uniq(arr):
    res = sorted(arr)
    if res[0] == res[1]:
        return res[-1]
    else:
        return res[0]

arr = [1,1,1,1,0.55,1,1,1]
print(find_uniq(arr))