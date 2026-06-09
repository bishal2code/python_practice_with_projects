# Dictonary
student = {"name": "Prajwal Sapkota","RollNo": 12, "isActive": False}

# Access
print(student["name"])

# Add/Update
student["name"] = "Binay Lami"

student["phone"] = False

# Remove
student.pop("isActive")

# Check Memebership
print("name" in student)

print(student)