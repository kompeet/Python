def is_palindrome(x):
    given_number = x
    reverse_number = 0
    while given_number > 0:
        last_digit = given_number % 10
        reverse_number = (reverse_number * 10) + last_digit
        given_number = (given_number // 10)

    return x == reverse_number

x = 121
print(is_palindrome(x))
