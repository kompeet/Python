def maximum_toys(prices, k):
    prices = sorted(prices)
    present_num = []
    for i in prices:
        if sum(present_num) + i < k:
            present_num.append(i)
    return len(present_num)

prices = [3000,200,500,1300,1000,3000]
k = 8000
print(maximum_toys(prices, k))