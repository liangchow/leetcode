# Node.js Notes

## Setup Quickguide
1. Install node.js by using `npm -init -y`. 
2. Add dependencies, for example, `npm -i express firebase-admin cors stripe dotenv`.
3. Create a new file called `server.js` in root folder. 
4. Under "scripts", add `"dev": "nodemon server.js"` in `package.json`:
    ```
    "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "nodemon server.js"
    },
    ```
4. Install `nodemon` using `npm i --save-dev nodemon`.
5. Now, you should be able to run server by typing `npm run dev` in the terminal.