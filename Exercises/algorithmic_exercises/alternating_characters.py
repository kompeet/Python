def alternating_characters(s):
    num = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            num += 1
    return num

s = "AAABBB"
print(alternating_characters(s))