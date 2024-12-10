--SQL

-- create table for database schema
CREATE TABLE table_name (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER);

-- database schema
| table_name | 3 rows |
| -----------| ------ |
| id         | INTEGER|
| name       | TEXT   |
| quantity   | INTEGER|

-- Insert data into query result table
INSERT INTO table_name VALUES (1, "Booka", 2);
INSERT INTO table_name VALUES (2, "Bookb", 4);
INSERT INTO table_name VALUES (3, "Bookc", 8);

-- query result
|id| name |quantity| 
|--| -----| -------|
|1 | Booka| 2      |
|2 | Bookb| 4      |
|3 | Bookc| 8      |


-- create a table
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
);

-- example: create a table with four columns to store students result
 CREATE TABLE students (
      id integer PRIMARY KEY,
      name text,
      quantity integer,
      score real
    )
  
-- datatypes
integer: id, phone, quantity
real, float: score
text: name, email
real
blob (binary large object): address

-- constraint uniquely identifies
primary key: identify rows
foreign key
unique
not null

-- insert 
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3, ...);


-- query
-- query table from all columns
SELECT * FROM table_name;

-- query table from a specific column
SELECT column FROM table_name;

SELECT * FROM table_name WHERE column = 'filter';

-- select multiple columns
SELECT column1, column2 FROM table_name;


-- different values from a column in the table_name
-- distinct ensure repeated items only counted once
SELECT DISTINCT column FROM table_name;
SELECT COUNT(DISTINCT column) FROM table_name;

-- sort by asc or desc
SELECT * FROM table_name
ORDER BY column ASC;

SELECT * FROM table_name
ORDER BY column DESC;

SELECT * FROM table_name
ORDER BY column1 ASC, column2 DESC;

-- limit number of rows
-- example: first 5 rows limit
SELECT * FROM table_name LIMIT 5;

-- filter
SELECT * FROM table_name WHERE column > 5 ORDER BY column;

--- 1. GROUP BY display number under this column, 2. SUM, 3. SELECT the column
SELECT column, SUM(quantity) FROM table_name GROUP BY column;

-- filter numeric column
-- select between 1 to 3
SELECT * FROM table_name
WHERE columns BETWEEN 1 AND 3;


-- aggregate find max, min, sum and avg
-- sum
SELECT SUM(quantity) FROM table_name;

-- AND
SELECT * FROM table_name WHERE column1 > 50 AND column2 < 30;

-- OR
SELECT * FROM table_name WHERE column1 > 50 OR column3 > 100;

-- IN: filter a value is in a list instead of using many OR operators
SELECT * FROM table_name WHERE column IN ("column1", "column2", "column3", "column4");

-- subqueries updated in real time
SELECT * FROM table_name WHERE column IN (
    SELECT column FROM table_new_name);

-- LIKE match any rows which contain a in %new_column_ans%
SELECT * FROM table_name WHERE column IN (
    SELECT column FROM table_new_name WHERE new_column LIKE "%new_column_ans%");


-- rename column name
-- before
SELECT column1, sum(column2) FROM table_name GROUP BY column1
-- after
SELECT column1, sum(column2) AS total_column2 FROM table_name GROUP BY column1

SELECT column1, column2, ROUND(column3* 100) AS percent_completed 
FROM table_name;

-- HAVING will base on group values
SELECT column1, SUM(column2) AS total_column2 FROM table_name
    GROUP BY column1
    HAVING total_column2 > 150;

-- HAVING COUNT
SELECT column1 FROM table_name GROUP BY 
column1 HAVING COUNT(*) >= 2;

-- find %
/* 50-90% of max */
SELECT COUNT(*) FROM table_name WHERE
    column1 >= ROUND(0.50 * (220-30)) 
    AND  column1 <= ROUND(0.90 * (220-30));

-- CASE: similar to if switch
SELECT type_column, column1,
    CASE 
        WHEN column1 > 220-30 THEN "condition1"
        WHEN column1 > ROUND(0.90 * (220-30)) THEN "condition2"
        WHEN column1 > ROUND(0.50 * (220-30)) THEN "condition3"
        ELSE "condition4"
    END as "new_column_created"
FROM table_name;


SELECT COUNT(*),
    CASE 
        WHEN column1 > 220-30 THEN "condition1"
        WHEN column1 > ROUND(0.90 * (220-30)) THEN "condition2"
        WHEN column1 > ROUND(0.50 * (220-30)) THEN "condition3"
        ELSE "condition4"
    END as "new_column_created"
FROM exercise_logs
GROUP BY new_column_created;


SELECT COUNT(*),
    CASE
        WHEN number_grade > 90 THEN "A"
        WHEN number_grade > 80 THEN "B"
        WHEN number_grade > 70 THEN "C"
        ELSE "F"
    END AS "letter_grade"
FROM student_grades
GROUP BY letter_grade 


-- example from hackerank 
-- If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
-- substring (string, start, length)
SELECT NAME FROM students WHERE  marks > 75 ORDER BY substring(NAME, LENGTH(NAME)-2, 3), ID;


-- null 
SELECT column_names
FROM table_name
WHERE column_name IS NULL;

-- not null
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;

-- group different ids (ex1_id, ex2_id and ex3_id) into 1 id
SELECT DISTINCT ex2_id as id
FROM Views
WHERE ex2_id = ex3_id
ORDER BY id ASC;

-- if characters used in the column of the table is strictly greater than 5
SELECT column1
FROM table_name WHERE LENGTH(column2) > 5;

-- find the difference between the maximum and minimum columns in table_name
SELECT MAX(column) - MIN(column)
FROM table_name;

-- sum of round
SELECT ROUND(SUM(column1), rounded decimal value), ROUND(SUM(column2), rounded decimal value)
FROM table_name;
