# TypeScript Notes
## Table of Contents
1. [Type Annotations with Objects](#type-annotations-with-objects)

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