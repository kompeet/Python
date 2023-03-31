def mini_max_sum(arr):
    sum_arr = sum(arr)
    sum_max = sum_arr - max(arr)
    sum_min = sum_arr - min(arr)
    print(sum_max, sum_min)


arr = [1,2,3,4,5]
mini_max_sum(arr)