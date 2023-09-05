//Single Inheritance
class Animal {
    constructor(name) {
       this.name = name;
    }
    speak() {
       console.log(`${this.name} makes a noise.`);
    }
 }
 
 class Mammal extends Animal {
    breathe() {
       console.log(`${this.name} breathes air.`);
    }
 }


//Multilevel Inheritance
 class Dog extends Mammal {
    bark() {
       console.log(`${this.name} barks.`);
    }
 }

 //Hierarcial Inheritance
 class Cat extends Mammal {
    meow() {
       console.log(`${this.name} meows.`);
    }
 }
 
const dog = new Dog('Dobby');
dog.speak();
dog.breathe();
dog.bark();  
const cat = new Cat('Louis');
cat.breathe(); 
cat.meow(); 

//Multiple Inheritance is not allowed in ES6 i.e Multiple parents cannot have the same child.
 