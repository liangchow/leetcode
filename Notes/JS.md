# JavaScript Notes

## Objects
Objects are collections of key-value pairs, i.e., dictionary in Python. The object `data` below contains three properties (or *keys*): player, fightingStyle, hair color, age, human, costume color. Each *key* has a *value*.

```
const character = {
    player: "Hworang",
    fightingStyle: "Tae Kwon Do",
    hair color: "orange",
    age: 25 
    human: true,
    costume color: ["blue", "red"]
    }

// JavaScript automatically typecast non-string properties as strings.

const object = {
    make : "Ford",
    5 : "five",
    "model" : "focus"
}


let users = {
    Alan: {
        age: 27,
        online: false,
    },
    Jeff: {
        age: 32,
        online: true,
    },
    Sarah: {
        age: 48,
        online: false,
    }
}
```

Some basic operations to objects are:

- Access object properties with `.` or `[]`, e.g., `character['hair color'] = "orange"`.
- Access value with property name: `character[age]` will return `25`. 
- Add new key-value pair: `character.origin = "South Korea"`, `foods.waterlon = 20`, `character['costume color'] = "white"`.
- Modify object value: `character.age = 20` to update age from `25` to `20`. 
- Delete object properties: `delete character.human`

More....

- **`Object.keys(users)`**: Access properties, e.g., `Object.keys(users) = ["Alan", "Jeff", "Sarah"]`.
- **`Object.hasOwnProperty(prop)`**: Test object for properties, e.g., `users.hasOwnProperty("Ali")` returns `false`.

Finally....<br>
A complex object can have multiple objects. In the example below, each inner object has an `id`, representing a specific object.These objects can have missing data or incomplete.

```
const recordCollection = {
  2548: {
    albumTitle: 'Slippery When Wet',
    artist: 'Bon Jovi',
    tracks: ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    albumTitle: '1999',
    artist: 'Prince',
    tracks: ['1999', 'Little Red Corvette']
  },
  1245: {
    artist: 'Robert Palmer',
    tracks: []
  },
  5439: {
    albumTitle: 'ABBA Gold'
  }
};

function updateRecords(records, id, prop, value) {

    if (value === ''){
        delete records[id][prop]
    } else if (prop !== 'tracks' && value !== ''){
        records[id][prop] = value
    } else if (prop === 'tracks' && value !== ''){
        if (records[id].hasOwnProperty('tracks')){
            records[id][prop] = []
        }

        records[id][prop].push(value)
    }
  return records;
}

```

## Array: Basic Manipulation Methods

- **`push()`**: Append data to end of an array, e.g., `[1,2,3].push(4) = [1,2,3,4]`.
- **`pop()`**: Remove the last element in an array, e.g., `[1,2,3].pop() = 3`.
- **`unshift()`**: Append data to beginning of an array, e.g., `[1,2,3].push(0) = [0,1,2,3]`.
- **`shift()`**: Remove the first element in an array, e.g., `[1,2,3].shift() = 1`.
- **`splice(startIndex,numToRemov,toAdd)`**: Remove multiple or single element inside an array, e.g., `[10,11,12,12,15].splice(3,1, 13, 14) = [10,11,12,13,14,15]`. Starts from index-3 and remove 1 number, which is 12, from the array: `[10,11,12,15]`. Then add 13 and 14 to that position.
- **`slice(startIndex, endIndex)`**: Extract a given number of array, e.g., `[1,2,3,4,5].slice(1,3) = [2,3]`
- **`...`**: Spread operator to copy or combine an array, e.g., `let thisArray = [1,2,3]; let thatArray = [...thisArray]`.
- **`indexOf()`**: Check presence of an element. Return `-1` if non-exists, e.g., `['apple','orange',kiwi'].indexOf('kiwi') = 2`

```
// Build a filter function by using indexOf() to check if something is true or false

function filter(arr, elem):
  let newArray = []
  for (let i=0; i<arr.length; i++){
    if (arr[i].indexOf(elem) == -1){    // push only if elem doesn't exist in the array
      newArray.push(arr[i])
    }
  }

  return newArray

arr = [[10,8,3], [14,6,23], [3,18,6]]
filter( arr, 18)
// returns [[10,8,3], [14,6,23]]
```
### Map, Filter, and Reduce

`.map()`
```
// Example 1:

const users = [
  { name: 'John', age: 34 },
  { name: 'Amy', age: 20 },
  { name: 'camperCat', age: 10 },
]

const names = users.map(user => user.name)
console.log(names)

// return
['John', 'Amy', 'camperCat']

```


