def hourg_glass_sum(arr):
    all_sum = []
    hourglass_sum = 0
    for i in range(4):
        for j in range(4):
            fist_row = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            second_row = arr[i+1][j+1]
            third_row = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglass_sum = fist_row + second_row + third_row
            all_sum.append(hourglass_sum)
    return max(all_sum)


