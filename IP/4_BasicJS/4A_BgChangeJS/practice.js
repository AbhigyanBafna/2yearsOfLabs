//Basic function
function greet(name){
    return "Hello " + name +"!";
}
const greeting = greet("Abhigyan");
console.log(greeting);

//Anonymous function
const add = function (a,b) {
    return a+b
}=
const sum = add (5,10);
console.log("Sum: ",sum);

//Arrow Function
const multiply = (a,b) => a*b;
console.log(multiply(3,4));

//For loop
for (let i=0; i<5; i++){
    console.log("For loop iteration: "+i);
}

//forEach Loop
const numbers = [1,2,3,4,5];
numbers.forEach((number) => {
    console.log("Number: ",number);
});

//For...inLoop
const person = {
    name: "Abhigyan",
    age: 18,
    occupation: "Engineer"
};
for (const key in person) {
    console.log(key + ":" + person[key]);
}

//For...of Loop
const colors = ["red", "green", "blue"];
for (const color of colors) {
    console.log("Color:", color);
}

//While loop
let count = 0;
while (count < 3){
    console.log("While loop count: " +count);
    count++;
}

// If statement 
const age = 18;
if (age >= 18){
    console.log("You're an adult!");
}
 else {
    console.log ("You're a minor.");
}

//Switch statement 
const day = "Wednesday";
switch (day){
    case "Monday":
        console.log("It's the start of the week");
        break;
    case "Wednesday":
        console.log("It's the middle the week");
        break;
    default:
        console.log ("It's another day");
}

//Conditional Statement 
const score = 85;
if (score >= 90) {
    console.log("A grade");
}else if (score >= 80) {
    console.log ("B grade");
}else {
    console.log("C grade");
}