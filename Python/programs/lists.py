marks = [10, 20, 536, "Abhi", True]
print(marks[0]) #List indexing starts from 0
print(marks[-3]) #Like strings lists also support negative index (len(marks)-3) = 2.
print(marks[1:]) #Goes on till end of list.
print(marks[1:4:2]) #Slices list to 1:4 and then selects according to jump '2'.

if "Abhi" in marks: #This works for strings as well.
	print("Yes")
	
#List Comprehension.
lst = [i*i for i in range(10) if i%2 == 0]
print(lst) #Square of even numbers till 10.

names = ["Daze", "Shia", "Aadi", "Nik"]
namesWithA = [item for item in names if "a" in item]
print(namesWithA)

#List Methods
l = [11, 12, 142, 0]
l.append(0) #Appends 0 to end of list
l.sort() #Sorts in ascending. l.sort(reverse=True) for desc.)
l.reverse()
print(l.index(0)) #Prints the index of the first 0 found in l.
print(l.count(0)) #Prints the count of 0's in l.
m = l.copy() #Creates a new list m and copies l to it.
l.insert(2,69) #Inserts 69 at 2nd Index.
m = [900, 800, 55]
k = l + m #Concatenates l and m in k.
l.extend(m) #Extends m by adding l to it.
print(l)