`.reduce()`




## Escape quote

| Code   | Output          |
| ------ | --------------- |
| `\'`   | single quote    |
| `\"`   | double quote    |
| `\\`   | backslash       |
| `\n`   | newline         |
| `\t`   | tab             |
| `\r`   | carriage return |
| `\b`   | backspace       |
| `\f`   | form feed       |

```
// Example
const myString = "FirstLine\n\t\\SecondLine"

// Returns:
FirstLine
    \SecondLine
```

## Ternary Operator

A one-line `if/else` statement in syntax `a ? b : c`, where `a` is the condition, `b` is the result when `true` and `c` is false.

```
// Check if a number if negative, positive, or zero

function checkSign(num){
  return (num < 0) ? "negative" : (num > 0) ? "positive" : "zero"
}

```

## Short-Circuit Evaluation

Logical operators `&&` and `||` evaluate from left to right and **short-circuit**, meaning that if left condition is met, it straight up return the result. 

- `false && ***anything***`: Short-circuit to `false`. 
- `true ||  ***anything***`: Short-circuit to `true`.

In other words, think the opposite: if the `true && ***anything***` and `false || ***anything***`, it has to return the second operand, i.e., check the second condition.

```
// If first condition is met, returns the second.

true && true         returns true ---> It has to return the second operand
true && false        returns false --> it has to return the second operand
false && true        returns false
false && false       returns false
true || true         returns true
true || false        returns true
false || true        returns true ---> It has to return the second operand
false || false       returns false --> It has to return the second operand
```
```
user.online = true
const greet = () => cosole.log("Hello! You are online.")

# Code 1
if (user.online){
  greet()
}

# Code 2
# If user.online is true, it doesn't short-circuit the second operand and HAS to return greet(). If user.online is false, it shorts and never returns greet() .
user.online && greet()

// Hello! You are online.
// Hello! You are online.
```
```
user.online = false

# Code 1
# If user.online is NOT false, then greet()
if (!user.online){
  greet()
}

# Code 2
# If user.online is false, it HAS to return greet().
(user.online || greet()) 

// Hello! You are online.
// Hello! You are online.
```
Other uses:

1. Default values **`const name = inputName || 'Guest'`**: If `inputName` is empty or null, name will default to `Guest`.
2. Guarding function calls **`user && user.sendMessage('Hello)`**: This ensures `sendMessage` only if `user` exists.
3. Lazy evaluation **`const res = actionA && actionB()`**: If `actionA` is false, then `actionB()` is skipped, saving resources.


Article: [Javascript Short-Circuit Conditionals](https://medium.com/@amaliesmidth/javascript-short-circuit-conditionals-6606bdeaa30d)

### Recursive

A concept that a function can be expressed in terms of itself. It always start with a *base case* for recursive function to stop calling itself. If a function is written correctly, eventually the *base case* will be reached. The basic formula for recursive is: `fn(n-1) ***operator*** (n-1)`.

```
// Recursive function to return the sum of first n elements of an array, arr

function sum(arr, n){
  if (n <= 0) {         // base case
    return 0
  } else {
    return sum(arr, n-1) + arr[n-1]
  }
}

// Recursive to multiply

function multiply(arr, n) {
  if (n <= 0) {
    return 1;
  } else {
    return multiply(arr, n-1) * arr[n-1];
  }
}

// Recursive to count up. countup(5) returns [1,2,3,4,5]

function countup(n){
  if (n < 1){
    return []
  } else {
    const countArray = countup(n-1)   // for n=5
    countArray.push(n)
    return countArray
  }
}

//Recursive to count down. countdown(5) returns [5,4,3,2,1]

function countdown(n){
  if (n < 1){
    return []                           // start with an exit condition -- a base case. return empty array if n < 1
  } else {
    const countArray = countdown(n-1)   // at n=5, we expect result to be [4,3,2,1]
    countArray.unshift(n)               // last step to add "5" at the beginning of [4,3,2,1]. Similarly, at n=4, add "4" to [3,2,1]
    return countArray                   // return [5,4,3,2,1]...
  }
}
```
Read more about [recursion](https://forum.freecodecamp.org/t/freecodecamp-challenge-guide-use-recursion-to-create-a-countdown/305925/2) <br>
Watch video about [recursion](https://www.youtube.com/watch?v=LteNqj4DFD8&t=584s)