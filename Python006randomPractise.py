string = "the Quick brown fox jumps over the laZy dog"
print(string.capitalize())


print("\n"*3)

# to capitalize every word in the string

print("____method 1____")
str = string.capitalize()
for i in range(len(str)):
    if str[i] == " ":
        str = str[:i+1] + str[i+1].upper() + str[i+2:]
    print(str[i], end="")   
    
         
         
print("\n"*3)





print("____method 2____")
print(string.title())





print("\n"*3)





print("____method 3____")
words = string.split()
for word in words:
    print(word.capitalize(), end=" ")
    
    
    
    
print("\n"*3)
