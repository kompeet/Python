numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"

def highest_lowest(numbers):
    numbers = numbers.split(' ')
    numbers = sorted(numbers, key=int)
    return numbers[-1] +" "+ numbers[0]


print(highest_lowest(numbers))
