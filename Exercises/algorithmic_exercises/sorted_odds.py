def sorted_odds(lst):
    sorted_odds = []
    new_lst = []
    for i in lst:
        if i % 2 != 0:
            sorted_odds.append(i)
    sorted_odds = sorted(sorted_odds)

    for i in lst:
        if i % 2 != 0:
            new_lst.append(sorted_odds.pop(0))
        else:
            new_lst.append(i)
    return new_lst


lst = [3,4,1,11,9,2,6]
print(sorted_odds(lst))
