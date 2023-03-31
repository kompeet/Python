def two_strings(s1, s2):
    letters = {}
    check = "NO"
    for i in s1:
        letters[i] = letters.get(i,0) + 1
    for j in s2:
        if letters.get(j,0) != 0:
            check = "YES"
            break
    return check

s1 = "AAA"
s2 = "BBBA"
print(two_strings(s1, s2))