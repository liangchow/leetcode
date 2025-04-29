# Javascript Notes

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
```
```
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
- Access keys using `Object.keys(users)` results in array `["Alan", "Jeff", "Sarah"]`.
- Access value with property name: `character[age]` will return `25`. 
- Add new key-value pair: `character.origin = "South Korea"`, `foods.waterlon = 20`, `character['costume color'] = "white"`.
- Modify object value: `character.age = 20` to update age from `25` to `20`. 
- Delete object properties: `delete character.human`

