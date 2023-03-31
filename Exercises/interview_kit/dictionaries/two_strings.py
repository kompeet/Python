def two_strings(s1, s2):
    letters = {}
    output = 'NO'
    for i in s1:
        letters[i] = letters.get(i, 0) + 1
    for j in s2:
        # if j in letters:
        if letters.get(j, 0) != 0:
            output = 'YES'
            break
    return output

a = "ADSFSAF"
b = "Z"
print(two_strings(a, b))