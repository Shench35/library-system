import mysql.connector
from library_file import *
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '' ,
    database = 'LIBRARY_original'
)

#query = input('Enter your desired book')
my_cursor = mydb.cursor()
my_cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
book_id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255) NOT NULL,
quantity_available INT DEFAULT 0,
author VARCHAR(255),
year INT DEFAULT 0,
edition_count INT DEFAULT 1,
availability VARCHAR(255) DEFAULT 'Available',
UNIQUE (title, author),
INDEX (title),
INDEX (author)
)
""")


my_cursor.execute("""
CREATE TABLE IF NOT EXISTS the_library_logins (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    usernames VARCHAR(255),
    passwords VARCHAR(255)
)
""")

my_cursor.execute("""
CREATE TABLE IF NOT EXISTS admin(
    name VARCHAR(255),
    position VARCHAR(255),
    salary INT
)""")

my_cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_no VARCHAR(255),
    email VARCHAR(255)
)
""")

sqlformula = """
INSERT INTO books 
(title, quantity_available, author, year, edition_count, availability, link)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
sqlformula_1 = """
INSERT INTO the_library_logins 
(usernames, passwords)
VALUES (%s, %s)
"""

sqlformula_2 = """
INSERT INTO admin
(name, position, salary)
VALUES (%s, %s, %s)
"""

sqlformular_3 = """
INSERT INTO customers
(first_name, last_name, phone_no, email)
VALUES (%s ,%s ,%s ,%s)
"""

sqlformula_4 = """
SELECT * FROM books
"""



