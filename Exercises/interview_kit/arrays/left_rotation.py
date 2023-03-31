def rot_left(a, d):
    x = a[d:] + a[:d]
    return x

a = [1,2,3,4,5,6,7,8,9]
b = 4
print(rot_left(a,b))