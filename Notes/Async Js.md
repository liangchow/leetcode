# Asynchronous JavaScript Notes

## Asynchronous Programming
Asyn programming is a process that allows an app to run set of instruction in parallel (a.k.a. multi-tasking). Several benefits include improved performance, better user XP etc. For example, reduced inefficiencies from an app and efficient data collection.

## Basic Async Example
Time-based rendering, `setTimeout()`
```
setTimeout(() =>{
    console.log('2. Display this first')
}, 1000)

setTimeout(() =>{
    console.log('1. Display this second')
}, 2000)

// Output:
2. Display this first
1. Display this second
```

## Use Callback Function
Caution with the 'callback hell' when too many callback stacks up.
```
function task2(callback){
    setTimeout(() =>{
    console.log('2. Display this first')
    callback();
}, 1000)
}

function task1(callback){
    setTimeout(() =>{
    console.log('1. Display this second')
    callback();
}, 2000)
}

function task3(callback){
    setTimeout(() =>{
    console.log('3. Display this third')
    callback();
}, 500)
}

task1(() => {
    task2(() => {
        task3(() => {
        })
    })
})

// Output:
2. Display this first
1. Display this second
3. Display this third
```

## Promise
A promise is an assurance or guarantee that something will happen in the future. A Promise is an object that holds the future value of an async
operation. For example, requesting some data from a server, the promise, promises us to get that data which we can use in future. `Promise()` has three states: pending, fulfiled, and rejected.

```
// Create a promise, example

const promise = new Promise((resolve, reject) => {
    const allWentWell = true

    if (allWentWell){
        resolve('All things went well')
    } else {
        reject('Something went wrong')
    }
})

// Return: Promise {<fulfilled>: 'All things went well'}

```