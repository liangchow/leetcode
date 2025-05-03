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



## Array Basic Methods

- **`push()`**: Append data to end of an array, e.g., `[1,2,3].push(4) = [1,2,3,4]`.
- **`pop()`**: Remove the last element in an array, e.g., `[1,2,3].pop() = 3`.
- **`unshift()`**: Append data to beginning of an array, e.g., `[1,2,3].push(0) = [0,1,2,3]`.
- **`shift()`**: Remove the first element in an array, e.g., `[1,2,3].shift() = 1`.

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
# If user.online is true, it doesn't short-circuit the second operand and HAS to return greet(). If user.online is false, it shorts greet() and never returns.
(user.online) && greet()

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

Article: [Javascript Short-Circuit Conditionals](https://medium.com/@amaliesmidth/javascript-short-circuit-conditionals-6606bdeaa30d)