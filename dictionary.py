marks = {
    "Sonu": 100,
    "Adarsh": 75,
    "Dilip": 81,
    "Sheela": 99,
    "Ramesh": 60,
    "Kavita": 88
}

# Printing marks of entire dictionary
print(marks) 

# Prinitng marks of a particular student
print(marks["Dilip"])

# Updating marks of a particular student 
marks.update({"Adarsh": 89})

# Printing updated marks 
print(marks["Adarsh"])

# Adding a new student and marks
marks["Anita"] = 31

# printing updated dictionary
print(marks)

# Removing a particular student from dictionary 
marks.pop("Ramesh")

# Prinitng updated dictionary
print(marks)

# Removing last inserted student from dictionary
marks.popitem()

# Prinitng updated dictionary
print(marks)

# Printing all student names 
print(marks.keys())

# Printing all marks 
print(marks.values())

# Printing all items in dictionary
print(marks.items())

# Clearing entire dictionary
marks.clear()