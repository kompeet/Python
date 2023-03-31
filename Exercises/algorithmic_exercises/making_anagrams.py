def make_anagram(a,b):
    letters = {}
    delete = 0
    for i in a:
        letters[i] = letters.get(i, 0) + 1
    for j in b:
        if letters.get(j, 0) != 0:
            letters[j] -= 1
        else:
            delete += 1
    return delete + sum(letters.values())

a = "abc"
b = "cbdf"
print(make_anagram(a,b))