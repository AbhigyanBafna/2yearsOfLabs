# Basics 1

1. A **print()** statement has 4 main points -
	1. Its Objects (Integers, Strings etc)
	2. Separator (Custom input between objects)
	3. End (Custom end of a print statement)
	4. file: An object with a write method. <br>
	Ex - `print(5, "Abhi", 10 , sep=" Sep ", end= " End ")`
	
2. **Comments** are an essential part to make code more understandable, here is how you comment in Python - 

	```python
	#This is a single line comment.
	
	""" This is a 
	multiline comment. """
	```

4. **Escape Sequence Characters** are used to insert characters that cannot be directly used in a string.

	Ex -
	`print("These are double quotes - \" and \n I just wrote in new line.")`
	( \n and \\" are the ESC)
	
5. **Variables** are like containers that store data in memory. They must start with a letter/underscore, can only contain alpha-numeric characters and are case-sensitive.
	
	Ex -
	 `cont1 = 1231; print(cont1)`
	 
6. **Data type** specifies the type of value a variable holds. Data types vary according to the language. In Python they are (Default) -

	| Numeric   | Text   | Boolean  | Sequenced | Mapped |
	| --------- | ------ | ---------| --------- | ------ | 
	| int       | String | True     | List      | dict   |
	| float     |        | False    | Tuple     | 
	| complex   |        |          |           | 
	
	```
	int: 3, -8, 0
	
	float: 7.349, -9.0, 0.0000001
	
	complex: 6 + 2i
	
	string: "Hello World!"
	
	boolean: true / false
	
	list: [8, 2.3, [-4, 5], ["apple", "banana"]] {mutable}
	
	tuple: (("parrot", "sparrow"), ("Lion", "Tiger")) {immutable}
	
	dict: {"name":"Sakshi", 
			"age":20, 
			"canVote":True}
	
	b = "1"
	print(type(b)) #The type() function gets the data type of specified variable.
	
	
	```

7. Programming languages use operators to perform various tasks. Python has a variety of **Arithmetic operators** used to perform calculations.

	| Operator  | Operation      | Example |
	| --------- | -------------- | ------- | 
	| +         | Addition       | 3 + 55  |
	| -         | Subtraction    | 3 - 55  | 
	| *         | Multiplication | 3 * 55  | 
	| /         | Division       | 3 / 55  | 
	| **        | Exponential    | 3 ** 55 | 
	| %         | Modulus        | 3 % 55  | 
	| //        | Floor Division | 3 // 55 |       

	Examples : [Calculator](https://github.com/AbhigyanBafna/brain2/tree/main/python/programs/calc.py)

8. **Typecasting** is the conversion of one data type into another data type. **User input** can be taken using the input() function. This returns a string value and hence if required we need to typecast them.  Python supports a wide variety of typecasting functions like 
 
	1. int()
	2. float()
	3. str()
	4. ord()
	5. hex()
	6. tuple()
	7. set()
	8. list()
	9. dict() and many more.

	There are two types of typecasting, explicit and implicit conversion. Ex -

	```python
	#Explicit Typecasting
	a = "400"
	b = "600"
	print(int(a) + int(b))
	
	
	#Implicit TypeCasting
	c = 1.9
	d = 8
	print(c + d)
	
	#User Input
	num1 = int(input())
	num2 = float(input())
	print(x + y)
	```
	
10. **Strings and its Methods.** There are a lot of ways we use to print strings. Also using the len() method we can get its length. Strings can also be sliced to print a custom part of the string. Let's look at examples -

	```python
	name = "Abhigyan"
	singleQsurname = 'Bafna'
	multilineString = ''' The Biggest Lie : 
	We will get regular with studies.
	The Biggest Truth : 
	The night before the exams decides who gets a KT. 
	'''
	
	#Strings are actually character arrays and hence we can print 
	indivdual characters
	print(name[0]) 
	print(name[1])
	print(name[2]
	
	#Printing each character using for loop.
	for character in apple:
	    print(character)
		
	
	favfruit = "Mango"
	mangoLength = len(favfruit)
	
	# String slicing
	print(favfruit[0:4])  # Prints characters from [0 to 4). (4 not included.)
	print(favfruit[:4])   # Prints everything upto 4).
	print(favfruit[0:-3]) # Interpreted as print(favfruit[0:len(favfruit) - 3]) a.k.a [0:2]
	print(favfruit[-4:-2]) #favfruit([1:3])
		
	```
	
	There are a ton of methods which can help us modify strings in all ways we can imagine. **Strings are immutable**. The way string methods work are by creating a new mordified string using the previous string.
	
	Examples : [stringMethods.py](https://github.com/AbhigyanBafna/brain2/tree/main/python/programs/stringMethods.py)
	
11. **If-else** statements are blocks of code which execute according to conditions. If the condition is true then if block is executed. If not, the else block is executed. Elif statements are simply more if statements for an if-else 	conditional. All of this works on **conditional operators** -

	| Operator  | Operation      | Example | Evaluation |
	| --------- | -------------- | ------- | ---------- |
	| >         | Less than      | 3 > 55  | (False)    |
	| <         | Greater than   | 3 < 55  | (True)     |
	| >=        | Less/Equal     | 3 >= 55 | (False)    |
	| <=        | Greater/Equal  | 3 <= 55 | (True)     | 
	| ==        | Equal to       | 3 == 55 | (False)    |
	| !=        | Not equal to   | 3 != 55 | (True)     |

	If-else conditionals can be broken down into 3 types -
	1. if-else.
	2. if-elif-else.
	3. nested if-elif-else.

	Examples : [elif.py](https://github.com/AbhigyanBafna/brain2/tree/main/python/programs/elif.py)
	> Note '=' is used for assigning values and '==' is used to evaluation.
	
12. **Match Case** statement takes the value of a given variable and tries to match it with different values(pattern) until it matches one which then executes that particular block of code. Ex -

	```python
	x = int(input("Enter the value of x: ")) # x is the variable to match
	
	match x:
    case 0:
        print("x is zero") # if x = 0 this will print
        
    case 4:
        print("case is 4") # if x = 4 this will print

    case _: 
        print("no match") # _ marks a default case (A case when nothing matches).
        
    case _ if x!=80:
        print(x, "is not 80") # we can also add if conditionals to cases.
	```
	
11. **Loops** check for certain conditions and then execute a group of statements certain number of times. The are three types of loops -
	1. **for loop** - These are mainly used when the number of iterations are known. To iterate specific number of times range() is used.
	2. **while loop** - Used when iterations are unknown
	3. **do-while loop** - Executes the statements once without any checks and then acts like a while loop.
	
	Examples : [loops.py](https://github.com/AbhigyanBafna/brain2/tree/main/python/programs/loops.py)
	
	**Break** terminates the loop entirely, hence skipping all further iterations of the loop while the **Continue** statement only skips the current iteration and moves to the next iteration. Ex -

	```
	#Prints Table of 5 but only skips 5x10.
	for i in range(13):
	if(i == 10):
	print("Skip the iteration") 
	continue
	print("5 X", i, "=", 5 * i)
	  	
	#Breaks when counter reaches 50
	i = 0
while True:
  print(i)
  i = i + 1
  if(i%51 == 0):
    break
  	```
  	
> Remember : In Python everything is an object

<br>
