# Firebase Notes

Cloud Firestore is a NoSQL, document-oriented database. We store data in *documents*, which are organized into *collections*. One advantage is less strictly defined data structure, however, it is encouraged to set criteria on the client side. 

- *Collections*: A collection of documents. Collection can only contains *documents* with less than 1MB. A document cannot contain another document. But a collection can point to another sub-collection of documents.
- *Documents*: Each document contains a set of key-value pair (called *fields*), i.e., dictionary in Python. Each *field* can be a string, numbers, boolean, array, map (a smaller .json object) etc. A map example is vector with x, y, and z dimensions.

A Firestore root must be a *collection*. For example, at the first level, it should be at least one *collection* and one *document* to store the data.
This means that general, we will be drilling the data between *collections* and *documents* unti lwe get to the data that we want.

```
Firestore Root
|-- Samples (Collection)
|   |-- Sample_data (document)
|       |-- foo: Hello world"
|       |-- pi: 3.14159


// Accessing data
firestore.collection(...).document(...).collection(...).document(...)

e.g.,
users/user_123/workouts/workout_abc/history/05182017
```

In the restaurant review app:
```
Restaurant (Collection)
|-- Restaurant 1 (Document)
|   |--Name: "BurgerThyme"
|   |--Address: "123 fake St"
|   |--Rating: 4.76
|   |--Reviews: (Subcollection)
|      |-- Review 1 (Document)
|      |   |-- Headline: "Awesome"
|      |   |-- Rating: 5
|      |   |-- Author: {name: "Todd Doe", profile_pic: "http://..."}
|
|-- Restaurant 2 (Document)
|   |--Name: "PandaSlow"
|   |--Address: "100 woo St"
|   |--Rating: 4.2
|   |--Reviews: (Subcollection)

Users (Collection)
|-- User 1 (Document)
|   |--name: "Todd Doe"
|   |--profile_pic: "http://..."
```
## Querying



## Setup
- Install firebase: **`npm i firebase`**
- Log in to Firebase `console`, create a `project`. Create a `web app`.
- Create **`firebase.js`**

```
//firebase.js

import { initializeApp } from 'firebase/app'
import { getFireStore } from 'firebase/firebase'

const firebaseConfig ={
    apiKey: ...,
    authDomain: ...,
    projectId: ...,
    storageBucket: ...,
    messagningSenderId: ...,
    appId: ...,
}

const app = initializeApp(firebaseConfig)

export const db = getFireStore(app)

```
- Create **`.env`** file to store `firebaesConfig()` keys.
- Create a firebase database, `db` .
