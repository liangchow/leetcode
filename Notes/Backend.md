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

In `package.json`, add:

- **`"start": "node --watch server.js"`**: To enable server auto-restarting on file saved.
- Or, install **`nodemon`** package.
- Install **`npm i hbr express`** handlebar package for dynamic web rendering.

To create an Express.js, add the following:

```
const express = require('express');
const app = express();
```

For static rendering, add `path` module and HTML pages to `/public`:

```
// myApp.js
// index.html --- static

const express = require('express');
const app = express();
const path = require('path'); //import path module

app.use(express.static(path.join(__dirname, "/public")));

app.get("/", (req, res) => {
    res.send("Hello World");
});

app.listen(3000, ()=>{
    console.log("Server is running on 3000");
})
```
<!-- 
For dynamic rendering, install **`hbr express`** module and 
 -->




