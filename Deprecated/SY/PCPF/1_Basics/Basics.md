# Paradigms and Computer Programming Fundamentals (PCPF)

Programming Paradigms are efficent ways to solve a problem using tools and techniques. <br>

1. <b>Imperitive Paradigm (how to)</b> - Works by following a step by step procedure to reach goal.
   * Procedural - Emphasis on Procedure. Ex - C, C++, Java.
   * Object Oriented - Emphasis on making objects and classes to do computations on. Ex - Java, C++.
   * Parallel Processing - Multiple procedures running together (threads). Ex - Java, NESL.

2. <b>Declarative Paradigm (what to do)</b> - Expresses logic without taking about how to do it.
   * Logical - Consists on a knowledge base over which queries can be run. Ex - Prolog.
   * Functional - Execution of a series of mathematical functions. Ex - Perl, Haskell.
   * Data Programming - Focuses of changes in data rather than hard coding. Ex - SQL.

# Initialization, Finalization and Binding

1. <b><a href = "https://github.com/AbhigyanBafna/collegeLabs/blob/main/SY/PCPF/1_Basics/2_initFinalBinding.cpp">Initialization</a></b> is the assignment of an initial value for a data object or variable. Without initialization, a variable 
would have an unknown value leading to unpredictable outputs when used in computations.

2. <b><a href = "https://github.com/AbhigyanBafna/collegeLabs/blob/main/SY/PCPF/1_Basics/2_initFinalBinding.cpp">Finalization</a></b> is the process of putting an object in its final form, usually done just before destroying it. The garbage collector 
takes care of the clean-up activities on the object. To do this in C++ Destructors can also be used explicitly in a class.

3. <b><a href = "https://github.com/AbhigyanBafna/collegeLabs/blob/main/SY/PCPF/1_Basics/2_initFinalBinding.cpp">Binding</a></b> refers to the linking between the function call and the function definition. <br>

   a. <b>Static Binding</b> happens at compile-time and also called early binding. This is because all 
   the information needed is available at the compile time. Static binding happens by default for any normal 
   function calls in the program. <br>
   
   b. <b>Dynamic Binding</b> takes place during run time based on the type of object. It is also called late binding/runtime binding. This happens 
   when the compiler cannot determine all the information required to resolve a function call during compile time. It can be achieved with 
   the use of virtual functions or overidden methods.

4. <b><a href = "https://github.com/AbhigyanBafna/collegeLabs/blob/main/SY/PCPF/1_Basics/1_callByRefVal.c">Call by Reference /Call by Value</a></b> are two different methods to pass data in a function.<br>

   a. <b>Call by Value</b> copies the data of variables in main function into new variables(formal parameters) and then works with it. Hence
   it never changes the value of actual parameters.  <br>
   
   b. <b>Call by Reference</b> uses actual parameters and hence the changes done in the function are applied in the whole program.

