# Step 1: Create a dictionary with student names and marks
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88,
    "Eva": 95
}

# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")

# Step 3: Retrieve and display the marks if the student exists
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")
