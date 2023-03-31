def solution(number):
    result = 0
    for i in range(1, number):
        if i > 0 and (i % 3 == 0 or i % 5 == 0):
            result += i
        elif i < 0:
            result += 0
    return result

number = 6
print(solution(number))