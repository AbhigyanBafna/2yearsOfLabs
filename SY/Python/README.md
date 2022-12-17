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
	
2. Comments are an essential part to make code more understandable, here is how you comment in Python - 

	```python
	#This is a single line comment.
	
	""" This is a 
	multiline comment. """
	```

3. If-else statements are blocks of code which execute according to the specified condition.

	```python
	p = 7 
	
	if (p > 5):
	    print("p is greater than 5.") #Condition is true hence this will execute.
	else:
	    print("p is not greater than 5.")
	```

4. Escape Sequence Characters are used to insert characters that cannot be directly used in a string. Ex - \n, \"

	Ex - `print("These are double quotes - \" and \n I just wrote in new line.")`
