def linear_search(input_list, target):
    for i in range(len(input_list)):
        if input_list[i] == target:
            return i
    return None


# Test cases
test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(linear_search(test, 5))
