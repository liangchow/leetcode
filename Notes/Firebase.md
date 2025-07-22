# Firebase Notes

Cloud Firestore is a NoSQL, document-oriented database. We store data in *documents*, which are organized into *collections*. One advantage is less strictly defined data structure, however, it is encouraged to set criteria on the client side. 

- *Collections*: A collection of documents. 
- *Documents*: Each document contains a set of key-value pair (called *fields*), i.e., dictionary in Python. Each *field* can be a string, numbers, boolean, array, map (a smaller .json object) etc. A map example is vector with x, y, and z dimensions.


## Setup
- **`npm i firebase`**
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
