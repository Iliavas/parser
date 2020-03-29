import numpy as np

def func(i):
    return round(float(i) * (42/10)**0.247)



a = open('a.txt', 'r')
b = a.read().split('\n')

arr = []
res = {}
for i in b:
    if len(i.split(' - ')) > 1:
        res.update({i.split(' - ')[0]: np.array([float(i.split(' - ')[1]), i.split(' - ')[2]])})
for i in res:
    arr.append(float(res.get(i)[0]))

arr1 = []
for i in arr:
    arr1.append(func(i))

