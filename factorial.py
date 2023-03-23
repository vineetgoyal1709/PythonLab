def factorial(num): 
    if num == 0: 
        return 1
    else:  
        fact = 1
        while num > 0:
            fact *= num
            num -= 1
        return fact

number = int(input("Enter the number : "))
print("factorial of the number is :", factorial(number))
