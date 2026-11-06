# Week 2: MySQL and Databases

Lab exercises from the Week 2 workbook, done in MySQL Workbench.

## Exercise 1: Sakila

- Ex1B_first_query.sql: my first queries on the Sakila sample database
- Ex1C_sakila_exploration.sql: queries on the actor and film tables

## Exercise 2: Normalization and database design

- Ex2A_events_normalized.xlsx: normalized events data (practice)
- Ex2B_ERD.png: my database diagram (ERD) from the group workshop

## Exercises 3 and 4A: Group workshop

Designed and built a database with my group (the lana_dog_walking schema).

- Ex3A_tables.xlsx: my table design
- Ex3A_create_tables.sql: creates the tables
- Ex4A_insert_records.sql: inserts the records

## Exercise 4B: Importing and exporting data

- Imported the survey results into the survey_results table in the dunkin schema with the Table Data Import Wizard
- Ran SELECT * to check the import
- Ex4B_survey_results.csv: original data
- Ex4B_survey_results.json: result exported from Workbench

## Exercise 4C: Northwind

- Loaded the Northwind database from a script
- Ex4C_northwind_extract.sql: SELECT queries on employees, products and categories, with comments answering the workbook questions
- Ex4C_order_sample.csv: first 50 orders (OrderID, OrderDate, ShipName, ShipCountry) exported from Workbench

## What I learned

- Fixing a MySQL login problem by resetting the root password
- Why the import wizard failed when it tried to create a new table, and how to import into an existing table instead