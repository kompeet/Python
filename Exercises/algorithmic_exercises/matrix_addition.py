import numpy as np

def matrix_addition(a, b):
        # lst = []
        # for i in zip(a, b):
        #     lst.append([x+y for x, y in zip(i[0], i[1])])
        # return lst

        # return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]

        # return np.add(a, b).tolist()

        lst = []
        for i in range(len(a)):
              lst.append([x+y for x, y in zip(a[i],b[i])])
        return lst


arr1 = [ [1, 2, 3], [3, 2, 1], [1, 1, 1] ]
arr2 = [ [2, 2, 1], [3, 2, 3], [2, 2, 2] ]
print(matrix_addition(arr1, arr2))