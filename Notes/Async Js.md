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
Caution with the 'callback hill' when too many callback stacks up.
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
// Create a promise, example 1:
const promise = new Promise((resolve, reject) => {
    const allWentWell = true

    if (allWentWell){
        resolve('All things went well')
    } else {
        reject('Something went wrong')
    }
})

// Return: Promise {<fulfilled>: 'All things went well'}

// Example 2:
const promise = new Promise((resolve, reject) => {
    const randomNumber = Math.floor(Math.random() * 10)

    setTimeout(()=>{
        if (randomNumber < 4){
            resolve('Well done')
        } else {
            reject('Oops. Try again')
        } 
    }, 2000)
})

// Return: Before 2 seconds, console shows 'Promise{<pending>}'. After 2 seconds, it shows the result like 'Oops. Try again'.
```
How a promise work: initially, it is set as pending state and then depending on the outcome it will either resolve or reject. In this case, we have to consume the the promise before we can access the data. So, one way to consume the promise is `.then()`.

## .then() and .catch()
Both `.then()` and `.catch()` methods take a callback function. `.then()` consumes the promise, i.e., resolve, while `.catch()` returns the reject.

```
// Example:
const promise = new Promise((resolve, reject) => {
    const randomNumber = Math.floor(Math.random() * 10)

    if (randomNumber < 4){
        resolve('well done')
    } else {
        reject('Oops. Try again')
    }
})

promise.then((value) => {
    console.log(value)
}).catch((error) => {
    console.log(error)
})

// returns: 'well done', depending on the random result, but the resolved ouput is returned.
// returns: 'Oops. Try again', , depending on the random result.

```
## Chaining the Promises, Promise.all()
```
// To chain a series of functions, example:

const promise = new Promise((resolve, reject) => {
    resolve('Well done. Promise one is resolved')
})

const promiseTwo = new Promise((resolve, reject) => {
    resolve('Well done. Promise two is resolved')
})

const promiseThree = new Promise((resolve, reject) => {
    reject('Oops. Promise three is rejected')
})

promise
.then((value) => {
    console.log(value)
    return promiseTwo
})
.then((value) => {
    console.log(value)
    return promiseThree
})
.catch((err) => {
    console.log(err)
})

// return:
'Well done. Promise one is resolved'
'Well done. Promise two is resolved'
'Oops. Promise three is rejected'
```
Use `promise.all()` that takes a array of function --- consumes several promises at the same time. This method is useful when we have multiple promises. For example, if we request different data from different APIs, but we want to only do something with the data when all requests are resolved. If one request failed, we do not want to use the data.

```
// Use of Promise.all() method, example:

const promiseOne = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log('Promise one is resolved!')
    }, 2000)
})

const promiseTwo = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log('Promise two is resolved')
    }, 1500)
})

promise.all([promiseOne, promiseTwo])
.then((data) => console.log(data[0], data[1]))
.catch((err) => console.log(err))

// return the result at the same time even if timeout is different. 
Promise one is resolved! Promise two is resolved
```
## Async/Await
To streamline async codes in a synchronous manner. Basically, it waits to the promise to resolve before moving to the next one. See the example below using `setTimeout()` to emulate different time outs. The `Async/Await` method is easier to read compared to chaining with `.then()` and less complicated than `promise().all`.

```
const preHeatOven = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const preHeatoven = true;

            if (preHeatOven){
                resolve('Preheat oven to 180 deg')
            } else {
                reject('Failed task')
            }
        }, 1000)
    })
}

const addSugarAndChocoChips = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const addSugarAndChocoChips = true;

            if (addSugarAndChocoChips){
                resolve('Place butter and choco chips')
            } else {
                reject('Failed task')
            }
        }, 1000)
    })
}

const bakeChocolateBrownie = async () => {

    try {
    
        const taskOne = await preHeatOven()
        console.log(taskOne)

        const taskTwo = await addSugarAndChocoChips()
        console.log(taskTwo)

        console.log('Enjoy your brownie')

    } catch(err) {
        console.log(err)
    }

}

// Returns:
After 1 sec....Preheat oven to 180 deg
After 1 more sec.....Place butter and choco chips
After 1 more sec.....Enjoy your brownie
```

## Fetch API
```
const getAllProducts = async () => {
    try {
        const response = await fetch('https://dummyjson.com/products/')
        const json = await response.json()
        console.log(json)
    } catch(err) {
        console.log(err)
    }
}

getAllProducts

// Returns:
A json files
```
```
// POST
fetch('https://dummyjson.com/products/add', {
    method: 'POST',
    header: {
        'Content-type': 'application/json'
    },
    body: JSON.stringify({
        description: 'Iphone 19',
        price: '1000'
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(err => console.log(err))

// Returns:
Add 1 product to the list
```
```
// PUT
fetch('https://dummyjson.com/products/1', {
    method: 'PUT',
    header: {
        'Content-type': 'application/json'
    },
    body: JSON.stringify({
        description: 'Iphone 20',
        price: '2000'
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(err => console.log(err))

// Returns:
Update product 1 description and price
```
```
// DELETE
fetch('https://dummyjson.com/products/1', {
    method: 'DELETE',
})
.then(response => response.json())
.then(data => console.log(data))
.catch(err => console.log(err))

// Returns:
Delete product 1 from the list
```
## Example: Chuck Norris API
```
// app.js

const loadJoke = asyn () => {
    try {
        const chuckNorrisFetch = await fetch('https://api.chucknorris.io/jokes/random', {
            headers: {
                Accept: "application/json"
            }
        })

        const jokeData = await chuckNorrisFetch.json()
        document.getElementByID('loadingJoke').innerHTML = jokeData.value

    } catch(err) {
        console.log(error)
    }
}

// onClick button 
document.getElementById('loadJokeBtn').addEventListener("click", loadJoke)

```


Resource:
[Asynchronous JavaScript Course – Async/Await , Promises, Callbacks, Fetch API](https://www.youtube.com/watch?v=OFpqvaJ3QYg)