def compare_triplets(a, b):
    alice = list(a)
    bob = list(b)
    a_points = 0
    b_points = 0
    result = []

    for i in range(len(alice)):
        if alice[i] > bob[i]:
            a_points += 1
    for j in range(len(bob)):
        if alice[j] < bob[j]:
            b_points += 1
    result.append(a_points)
    result.append(b_points)
    return result

a = [2,2,2]
b = [1,1,1]
print(compare_triplets(a, b))