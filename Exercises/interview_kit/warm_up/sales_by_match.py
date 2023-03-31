def sockMerchant(n, ar):
    srt = set(ar)
    result = 0
    for num in srt:
       result += ar.count(num)//2
    return result



ar = [1,2,3,2,1,2,3,2]




