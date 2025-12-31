# map,filter, zip, enumerate
"""
nums= [1,2,3,4,5,6]
names = ["Ac","Sachin","Keshab","Amisha","Koshish","Aayush"]
def square_nums(x):
    return x**2
map_result = list(map(square_nums,nums)) #map==>higher order function that takes 2 arguments that is function and iterator/collection,loops through all iterator and pass it to the function and return object! 
filter_result = list(filter(lambda x:x%2==0,nums)) #filter ==> filter and just return whatever is included and ignore others
for name,age in list(zip(names,nums)): #zip==> combine 2 interators in the basis of index / create a tuple
    print(name,age)
"""

# find the active user , give the name in list in dictionary 
"""
users = [
    {
        "name": "Sachin",
        "active": True
    },
    {
        "name": "Ac",
        "active": False
    },
    {
        "name": "Amisha",
        "active": True
    }
]
active_user = [{"name":user["name"]} for user in list(filter(lambda x:x["active"]==True,users))]
print(active_user) """

# returning index and value using enumerate 
"""
names = ["Ac","Sachin","Keshab","Amisha","Koshish","Aayush"]
for index,value in enumerate(names):
        print(index,value)
# for i in range(0, len(names)):
#     print(i,names[i]) """


    










