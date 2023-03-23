def palindrome(string):  
    if string == string[::-1]:  
        print("The given string is palindrome")
    else:
        print("The given string is not palindrome")
input_string = input("Enter the String : ") 
palindrome(input_string)
