# Python

1. Python is a high-level dynamically typed programming language.
2. It was designed by Guido van Rossum in 1991.
3. It is majorly used in -
	1. Web and software development. <br>
	2. AI and Data Science
	3. Scripting.

## Why Python tho?

1. Python has a simple syntax allowing to write programs with fewer lines.
2. It runs on an interpreter system, meaning that code can be executed as soon as it is written. Making prototyping very quick.
3. Python relies on using whitespaces for various purposes which enhances readability compared to programming languages which often use something like curly-braces { }.

## Index
1. Modules and Package Managers
2. Basics 1
3. Basics 2

## Modules and Package Managers

Modules are like code-books stored in a huge code libraryis like a code library. It helps us save time by importing code written by somebody else. There are two types of modules in python -

1. Built in Modules - These modules ship with the python interpreter and can directly be imported
2. External Modules - These modules need to be imported from a third party or a package manager like pip or conda.

Ex - `pip install pandas` (module name = pandas).

## Basics 1

Python works with an interpreter and executing code line by line can get very slow. To overcome this we use a script file with the .py extension which executes all the code in one go.

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

3. **If-else** statements are blocks of code which execute according to conditions. If the condition is true then if block is executed, if not, the else block is executed.

	```python
	p = 7 
	
	if (p > 5):
	    print("p is greater than 5.") #Condition is true hence this will execute.
	else:
	    print("p is not greater than 5.")
	```

4. **Escape Sequence Characters** are used to insert characters that cannot be directly used in a string.

	Ex -
	`print("These are double quotes - \" and \n I just wrote in new line.")`
	( \n and \\" are the ESC)
	
5. **Variables** are like containers that store data in memory. 
	
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

7. Programming languages use operators to perform various tasks. Python has a variety of **arithmetic operators** used to perform calculations.

	| Operator  | Operation      | Example |
	| --------- | -------------- | ------- | 
	| +         | Addition       | 3 + 55  |
	| -         | Subtraction    | 3 - 55  | 
	| *         | Multiplication | 3 * 55  | 
	| /         | Division       | 3 / 55  | 
	| **        | Exponential    | 3 ** 55 | 
	| %         | Modulus        | 3 % 55  | 
	| //        | Floor Division | 3 // 55 |       

	[calculatorV1.py]()

8. Typecasting is the conversion of one data type into another data type. Python supports a wide variety of typecasting functions like 
 
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
	```
	
9. **User input** can be taken using the input() function. This returns a string value and hence if required we need to typecast them.

	Ex - 
	
	```python
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
	Examples in - [stringMethods.py]()
	
11. **Conditional Operators and elif** Elif statements are simply more if statements for an if-else conditional. If-else statements work on conditional operators which are - 

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

	Examples : elif.py
	
12.
	
> Note : '=' is used for assigning values and == is used to evaluation.
	
	
> Remember : In Python everything is an object


	
