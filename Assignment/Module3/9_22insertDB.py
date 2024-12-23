# Write a Python program to insert data into an SQLite3 database and fetch it

import sqlite3

#connect db
try:
    db=sqlite3.connect("emp.db")
    print("DB connected")
except Exception as e:
    print(e)

#insert tbl
insert_data = "insert into empinfo(name,city)values('Riva','vadodara'),('VIra','Jetpur'),('Rajvi','Gandhinagar'),('DishA','Ahmedabad'),('Hir','Rajkot')"
try:
    db.execute(insert_data)
    db.commit()
    print("REcord inserted")
except Exception as e:
    print(e)