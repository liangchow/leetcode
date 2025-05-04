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
