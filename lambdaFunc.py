x = lambda a: a + 10 
print("Adding 10 to a : ", x(5))

x = lambda a, b: a * b
print("Multiplying two numbers", x(4, 5))  
def double(n):  
    return lambda a: a * n 
func = double(2)  
print(func(4))  
