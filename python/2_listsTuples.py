#Various basic problems on lists, list comprehension and tuples.

'''
Q1) Write a python program to create a list where the number of elements 
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
Q2) Given the list list 1 = [x,y,z]
Write a list comprehension to produce the following list -

A) [x,xx,xxx,y,yy,yyy,z,zz,zzz]
B) [x,y,z,xx,yy,zz,xxx,yyy,zzz]
'''

list1 = ['x','y','z']
list2 = [lst1*num for lst1 in list1 for num in range(1,4)]
print(list2)

list3 = [lst1*num for num in range(1,4) for lst1 in list1]
print(list3)



'''
Q3) Given a tuple of elements, write a python program to create 
a dictionary with tuple elements as a key and its count in 
tuple as value e.g t = (4,5,6,2,3,4,5,1,2,6,4) then output 
should be d = {4:3,5:2,2:2,3:1,1:1}
'''

t = (4,5,6,2,3,4,5,1,2,6,4)
keys = []
values = []
d1 = {}
for i in t:
    if i not in keys:
        keys.append(i)
        
for j in keys:
    n = t.count(j)
    values.append(n)

for i in range(len(keys)):
    d1[keys[i]] = values[i]
print(d1)

'''
Q4) Write a python program to print tuple of website suffixes 
from given dictionary 
{ 1:"www.yahoo.com",
  2:"www.tsec.edu",    
  3:"www.asp.net",
  4:"www.abcd.in"}
'''

d2 = {
  1:"www.yahoo.com",
  2:"www.tsec.edu",    
  3:"www.asp.net",
  4:"www.abcd.in"}

suffixes = []

for url in d2.values():
    suffix = url.split(".")[-1]
    suffixes.append(suffix)
print(tuple(suffixes))


    

    

    




