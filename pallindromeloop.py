def Palindrome(checkWord): 
    for i in range(0, int(len(checkWord) / 2)):  
        if checkWord[i] != checkWord[len(checkWord) - i - 1]:  
            return False
    return True


word = "maam" 
result = Palindrome(word)

if result:
    print("Palindrome")
else:
    print("Not Palindrome")
