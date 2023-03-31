def hourglass_sum(arr):
    all_sum = []
    hg_sum = 0
    for i in range(4):
        for j in range(4):
            sum_first = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            sum_second = arr[i+1][j+1]
            sum_third = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hg_sum = sum_first + sum_second + sum_third
            all_sum.append(hg_sum)
    print(all_sum)
    return max(all_sum)