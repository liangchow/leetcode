# TypeScript Notes
## Table of Contents
1. [Type Annotations with Objects](#type-annotations-with-objects)
2. [Type Annotations with Functions](#type-annotations-with-functions)
3. [Optional Parameters (?)](#optional-parameters-)
4. [Default Parameters (=)](#default-parameters-)

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

## Type Annotations with Functions
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

## Optional Parameters (?)
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

## Default Parameters (=)
```
// Default params
function greetDefault(name: string, age: number = 25){
        console.log(`Hello, ${name}! You are ${age} years old.`);
}

greetDefault('Alice');         // Output: "Hello, Alice! You are 25 years old."
greetDefault('Alice', 30);     // Output: "Hello, Alice! You are 30 years old."
```