<a id="top"></a>
# SQL, Models, and Migrations Notes
Some Data Management Systems are MySQL, PostgreSQl, SQLite etc. We write Python in Django. Django will automatically handle the SQL queries.

## Table of Contents
1. [General Notes](#general-notes)
2. [Syntax and Queries](#syntax-and-queries)
3. [Foreign Keys](#foreign-keys)
4. [SQL Models](#sql-models)


## General Notes
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

### Joining Table, e.g., Relationship Database
How to relate a dataset to another. For example, how mnay flight can be associated with many passengers.

**Passengers**
id|first|last|flight_id
---|---|---|---
1|Harry|Porter|1
2|Ron|Weasley|1
3|Hermione|Granger|2

Create a new table, **People**, to store people info with `id`.

**People**
id|first|last
---|---|---
1|Harry|Porter
2|Ron|Weasley
3|Hermione|Granger

Then, another new table **Passengers** with a `foreigh key` using `id`. The idea is Join Table from one table to another for mapping passenger to flight.
person_id|flight_id
---|---
1|1
2|1
2|4
3|2

```
// Join table using JOIN and ON: Select each person's "first, origin and destination" from the "flights" table, then join with the "passengers" table based on (related together) the "flight_id" column in the "passengers" table, that is associated with "id" in the "flights" table.

SELECT  first, origin, destination
    FROM flights JOIN passengers
    ON passengers.flight_id = flight.id;
```
first|origin|destination
---|---|---
Harry|New York|London
Ron|New York|London
Hermione|Shanghai|Paris

- `JOIN / INNER JOIN` Example above. Cross compare two tables based on the condition specified. Only returns the results when there's match on both sides.
- `LEFT OUTER JOIN`
- `RIGHT OUTER JOIN`
- `FULL OUTER JOIN`
- `CREATE INDEX`: For example, `CREATE INDEX idx ON passengers (last);` creates index called 'idx' on the last name in the passengers table

## SQL Models 
### models.py and Migration
Every `model` is a `class`. Each changes to the dataset needs to migrate in django.

```
// flights > models.py

from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```

-`python manage.py makemigrations`: Create the model Flight. A new file `0001_initial.py` is created.
-`python manage.py migrations`: To apply the migration, including `0001_initial`. A new `db.sqlite3` database file is created.
-`python manage.py shell`: To enter python shell to access the sqlite3 database. No need to use SQL syntax.

```
// To insert data

>>> from flights.model import Flight
>>> f = Flight(origin="New York", destination="London", duration=415)
>>> f.save()

// To read data

>>> flights = Flight.objects.all()
>>> flights
<QuerySet [<Flight: 1:New York to London>]>
>>> flight = flights.first()
>>> flight.id
1
>>> flight.duration
415

```



Watch video: [CS50W - Lecture 4 - SQL, Models and Migrations](https://www.youtube.com/watch?v=YzP164YANAU)