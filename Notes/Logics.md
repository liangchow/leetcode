# Logistical Exercise

### 1. Record Collection Exercise

[Record Collection Link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/record-collection)

```
const records = {
    2548: {albumTitle: "Slippery When Wet", artist: "Bon Jovi", tracks: ["Let It Rock", "You Give Love a Bad Name"]},
    2467: {albumTitle: "1999", artist: "Price", tracks: ["1999", "Little Red Corvette"]},
    2470: {artist: "Robert Palmer", tracks: []},
    ...
}

function updateRecords(records, id, prop, value) {
  return records
}
```

Conditions:
- If `value` is an empty string, delete `prop`.
- If `prop` is not "tracks" and `value` is not an empty string, assign `value` to that `prop`.
- If `prop` is "tracks" and `value` is not an empty string, but the album does not have "tracks", then create an empty array and add `value`.
- If `prop` is "tracks" and `value` is not an empty string, add `value` to the end of existing "tracks" array.

Rewritten to:
1. If `value === ""`, then `delete prop`.
2. If `prop !== "tracks" && value !== ""`, assign `value`. This means to add new prop and value.
3. If `prop === "tracks" && value !== ""`, but `album.hasOwnPropert("tracks) = false`, create `[]` then add `value`.
4. If `prop === "tracks" && value !== ""`, add `value` to existing "tracks". 

```
// Approach:

const album = records[id]

if ( value === "") {                    // i.
    delete album[prop]
} else if ( prop === "tracks" ){        // ii. value is not an empty string after i, skip 2 first
    album[prop] = album[prop] || []     //     first part of 3. Short-circuit eval. If album[prop] is false, it has to return an empty array, []
    album[prop].push(value )            //     second part of 3 and condition 4
} else {
    album[prop] = value                 // iii. back to 2. Add new prop and value.
}
```

### 2. Profile Lookup Exercise

[Profile Lookup Link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/profile-lookup)

```
const contacts = [
    {firstName: "Akira", lastName: "Laine", likes: ["chocolate"]},
    {firstName: "Harry", lastName: "Porter", },
    ...
]

function lookUpProfile(name, prop) {
}
```

Conditions:
- `name` should look up `firstName`, `prop` refers to any property in the array of object, `contacts`.
- If both are true, return the value.
- If `name` does not correspond to any contacts, return `No such contact`.
- If `prop` does not exist, return `No such property`.

Rewritten to:
1. If `contacts[i].firstName === name`, look up `prop` and return value.
2. If `prop` not in `contacts[i]`, return `No such property`.
3. If `contacts[i].firstName !== name`, return `No such contact`.

```
// Approach

for (let i=0; i < contacts.length; i++){    // i. loop through every object in the array

    if (contacts[i].firstName === name){
        if (prop in contacts[i]){
            return contacts[i].[prop]       // ii. start with 1 
        }
            return "No such property"       // 2. if not property in the array
    }
}
return "No such contact"                    // iii. 3. name is not even in the array 

```
### 3. Recursive Exercise

[Use Recursion to Create a Range of Numbers Link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/use-recursion-to-create-a-range-of-numbers)

Use recursive to return an array of integers which begins with `startNum` and ends with `endNum`. The starting number will always be less than or equal to the ending number.

```
// Approach
// Similar to countup(n), except with an additional "startNum" variable. Use "startNum" as a criteria for exit condition.

function rangeOfNumbers(startNum, endNum){
    if (starNum > endNum){      // startNum cannot be greater than endNum, so this is the exit condition
        return []
    } else {
        const countArray = rangeOfNumbers(startNum, endNum-1)
        countArray.push(endNum)
        return countArray
    }
}

// rangeOfNumbers(6,9) return [6,7,8,9]
```

### 4. Use Caution When Reinitializing Variables Inside a Loop

[Use Caution When Reinitializing Variables Inside a Loop Link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/debugging/use-caution-when-reinitializing-variables-inside-a-loop)

