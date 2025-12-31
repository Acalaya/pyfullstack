
# position argument and named argument
"""
def student_info(name,age,college):
    print(f"{name},{age},{college}")
student_info("Ac",23,"u-tech") //position argument
student_info(age=23,name="Ac",college="u-tech") //named argument
"""
# condition and default values
"""
def product(name,year=None,company=None):
    if year is not None:
        print(f"{year}")
    print(f"{name},{year},{company}")
product(name="glass",company="Acalaya") """

# *args and **kwargs
"""
# //args
c = 0
def demo(a,b,*args):
    c = list(args)
    c.append(11)
demo(1,2,3,4,5,6,7,8,9,10)

 //kwargs
d = 0
def second_demo(a,b,*args,name,age,**kwargs):
    return kwargs

d = second_demo(1,2,3,4,5,6,name="Ac",age= 23,college="devsign",course="python",position="developer") 
print(d)
d.update({"god":"shiva jii"})
print(d) """






