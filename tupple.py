Tuple = ("First index", 1, 2, 3, "aiads", True, False, "Last index")
print("Length of tuple", len(Tuple))  
print("Backward indexing : ", Tuple[-1])  
print("Forward indexing : ", Tuple[0]) 
print("Slicing in tuple using forward indexing", Tuple[0:2]) 
print("Printing tuple", Tuple)  

New_Tuple = (1, 2, 3, 4)  
List = [New_Tuple, 1, 2, 34] 
print("nested tuple in list:", List) 
List1 = list(New_Tuple)
print("Changing tuple into list", List1) 
List1[1] = "aiads"  
print("After changing value : ", List1)
List1.append("New element")
New_Tuple = tuple(List1)
print("After appending in tuple : ", New_Tuple)
