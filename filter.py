def fun(i):
    if i % 2 == 0:
        return i
    else:
        return False


List = [1, 2, 3, 4, 5, 6]
a = filter(fun, List) 
for i in a:
    print(i)
