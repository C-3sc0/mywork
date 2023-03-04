#program that stores student name and a list of her
#course and grades in a dict

student = {
    "name": "Mary",
    "modules": [
        {
            "courseName": "Programming",
            "grade": 45
        },
        {
            "courseName": "History",
            "grade": 99
        }
    ]
}

print("Student: {}".format(student["name"]))

# mudules in an array in the dict student
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))

