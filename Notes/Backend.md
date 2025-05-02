# Back-End Development and APIs Notes

## Node Package Manager (npm)

npm (Node Package Manager), is a command line tool to install, create, and share packages of JavaScript code written for Node.js. There are many open source packages available on npm, so before starting a project, take some time to explore so you don't end up recreating the wheel for things like working with dates or fetching data from an API.

The `package.json` file is the center of any Node.js project or npm package. It stores information about your project. It consists of a single JSON object where information is stored in key-value pairs. There are only two required fields; `name` and `version`, but it’s good practice to provide additional information. 

- To initialize: `npm init`. Use `npm init -y` to skip all questions.
- Semantic version: MAJOR-MINOR-PATCH, i.e., `1.2.0`.
    - To allow npm install latest PATCH version, use `~`, i.e., `~1.2.0`.
    - To allow npm install latest MINOR version, use `^`, i.e., `^4.14.0`.

```
// package.json

{
	"author": "liangchow",
	"description": "A project that does something awesome",
	"keywords": ["freecodecamp", "microservice", "guide" ],
	"license": "MIT",
	"version": "1.2.0",
	"name": "fcc-learn-npm-package-json",
	"dependencies": {
		"express": "^4.14.0",
        "hbr": "^1.1.0",
        "nodemon": "^3.1.10"
	},
	"main": "server.js",
	"scripts": {
		"start": "node server.js"
		"dev" : "nodemon server.js"
	},
	"repository": {
		"type": "git",
		"url": "git+https://github.com/freeCodeCamp/boilerplate-npm.git"
	},
	"version": "1.0.0",
	"description": "This is the boilerplate code for the Managing Packages With npm Challenges.",
	"keywords": [],
	"license": "ISC",
	"bugs": {
		"url": "https://github.com/freeCodeCamp/boilerplate-npm/issues"
	},
	"homepage": "https://github.com/freeCodeCamp/boilerplate-npm#readme"
}
```
## Express.js

Express is a Node.js framework for REST APIs. To start a project from scratch, follow these steps:

- **`npm init -y`**: To initializea a Node.js project. Create `package.json`.
- **`npm i exress`**: To install Express.js.
- **`npm --save-dev nodemon`**: To install package in development dependency. Alternatively, in `package.json`, add **`"start": "node --watch server.js"`** to enable server auto-restarting on file saved.
- **`npm i hbr express`**: To install handlebar package for <em>dynamic web rendering</em>.

In the project folder,
- Create a new file called `server.js`.
- Create a script **`"dev": "nodemon server.js",`** in `package.json`.
- Create a new folder called `routes`.

### CRUD-method: Create-post, Read-get, Update-put, and Delete-delete

- **`app.use()`**: Add a new middleware to the app, e.g., error handling.
- **`app.post()`**
- **`app.get()`**
- **`app.put()`**
- **`app.delete()`**
- **`app.listen(port, () => console.log('Server is start on port: ${port}'))`**: Listen to port and console log port number.

For static rendering, add `path` module and HTML pages to `/public`:

```
// myApp.js
// index.html --- static

const express = require('express');
const app = express();
const path = require('path'); //import path module
const port = 3000;

// MIDDLEWARE
app.use(express.static(path.join(__dirname, "/public")));
app.use(express, json()); // We should expect to read json
app.use(require('cors')()); // Call the CORS function to make request on different domains

app.get("/", (req, res) => {
    res.status(200).send("Hello World");
});

app.post('/api/data', (req, res) =>{
	res.status(200).send({message: "where is your package?"})
});

app.listen(port, ()=>{
    console.log("Server is running on port: ${port}");
})
```

<!-- 
For dynamic rendering, install **`hbr express`** module and 
 -->




