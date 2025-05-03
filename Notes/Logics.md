# Logistical Exercise

### 1. Record Collection Exercise

[Record Collection Link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/record-collection)

```
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
function lookUpProfile(name, prop) {
}
```