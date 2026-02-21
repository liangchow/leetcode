# TypeScript Notes
## Table of Contents
1. [Type Annotations with Objects](#type-annotations-with-objects)
2. [Type Annotations with Functions](#type-annotations-with-functions)

## Type Annotations with Objects
```
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