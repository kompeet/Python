def high(x):
    char_arr = x.split()
    dc = {}
    for i in char_arr:
        points = 0
        for char in i:
            points += ord(char)-96
        dc[i] = dc.get(i, 0) + points
    top = max(dc, key=dc.get)
    return top


test1 = 'what time are we climbing up the volcano'
test2 = 'aa b'
print(high(test1))