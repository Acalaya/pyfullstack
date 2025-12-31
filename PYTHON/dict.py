# funtion looping key, value pair 
"""
students = {
    "name": "Acalaya",
    "class": "Python",

}
for key,value in students.items():
    print(f"{key} ===> {value}")
"""
# find the result of koshish 
"""
student_info = {
    "name": "Kosish",
    "roll_no": 11,
    "marks" : [20,30,40],
    "subjects": ("math","english","science"),
    "numbers" : [
    [-1,-2,2,4],
    [1,2,3,8],
    [-10,10,3],
    [4,8,14],
    [-2,-8,-6,20]]
}
sub = student_info["marks"]
result = (sum(student_info["marks"]))
prct = result / len(sub)
print(f"{student_info['name']} got {result} with {prct} '%'")
"""

# if it is black friday,find the product price with the given discount
"""
data = {
    "product_name" : "mobile",
    "product_price": 170000,
    "is_black_friday": True,
    "discout_percentage": 15,
}
disc_price = (data["product_price"] * data["discout_percentage"])/100
total_price = data["product_price"]- disc_price
print(total_price)
# for key,value in data.items():
#     print(f"{key,{value}}")

if data["is_black_friday"]:
        print("Total Price:", total_price)
else:
        print("nothing")
"""

# take a dictionary, access the data and update the data 
"""
Student_info = []
for i in range(0,3):
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    course = input("Enter your course: ")
    Student_info.append({
        'name' : name,
        'age' : age,
        'course' : course
    })
print(Student_info)
//
data = {}
data.update({
    'name' : name,
    'age' : age,
    'course' : course
})
//
"""
# remove
"""
student_info = {
    "name": "atithi",
    "age": 23
}
name = student_info.pop("college","Utech")
print(f"student_info ===> {student_info}")
print(f"removed_item ===> {name}")
// 
popitem //
popped_item = student_info.popitem()
print(student_info)
print(f"popped_item ===> {popped_item}")
//
del student_info["age"]
print(student_info)
//
student_info.clear()
print(student_info)
//
"""
# access math (nested dictionary) 
"""
student_info = {
    "name": "sachin",
    "marksheet": {
        "Nepali": 80,
        "English": 50,
        "Math": 24
    }
}
marks = student_info.get("marksheet")
maths = marks.get("Math")
print(maths) """

# find the total marks, compare the data , find position and score
student_info = [
    {
        "name": "kosish",
        "roll_no": 21,
        "marks": [60,67,80,50]
    },
    {
        "name": "Atithi",
        "roll_no": 1,
        "marks": [61,68,90,50]
    },
    {
        "name": "Keshab",
        "roll_no": 2,
        "marks": [50,67,98,50]
    },
    {
        "name": "Aarjan",
        "roll_no": 17,
        "marks": [60,62,80,90]
    },
]
result = []
for i in student_info:
    marks = i["marks"]
    name = i["name"]
    total_marks = sum(marks)
    result.append((name,total_marks))

# def sort_result(x):
#     ('kosish',257),
#     return x[1],

result.sort(reverse=True, key = lambda x:x[1])
print(result)

name_of_student = result[0][1]
marks_of_student = result[0][0]

print(f"{name_of_student} got the first rank with total marks {marks_of_student}.")


    



