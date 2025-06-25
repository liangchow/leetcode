# SQL, Models, and Migrations Notes
Some Data Management Systems are MySQL, PostgreSQl, SQLite etc. We write Python in Django. Django will automatically handle the SQL queries.

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

### Constraints
- CHECK: Ensure a certain value falls within a certain range, e.g., movie rating from 1 to 5.
- DEFAULT: Give a default value.
- NOT NULL
- PRIMARY KEY
- UNIQUE: Guarantee every value is unique

### Functions
- AVERAGE
- COUNT
- MAX
- MIN
- SUM
- ...

### Other Clauses
- `LIMIT`: Limit rows of data returned, e.g., `SELECT * FROM flights LIMIT 5`.
- `ORDER BY`: For example, `SELECT * FROM flights ORDER BY destination`.
- `GROUP BY`: For example, `SELECT * FROM flights GROUP BY origin="London"`.
- `HAVING`
- ...

## Syntax and Queries
**Important**: SQL recognizes end of command using semi-colon `;`.
- `CREATE TABLE`: Create a new table.
- `INSERT`: Insert data.
- `SELECT`: Read data from an existing data table. Combine with `WHERE`, `AND`, `OR`, `IN` and/or `% %` (wild card) to filter specific data.
- `UPDATE`: Update data in a table, i.e., `SET`.
- `DELETE`
- `.mode columns`: In SQLite, make data table as a columns mode.
- `.headers yes`: In SQLite, make the data table looks organized.

```
// Example:

// Create a table with columns: id (INTEGER, PRIMARY KEY=Unique, auto update new row), origin (TEXT), destination (TEXT), and duration (INTEGER)
CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);

// Add a new row to the table flights
INSERT INTO flights (origin, destination, duration) VALUES ("New York", "London", 415);

// Update duration to 430 for the row where origin is "New York" and destination is "London"
UPDATE flights
    SET duration=430
    WHERE origin="New York" AND destination="London";

// Delete data
DELETE FROM flights WHERE destination="Tokyo"

// Read all rows of data from flights 
SELECT * FROM flights;

// Read all rows of origin and destination data from flights
SELECT origin, destination FROM flights;

// Read all data from row 3
SELECT * FROM flights WHERE id=3;

// Read all data where "New York" is the origin
SELECT * FROM flights WHERE origin="New York";

// Read all data where duration is longer than 500 minutes and desitnation is Paris
SELECT * FROM flights WHERE duration > 500 AND destination="Paris";

// Read all data where the origin is "New York" or "Lima"
SELECT * FROM flights WHERE origin IN ("New York", "Lima");

// Read all data where the origin has "a" in it
SELECT * FROM flights WHERE origin LIKE "%a%";
```
## Foreign Keys
Like "referencing" data to another dataset. For example, create code for each airport using `foreign keys`.

id|code|city
---|---|---
1|JFK|New York
2|PVG|Shanghai
3|IST|Istanbul




Watch video: [CS50W - Lecture 4 - SQL, Models and Migrations](https://www.youtube.com/watch?v=YzP164YANAU)