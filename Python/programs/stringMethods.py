a = "abhigyan ~~~Bafna ~~~"

print(a.upper())
print(a.lower())
print(a.rstrip("~"))
print(a.replace("Abhigyan", "Abhi"))
print(a.split(" "))
print(a.capitalize())
print(a.center(50,"."))
print(a.count("abhi"))
print(a.endswith("!!!"))
print(a.endswith("n", 4, 8)) #Slices the string to [4,8) a.k.a 'gyan' and then checks if it ends with 'o'.
print(a.startswith("ab"))


str1 = "Hello World 11"
print(str1.find("Wor")) # finds and returns first occurance index, or else returns -1
print(str1.isalnum()) # True only if entire string consists of alphabets or numbers.
print(str1.isalpha()) #True if alphabets
print(str1.islower())
print(str1.isupper())
print(str1.isprintable())
print(str1.isspace())
print(str1.istitle()) #Each word needs to be capitalized
print(str1.swapcase())
print(str1.title())