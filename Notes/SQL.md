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

## Syntax
```
// Create a table with columns: id (INTEGER, PRIMARY KEY=Unique, auto update new row), origin (TEXT), destination (TEXT), and duration (INTEGER)

CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);
```



Watch video: [CS50W - Lecture 4 - SQL, Models and Migrations](https://www.youtube.com/watch?v=YzP164YANAU)