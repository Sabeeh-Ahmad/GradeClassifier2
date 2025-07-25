# 📝 Grades Classifier - Session 6: Data Structures I - Dictionaries
# Welcome to Python School! Let's help you process your exam scores like a pro 📚✨
# We will update our last session's project to allow adding multiple subjects using
# the 'dict' data structure in Python.

# Print welcome message
print("Welcome to Grade Classifier 2")

# Ask for student name
name = print("Enter the student's name: ")

# Define dictionary of subject labels
# The key should be subject name and the value should be the
# label for that subject. For example, math maps to Mathematics ➗
subject_lvls = {"maths": "Mathematics", "bio": "Biology", "geo": "Geography"}

# Define dictionary to store obtained marks in each subject
obtained_marks_dict = {}

# Take marks for three subjects (out of 100 each)
# Use a for loop to iterate over the appropriate dictionary.
# You should also define and iteratively update a variable for the
# accumulated obtained marks.
obtained_marks = 0

for key, value in subject_lvls.items():
  marks = float(input(f"Enter marks for {value} out of 100: "))
  obtained_marks_dict[key] = marks
  obtained_marks += marks
# Compute total possible marks assuming each subject is 100 marks.
total_marks = len(subject_lvls) * 100

# Calculate average and percentage
avg = round(obtained_marks/len(subject_lvls), 2)
perc = round((obtained_marks/total_marks) * 100, 2)
# Round for nicer output
# Print student report
print("Student Report\n")
# Display results
print("Student:", name)
for key, marks in obtained_marks_dict.items():
  print(f"Your marks in the subject {key} are {marks}.")

print(f"Your total marks are {obtained_marks} out of {total_marks}.\n")
print(f"Your average marks are: {avg}")
print(f"Your percentage is: {perc}\n")
# Assign grade based on percentage
if perc >= 90:
  print("Grade A+")
elif perc >= 80:
  print("Grade A")
elif perc >= 70:
  print("Grade B")
elif perc >= 60:
  print("Grade C")
elif perc >= 50:
  print("Grade D")
else:
  print("Grade F")
# Encouraging message
print("\nKeep working hard and keep learning! 💡📘\n")

# 💡 Notes for learners:
# - Arithmetic: + for addition, / for division, () controls order (precedence).
# - Comparison: >= checks "greater than or equal to".
# - A comparison returns True or False, which we can print as a result.
