# Program: Create a Student Class with a Grade Method

# Step 1: Define the Student class
class Student:
    
    # Step 2: Constructor to initialize student details
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Step 3: Method to calculate grade based on marks
    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"


# Step 4: Create a Student object
name = input("Enter student name: ")
marks = float(input("Enter student marks: "))

student = Student(name, marks)

# Step 5: Display student details and grade
print("Student Name:", student.name)
print("Marks:", student.marks)
print("Grade:", student.get_grade())

# End of Program