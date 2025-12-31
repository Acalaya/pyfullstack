"""N = int(input("Enter N: "))
total = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        total += i

print("Sum of even numbers from 1 to", N, "is:", total)
"""
#checking whether is present or not present
"""str= "Hi, It's me the Acalaya!"
if "baby"  in str:
    print("No, 'baby' is NOT present.")
else:
    print("Yes darling") """

# slicing
"""
a = "Baby, Doll"
print(a[2:]) """

# split
"""
a = "Baby, Doll"
print(a.split(',')) """

# decimal
"""
marks = 11
brth = f"I got {marks:.3f} out of 15"
print(brth) """

# escape character
"""
print("HI, what's up darling, I'm so in love with you , you never know. \"hi baby\"") """

#sampleemail with input username and birthyear
"""
username = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
example = username.lower() + str(birth_year)
eml = f"{example}@gmail.com"
print(eml) """
# extracting letters and splitting through a character
"""
sample = "example@gmail.com"
eml = sample.split('@')
username = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
print(f"{username.lower().replace(' ','')}{birth_year}{eml[1]}")  """

#email validation and password more than 8 character and if email= admin@gmail.com and password= admin123, then print you're admin otherwise you're logged in as normal user
"""
eml = input(f"Enter your email: ")
pswd = input(f"Enter your password: ")
x = len(pswd)
if "@gmail.com" in eml and x >= 8 :
    if eml == "admin@gmail.com" and pswd == "admin123":
        print("Admin user")
    else:
        print("Valid user")
else:
    print("Invalid user")  """


# replacing symbols 
"""
s_id = input("Enter your id: ")
print(s_id)
sec_id = s_id.replace('*','#').replace('$','#').replace('^','')
print(sec_id) """

# remove the numbers in a string dleaving the characters behind
"""
text = "123atithi123"
result = ""

for i in text:
    if i.isalpha():
        result += i

print(result) """

# now with input, printing number, character and symbol separately
"""
a = input("Enter your email: ")
num = ''
char = ''
sbl = ''
for i in a:
    if i.isdigit():
        num += i
    elif i.isalpha():
        char += i
    else :
        sbl += i
print(num)
print(char)

print(sbl) """
# 
"""
sample = "example@gmail.com"
eml = sample.split('@')
username = input("Enter your name: ") 

print(f"{username.lower().replace(' ','')}{birth_year}{'@'}{eml[1]}") 
print(birth_year) """

# import datetime
"""birth_year = input("Enter your birthdate: ")
date_format = datetime.date() """

# in list, even and odd number printing
"""
num = [1,2,3,4,5,6,7]
num1 =(num[1:7:2])
num2= (num[0:7:2])
print(num1,num2) """
# dynamic data
"""
num = [1,2,3,4,5,6,7,8,9]
num1 = []
num2 = []
for x in num:
    if x % 2 == 0:
        num1.append(x)
    else:
        num2.append(x)
print(num1, num2 )
 """

# remove even but print everything else
"""
num = [1,2,3,4,5,6,7,8,9]
i = 0
while i < len(num):
    if num[i] % 2 == 0:
        num.remove(num[i])
    i += 1
print(num)
"""
# sorting on key basis
"""
my_list = [
    ['sachin',12],
    ["aasika",57],
    ["amisha",11]
]

def number_sort(x):
    return x[1]

my_list.sort(key = number_sort)
print(my_list)
// lambda function using
my_list = [
    ['sachin',12],
    ["aasika",57],
    ["amisha",11]
]

my_list.sort(key = lambda x: x[1])
print(my_list)
 """


# sum of lists
"""
nums = [
    [1,2,3,5],
    [4,5,6],
    [3,4,5,6]
]
//
summed_up = [(sum(nums[0]),sum(nums[1]),sum(nums[2]))]
//
output = []
for i in nums:
    result = sum(i)
    output.append(result)
print(output) """

# nums = [
#     [1,2,3,4],
#     [2,3,4,5],
#     [4,5,6,7,8]
# ]
# result = 0
# for i in nums:
#     for j in i:
#         if j % 2 == 0:
#             result += j
# print(result)
 
#  add the numbers in list but eliminate duplicacy and any negative numbers
"""
nums = [
    [-1,-2,2,4],
    [1,2,3,8],
    [-10,10,3],
    [4,8,14],
    [-2,-8,-6,20]
]
num_list = []
for i in nums:
    for j in i:
        if j % 2 == 0 and j > 0 :
            num_list.append(j)
no_duplicate_item = set(num_list)
result = list(no_duplicate_item)
print(sum(result)) """

# take user i=url as input and check the format
"""
img = input(f"Enter your image url: ")
if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith(".png"):
    print("valid")
else:
    print("invalid") 
// 
img_url=("https;//upload.acalaya1.jpeg")
img_url_extensions = ['jpeg','jpg','png']
splitted_img = img_url.rsplit('.',1)[1]
if splitted_img in img_url_extensions:
    print("valid image url")
else:
    print("invalid")
    """

# combine the numbers and list in anjother list 
"""
nums = [1,2,3,4,[5,6,7],8,[9,10,11],12]
# output = [1,2,3,4,5,6,7,8,9,10,11,12]
output = []
for i in nums:
    if type(i) == list:
        for j in i:
            output.append(j)
    else:
        output.append(i)
         
print(output) """

