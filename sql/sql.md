### Install sqlite in jupyter notebook

- Open anaconda > go to environments > install ipython-sql

### SQL syntax
- SELECT: extract

Query from all columns

    SELECT * FROM table_name;

Query from a specific column

      SELECT column_name1, column_name2
      FROM table_name;

<code> WHERE </code> is used to filter specific conditions such as =, <, >, and LIKE

      SELECT column_name1, column_name2
      FROM table_name
      WHERE column_name1 > condition;

- UPDATE

        UPDATE table_name
        SET column_name2 = new_value2, 
        WHERE column_name1 = condition;

- DELETE

        DELETE FROM table_name 
        WHERE condition;

- INSERT INTO

        INSERT INTO table_name (column_name1, column_name2)
        VALUES (value1, value2);

- CREATE

Create Table

    CREATE TABLE table_name (
        column1 datatype,
        column2 datatype,
    );

Create Database

    CREATE DATABASE database_name;

Note: VARCHAR, BOOL, INT, FLOAT, DATETIME

- ALTER: modify

Add

    ALTER TABLE table_name
    ADD column_name datatype;

Delete

    ALTER TABLE table_name
    DROP COLUMN column_name1;

Rename

    ALTER TABLE table_name
    RENAME COLUMN old_name to new_name;

- SELECT DISTINCT: different values

        SELECT DISTINCT column_name 
        FROM table_name;

- ORDER BY: sort

         SELECT column1, column2,
         FROM table_name
         ORDER BY column1, column2, ASC|DESC;

         SELECT column_name
         FROM table_name
         WHERE criteria
         ORDER BY column_name;

- GROUP BY

        SELECT column_name  
        FROM table_name
        WHERE condition
        GROUP BY column_name

- AND, OR, NOT

         SELECT column_name1, column_name2,
         FROM table_name
         WHERE NOT condition;

- COUNT, SUM, AVG
          
         SELECT COUNT(column_name)
         FROM table_name
         WHERE condition;

- MIN, MAX

        SELECT MIN(column_name)
        FROM table_name
        WHERE condition;

<br/>
<br/>
