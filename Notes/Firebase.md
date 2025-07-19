# Firebase Notes

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
- Create **`.env`** file to store `firebaesConfig()` privately.