Fix the code so that zeroArray(3,2) returns `[[0,0], [0,0], [0,0]]`
```
// Problem: Fix the code so that zeroArray(3,2) return the correct result.

function zeroArray(m, n) {
  let newArray = [];
  let row = [];

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      row.push(0);
    }
    newArray.push(row);
  }
  return newArray;
}

let matrix = zeroArray(3, 2);
console.log(matrix);

// return [ [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]]
```

### 5. Reverse a String
[Reverse a String Link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/reverse-a-string)

Reverse `str`. For example, `'hello'` becomes `'olleh'`. `reverseString()` should return a string.

```
// Approach

function reverseString(str){
    const res = ""

    for (let i = str.length-1; i >= 0; i--){
        res += str[i]
    }
}
```

### 6. Factorialize a Number
[Factorialize a Number Link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/factorialize-a-number)

Return the factorial of the provided integer. For example, `5! = 5*4*3*2*1 = 120`. `factorialize(0)` should return `1`.

```
//Approach

factorialize(num){
    if (num == 0){
        return 1
    } else {
        return factoriallize(num-1)*num
    }
}
```
### 7. Find the Longest Word in a String

[Find the Longest Word in a String Link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/find-the-longest-word-in-a-string)

Return the length of the longest word in a given sentence. It should return a number.

```
// Approach

function findLongestWordLength(str) {
    let word = str.split(' ')   // split sentence to words by a space ' '
    let maxLength = 0

    for (i=0; i < str.length; i++){
        if (word[i].length > maxLength){
            maxLength = word[i].length
        }
    }

    return maxLength
}

function findLongestWordLength(str) {

    return Math.max(...arr.split(' ').map(word => word.length))
}
```

### 8. Return Largest Numbers in Arrays

[Return Largest Numbers in Arrays Link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/return-largest-numbers-in-arrays)

Return an array consisting of the largest number from each provided sub-array. 

```
// Approach

function largestOfFour(arr){
    let res = []

    for (let i=0; i<arr.length; i++){

        let max = arr[i][0]     // initialize max

        for (let j=1; j<arr[i].length;j++){
            if (arr[i][j] > max){
                max = arr[i][j]
            }
        }

    res[i] = max
    }
return res
}
```

### 9. Confirm the Ending

[Confirm the Ending Link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/confirm-the-ending)

Check if a string (first argument, `str`) ends with the given target string (second argument, `target`).

```
// Approach

function confirmEnding(str, target){

    const ext = str.slice(str.length-target.length, str.length)
    return ext == target ? true : false
}

function confirmEnding(str, target){
    return str.slice(str.length-target.length) === target
}

function confirmEnding(str, target){
    return str.slice(-target.length) === target
}

```

### 10. Repeat a String Repeat a String

[Repeat a String Repeat a String Link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/repeat-a-string-repeat-a-string)

Repeat a given string `str` (first argument) for `num` times (second argument).

```
// Approach

function repeatStringNumTimes(str, num){
    let res = ''
    for (let i=0; i<num; i++){
        res += str
    }
    return res
}
```

### 11. Truncate a String

[Truncate a String Link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/truncate-a-string)

Truncate a string (first argument) if it is longer than the given maximum string length (second argument). Return the truncated string with a `...` ending.

```
// Approach

function truncateString(str, num) {
    if (num >= str.length){
        return str
    } else {
        return str.slice(0,num) + "..."
    }
}

function truncateString(str, num) {
    if (str.length > num) {
        return str.slice(0, num) + "...";
    } else {
        return str;
    }
}
```

### 12. Finders Keepers

[Finders Keepers Link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/finders-keepers)

Create a function that looks through an array `arr` and returns the first element in it that passes a 'truth test'. This means that given an element `x`, the 'truth test' is passed if `func(x)` is `true`. If no element passes the test, return `undefined`.

```
// Approach

function findElement(arr, func) {

  for (let i=0; i<arr.length;i++){
    if (func(arr[i])){
      return arr[i]
    }
  }
}
```
