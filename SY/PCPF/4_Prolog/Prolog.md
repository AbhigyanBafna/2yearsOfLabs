# Prolog

<b> Introduction </b>
1. Prolog is a logic programming language. It has important role in AI. It is intended primarily as a declarative programming 
language.
2. Declarative programming is when you write your code in such a way that it describes what you want to do, not how you want 
to do it. It is left up to the compiler to figure out the how. Ex- Prolog, SQL.
3. In prolog, logic is expressed as relations (called as Facts and Rules) in a knowledge base. Knowledge bases has a .pl file extension.
4. Core heart of prolog lies at the logic being applied which is carried out by running a query over these relations.
<br>

<b> Knowledge Base Syntax </b>
```prolog
loves(romeo,juliet).                          /* This is how a fact is written. Fact - Romeo loves Juilet */
happy(albert). happy(alice).                    
with_albert(alice).
male(bob). male(carl). male(albert).
parent(albert, bob). parent(alice, bob).
parent(bob, carl). parent(bob, charlie).
brother(bob, bill).                           /* End of facts for the code 👇🏻 */



loves(juliet,romeo). :- loves(romeo,juliet). 


/* 👆🏻 An if(:-) statement trying to say - " If Romeo loves Juilet then Juilet loves Romeo " where juilet, romeo
are subjects (the whom part of the sentance) while loves is the predicate (something about the subject). */


does_alice_dance :- dances(alice) ,                           
  write('When Alice is happy and with Albert she dances'). 
  
  
/* Typing does_alice_dance. in the terminal will write that statement because 
dances(alice) is true. (,) represents AND */

                                              
get_grandchild :- parent(albert, X), parent(X, Y),            
              write('Alberts grandchild is '),                
              write(Y), nl.
              
/* Typing get_grandchild. in the terminal will write that statement after finding Y = carl and Y = charlie from
the facts. nl prints new line */
              
what_grade(5) :-
  write('Go to kindergarten').
what_grade(6) :-
  write('Go to first grade').
what_grade(Other) :-
  Grade is Other - 5,
  format('Go to grade ~w', [Grade]).        /* A nested if Example*/
  
/* MATHS*/
  
X is 2 + 2.                                 /* 'is' is used as = to assign values to Variables */
X is mod(7,2).                              /* X = 1 (Modulus) */
random(0,10,X).                             /* Assigns X a random value from 0-10 */
between(0,10,X).                            /* Get all values between 0 and 10 */
X is abs(-8).                               /* Get absolute value of -8 */
X is max(10,5).                             /* Get largest value */
X is round(10.56).                          /* Round a value */
X is truncate(10.56).                       /* Convert float to integer */
X is 2** 3.                                 /* 2^3 */

     
/* Read Write Operations in Prolog */

say_hi :-                                   
  write('What is your name? '),
  read(X),
  write('Hi '),
  write(X).
  
  
/* Looping in Prolog */

count_to_10(10) :- write(10), nl. /* Loop Terminator */
 
count_to_10(X) :-                 /* The Loop */
  write(X),nl,
  Y is X + 1,
  count_to_10(Y).

```

<b> Queries Syntax </b>
```
change_directory('/Users/abhi/Desktop/Prolog_Practice').

[knowledgeBase]. /* Loads the knowledge base in your current directory */

listing(male). /* Will list everyone who's a male */

male(_).      /* _ is an anonymous variable which returns true without telling us the males name. */


/* Lists in Prolog. (Used to store data that has an unknown number of elements) */

write([albert|[alice, bob]]), nl.   /* We can add items to a list with the | (List Constructor) */
length([1,2,3], X).                 /* X = 3 */
[H|T] = [a,b,c].                    /* Divides list into Head and Tail : H = a and T = [b,c] */

[_, _, [X|Y], _, Z|T] = [a, b, [c, d, e], f, g, h].     /* Lists inside Lists : X = c Y = [d,e] , Z = g T = h*/

List1 = [a,b,c].
member(a, List1).                   /* Find out if a value is in a list with member */

reverse([1,2,3,4,5], X).            /* Some operations on lists */
append([1,2,3], [4,5,6], X).


/* Strings */

name('A random string', X).                                           /* Convert a string into an Ascii character list */
name(X, [65,32,114,97,110,100,111,109,32,115,116,114,105,110,103]).   /* Convert a Ascii character list into a string */

```

[Source](https://www.youtube.com/watch?v=SykxWpFwMGs)


