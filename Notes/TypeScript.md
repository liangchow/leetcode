<a id="top"></a>
# TypeScript Notes

[Learn TypeScript – Crash Course for Beginners](https://www.youtube.com/watch?v=ZvZ7gvcmPmI)

## Table of Contents
1. [Type Annotations with Objects](#type-annotations-with-objects)
2. [Functions](#functions)
    - [Type Annotations with Functions](#type-annotations-with-functions)
    - [Optional Parameters (?)](#optional-parameters-)
    - [Default Parameters (=)](#default-parameters-)
3. [Advanced Types](#advanced-types)
    - [Literal Types (|)](#literal-types-)
    - [Type Alias](#type-alias)
4. [Enums](#enums)

## Type Annotations with Objects
```
// Object
let personExTwo: {
    name: string;
    age: number;
    jobTitle?: string;
    address: {
        street: string;
        city: string;
    };
} = {
    name: "Alice",
    age: 30,
    jobTitle: "Engineer",
    address: {
        street: "123 Main St",
        city: "Oakland',
    },
};
```
[Back to Top](#top)

## Functions
### Type Annotations with Functions
```
// Function to calculate the area of a rectangle
function calcRectArea( length: number, width: number): number {
    return length * width;
}

// Call function with valid arguments
const length = 5;
const width = 3;
const area = calcRectArea(length, width);
console.log(area)   // 15
```

### Optional Parameters (?)
```
// Optional params
function greetOptional(name: string, age?: number){
    if (age !== undefined){
        console.log(`Hello, ${name})! You are ${age} years old.`);
    } else {
        console.log(`Hello, ${name}!`);
    }
}

greetOptional('Alice');         // Output: "Hello, Alice!"
greetOptional('Alice', 30);     // Output: "Hello, Alice! You are 30 years old."
```

### Default Parameters (=)
```
// Default params
function greetDefault(name: string, age: number = 25){
        console.log(`Hello, ${name}! You are ${age} years old.`);
}

greetDefault('Alice');         // Output: "Hello, Alice! You are 25 years old."
greetDefault('Alice', 30);     // Output: "Hello, Alice! You are 30 years old."
```
[Back to Top](#top)

## Advanced Types
### Literal Types (|)
```
// Input can only be these values
let direction: "left" | "right" | "up" | "down";

// Another example
function setColor(color: "red" | "blue" | "green"){
    ...
}
```
### Type Alias
Create custom name for type using `type`.
```
//
type MyString = string;
let myName: MyString = "Glitcher";

// Can be either string or number
type MyStringOrNumber = string | number;
let myValue: MyStringOrNumber = 10;
```
```
// Another example for object
type Employee = {
    name: string;
    age: number;
    email?: string;
};

const alice: Employee = {
    name: "Alice",
    age: 30,
    email: "alice@example.com",
};

const bob: Employee = {
    name: "Bob",
    age: 25;
};

console.log(alice)
console.log(bob)
```
[Back to Top](#top)

## Enums
Assign meaningful names to variables, making code more readable. Commonly used like days and weeks.
```
enum Days {
    Sunday,
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday
}

const today: Days = Days.Wednesday
console.lot(`Today is ${Days[today]}.`)     // Output: Today is Wednesday.
```
[Back to Top](#top)