def func1(list_a):
    list_a[0] = 77
    
    return list_a



a1 = [1, 2,3]
asdf = func1(a1[:])
a3 = a1[:]
print(asdf)
