import operator  
from functools import reduce 
from itertools import accumulate 


def sumOfList(a, b):
    sum = a + b  
    return sum


List = [1, 2, 3, 4, 5, 6]
a = (reduce(sumOfList, List))  
print(a)

b = list(accumulate(List, operator.add)) 
print(b)
