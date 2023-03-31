def plus_minus(arr):
    count_pos = 0
    count_zero = 0
    count_neg = 0
    for i in arr:
        if i > 0:
            count_pos += 1
        elif i == 0:
            count_zero += 1
        else:
            count_neg += 1
    print("{:.6f}".format(count_pos/len(arr)))
    print("{:.6f}".format(count_zero/len(arr)))
    print("{:.6f}".format(count_neg/len(arr)))

arr = [1,1,0,-1,-1]
plus_minus(arr)
