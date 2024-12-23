# Write a Python program to create a database and a table using SQLite3

import sqlite3

#connect db
try:
    db=sqlite3.connect("emp.db")
    print("DB connected")
except Exception as e:
    print(e)

#create tbl
tbl_create="create table empinfo(id integer primary key autoincrement, name text, city text)"

try:
    db.execute(tbl_create)
    print("Table created")
except Exception as e:
    print(e)

#insert tbl
insert_data = "insert into empinfo(name,city)values('Rachna','Jetpur'),('Era','Junagadh'),('Nidhi','Gandhinagar'),('Dhruvi','Ahmedabad'),('Hir','Rajkot')"
try:
    db.execute(insert_data)
    db.commit()
    print("REcord inserted")
except Exception as e:
    print(e)
