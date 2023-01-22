
#WAP to print a star pattern.

n = int(input("Please enter a number:"))

for i in range(0,n):
    for j in range(i):
        print("*",end=" ")
    print("")
    
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("")
   
#WAP to accept name and surname in two variables and print them in reverse.

name = input("Please enter your name:")
sname = input("Please enter your surname:")

for i in range(len(sname)-1,-1,-1):
    print(sname[i],end=" ")

for i in range(len(name)-1,-1,-1):
    print(name[i],end=" ")

   
    