List1 = []  
List2 = [1, 2, 3, 4, 5, 6]  
n = int(input("Enter number of elements : "))

for i in range(0, n): 
    item = int(input("Enter Item in list :"))
    List1.append(item) 
for k in List2: 
    if k in List1:  
        ans = "Equal"
    else:
        ans = "Not Equal"

print(ans)
