#For loop
name = 'Abhi'
colors = ["Red", "Green", "Blue", "Yellow"]

for i in name:
    print(i, end=", ")
print("\n")

for x in colors:
    print(x)
print("\n")

#Ranged for loop
for k in range(4): #By default a ranged loop starts with 0. Prints 0 1 2 3
    print(k)

for k in range(4,6): # Prints 4 5
    print(k)

for k in range(4,8,2): #The 2 here gives the increment value to for loop, by default it is 1. Prints 4 6
    print(k)
print("\n")


#While loop
i = int(input("Enter any number: "))
count = 0
while(count<=5):
  print(i)
  count = count+1
print("Done with the loop")

#Do while loop
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if number < 0:
    print(number, "is not a positive number")
    break