def binary_array_to_number(arr):
    count = 0
    num = 1
    for i in arr[::-1]:
        count += i*num
        num *= 2
    return count

arr = [0,1,1,1]
print(binary_array_to_number(arr))