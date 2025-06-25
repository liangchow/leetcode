# SQL, Models, and Migrations Notes
Some Data Management Systems are MySQL, PostgreSQl, SQLite etc.

### SQLite Support Types
- TEXT
- NUMERIC: Boolean, date etc.
- INTEGER
- REAL
- BLOB: Binary large object, like 0 and 1's.
- ...

### MySQL Support Types
- CHAR(size)
- VARCHAR(size): Variable length of characters, i.e., up to "size" of characters.
- SMALLINT, INT, and BIGINT: If number is pretty small, use SMALLINT.
- FLOAT
- DOUBLE
- ...

## Syntax and Queries
- `CREATE TABLE`: Create a new table.
- `INSERT`: Insert data.
- `SELECT`: Read data from an existing data table. 

```
// Example
// Create a table with columns: id (INTEGER, PRIMARY KEY=Unique, auto update new row), origin (TEXT), destination (TEXT), and duration (INTEGER)

CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);

// Add a new row to the table flights

INSERT INTO flights
    (origin, destination, duration)
    VALUES ("New York", "London", 415);

// Read all rows of data from flights 
SELECT * FROM flights;

// Read all rows of origin and destination data from flights
SELECT origin, destination FROM flights;

```
### Constraints
- CHECK: Ensure a certain value falls within a certain range, e.g., movie rating from 1 to 5.
- DEFAULT: Give a default value.
- NOT NULL
- PRIMARY KEY
- UNIQUE: Guarantee every value is unique




Watch video: [CS50W - Lecture 4 - SQL, Models and Migrations](https://www.youtube.com/watch?v=YzP164YANAU)