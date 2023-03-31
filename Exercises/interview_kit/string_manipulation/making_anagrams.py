def make_anagram(a, b):
    delete_sum = 0
    dict_str = {}
    for i in a:
        dict_str[i] = dict_str.get(i, 0) + 1
    for j in b:
        if dict_str.get(j, 0) != 0:
            dict_str[j] -= 1
        else:
            delete_sum += 1
    return delete_sum + sum(dict_str.values())

a = "cdeasdf"
b = "abcgdfgdrkjh"
print(make_anagram(a, b))