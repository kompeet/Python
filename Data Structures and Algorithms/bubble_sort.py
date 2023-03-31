def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]


# Test case
test = [3, 6, 7, 4, 3, 2, 4, 45, 3, 5, 6, 7, 7, 54, 5, 45, 46, 3]
bubble_sort(test)
print(test)
