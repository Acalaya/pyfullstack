# list comprehension syntax 
# for loop ==> [statement looping]
# for if ==> [statement looping if condition ]
# for if/else ==> [statement if condition else statement for looping]
"""
nums = [1,2,3,4,5,6,7,8,9,10]
sq_nums = [i**2 for i in nums if i%2 == 0]
// 
# for i in nums:
#     sq_nums.append(i**2)
//
print(sq_nums) """

# for even, square and for odd, cube 
"""
nums = [1,2,3,4,5,6,7,8,9,10]
sq_nims = [i**2 if i % 2 == 0 else i ** 3 for i in nums]
print(sq_nims) """

# if s starts, 3 letters otherwise capitalize the first letter 
"""
names= ["sachin","sugar", "strawberry","keshab","koshish","dependra","sachina"]
# name = names.split("s")
namies = [(i[0:3]) if i[0] == "s" else (i.capitalize()) for i in names ]
print(namies) """

#  dictionary comprehension
"""
nums = [1,2,3,4,5,6,7,8,9,10]
output = {
    i:i**2
    for i in nums
}
print(output) 
// 
names= ["sachin","sugar", "strawberry","keshab","koshish","dependra","sachina","shivanshi"]
namies = {
    i: i.capitalize() if not i.startswith('s') else i.upper() if i == "shivanshi" else i[0:3]
    for i in names
}
print(namies)  """







