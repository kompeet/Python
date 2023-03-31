def parts_sums(ls):
    sum_list = [sum(ls)]
    for i in ls:
        sum_list.append(sum_list[-1]-i)
    return sum_list


ls = [1,2,3,4,5]
print(parts_sums(ls))