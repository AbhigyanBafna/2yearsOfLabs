'''
Write a python program to create a list where the number of elements 
are taken from the user. Further add even numbers from list and odd 
numbers from list. These two numbers should be displayed as tuples.
'''

n = int(input("Enter number of elements:"))
list1 = []
even = 0
odd = 0
for i in range(n):
	a = int(input("Enter element :"))
	list1.append(a)
print(list1)

for i in range(n):
    if(list1[i]%2==0):
        even += list1[i]
    else:
        odd += list1[i]

evOdd = (even,odd)
print(evOdd)

'''
Given the list list 1 = [x,y,z]
Write a list comprehension to produce the following list -

A) [x,xx,xxx,y,yy,yyy,z,zz,zzz]
B) [x,y,z,xx,yy,zz,xxx,yyy,zzz]
'''

list1 = ['x','y','z']
list2 = [lst1*num for lst1 in list1 for num in range(1,4)]
print(list2)

list3 = [lst1*num for num in range(1,4) for lst1 in list1]
print(list3)
        
        
    
    
    




