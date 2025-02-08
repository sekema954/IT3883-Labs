# Assignment 2.py
# Course: IT3883/section W02
# Student Name: Samuel Ekema
# Assignment Number: Lab2
# Due Date: 02/7/2025
# Purpose:This program reads a file containing student names and their six grades, calculates their final average, and prints the results in descending order.
# I watched Youtube videos, used geeks.com as well as stackoverflow to help me complete this project.


# Function to calculate student averages and sort them
def process_student_grades(filename):
    # List to store student names and their average scores
    students = []

    # Open and read the input file
    with open(filename, 'r') as file:
        for line in file:
            # Split each line by spaces
            data = line.split()
            name = data[0]
            scores = list(map(float, data[1:]))
            # Calculate average
            average_score = sum(scores) / len(scores)
            students.append((name, round(average_score, 2)))

    # Sort students by their average scores in descending order
    students.sort(key=lambda x: x[1], reverse=True)

    # Print the results
    for student in students:
        print(f"{student[0]} {student[1]:.2f}")


# get input text & process it
filename = "/Users/admin/Downloads/inputs.txt"
process_student_grades(filename)
