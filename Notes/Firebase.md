# Firebase Notes

Cloud Firestore is a NOSQL, document-oriented database. We store data in *documents*, which are organized into *collections*.
- *Documents*: Each document contains a set of key-value pair. 
- *Collections*:  

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
