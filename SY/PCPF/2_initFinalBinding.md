# Initialization, Finalization and Binding

1. <b>Initialization</b> is the assignment of an initial value for a data object or variable. Without initialization, a variable 
would have an unknown value leading to unpredictable outputs when used in computations.
<br>

2. <b>Finalization</b> is the process of putting an object in its final form, usually done just before destroying it. The garbage collector 
takes care of the clean-up activities on the object. To do this in C++ Destructors can also be used explicitly in a class.
<br>

3. <b>Binding</b> refers to the linking between the function call and the function definition. <br>

   a. <b>Static Binding</b> happens at compile-time and also called early binding. This is because all 
   the information needed is available at the compile time. Static binding happens by default for any normal 
   function calls in the program. <br>
   
   b. <b>Dynamic Binding</b> takes place during run time based on the type of object. It is also called late binding/runtime binding. This happens 
   when the compiler cannot determine all the information required to resolve a function call during compile time. It can be achieved with 
   the use of virtual functions or overidden methods.
