# Assignment 5.py
# Course: IT3883/section W02
# Student Name: Samuel Ekema
# Assignment Number: Lab3
# Due Date: 04/19/2025
# Purpose: This program reads a text file with temperature readings for each day of the week,
""" I watched Youtube videos, used geeks.com, w3schools.com as well
    as stackoverflow to help me complete this project. I also worked on
    a similar project as this before. So it wasn't too hard
"""


import sqlite3

# Create SQLite database and connection
conn = sqlite3.connect("temperatures.db")
cursor = conn.cursor()

# I used SQL query to create the table and set the id as primary key
cursor.execute("""
    CREATE TABLE IF NOT EXISTS TemperatureData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT,
        Temperature_Value REAL
    )
""")

# Read input file and insert data. I used the for loop to insert the data in cols and rows
with open("Assignment5input.txt", "r") as file:
    for line in file:
        try:
            day, temp = line.strip().split()
            cursor.execute("INSERT INTO TemperatureData (Day_Of_Week, Temperature_Value) VALUES (?, ?)", (day, float(temp)))
        except ValueError:
            continue

conn.commit()

# I Queried the average temperature for Sunday and Thursday by using select statement
cursor.execute("""
    SELECT AVG(Temperature_Value) FROM TemperatureData WHERE Day_Of_Week = 'Sunday'
""")
avg_sunday = cursor.fetchone()[0]


cursor.execute("""
    SELECT AVG(Temperature_Value) FROM TemperatureData WHERE Day_Of_Week = 'Thursday'
""")
avg_thursday = cursor.fetchone()[0]

# Print results
print(f"Average temperature on Sunday: {avg_sunday:.2f}°F")
print(f"Average temperature on Thursday: {avg_thursday:.2f}°F")

# Close connection
conn.close()
