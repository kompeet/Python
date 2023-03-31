def binary_search(input_list, value):
    low = 0
    high = len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if input_list[mid] == value:
            return mid
        elif input_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Test cases
test = [1, 3, 9, 11, 15, 19, 29, 30]
test_val1 = 25
test_val2 = 15
print(binary_search(test, test_val1))
print(binary_search(test, test_val2))
