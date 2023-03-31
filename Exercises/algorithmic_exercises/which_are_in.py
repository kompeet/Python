def in_array(array1, array2):
    lst = []
    for i in array1:
        for j in array2:
            if i in j:
                lst.append(i)
    return sorted(set(lst))
    # return sorted(set([word for word in array1 for word_2 in array2 if word in word_2]))

a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))