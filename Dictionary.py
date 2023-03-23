Dictionary = {
    "Key": "Value",
    1: "Hello",
    2: "Welcome",
}
print("Dictionary-", Dictionary) 
Dictionary[1] = "Value Changed"
print("After changing value:", Dictionary)
Dictionary["New Key"] = "New Value"  
print("After adding new key", Dictionary)
Dictionary.pop("New Key")   
print("Removing items", Dictionary)
New_Dictionary = {1: True, 2: False} 
Dictionary["New Dictionary"] = New_Dictionary  
print("Nested Dictionary", Dictionary)
Dictionary.update({1: "value updated"})  
print("updated value: ", Dictionary)
