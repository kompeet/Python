def quicksort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        pivot = input_list[0]
        less = [i for i in input_list[1:] if i <= pivot]
        greater = [i for i in input_list[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Test cases
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))