def uniq_order(lst):
    new_lst = []
    char = 0
    for i in range(len(lst)):
        if lst[i] != char:
            new_lst.append(lst[i])
        char = lst[i]
    return new_lst


lst = "AAbbCCXXyy"
print(uniq_order(lst))