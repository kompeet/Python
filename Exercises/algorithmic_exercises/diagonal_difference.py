def diagonalDifference(arr):
    count = 0
    for i in range(len(arr)):
        count += arr[i][i] - arr[i][-1-i]
    return abs(count)
