# Task 1: Create a Dictionary of Student Marks

# Step 1: Create a dictionary of student names and marks
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92,
    "Ethan": 88
}

# Step 2: Ask the user to enter a student's name
name = input("Enter the student's name: ")

# Step 3: Retrieve and display marks
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the record.")






# Task 2: Demonstrate List Slicing

# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements
first_five = numbers[:5]

# Step 3: Reverse the extracted elements
reversed_list = first_five[::-1]

# Step 4: Print both lists
print("First five elements:", first_five)
print("Reversed list:", reversed_list)
