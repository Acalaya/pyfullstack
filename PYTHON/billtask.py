# Task 1: todo app, task, is copletd or not (true/false)  , add and delete 
# def task(task_list,task_completed,):
# print output as below

# ======= Your Bill =====
# moble ===== Rs total price
# television === Rs total price
# watch === Rs total price
# pen ==== Rs total price
# ================================
# total price = Rs (all product price)

inventory = [
    {
        "product_name": "mobile",
        "price": 1234,
        "qty": 5
    },
    {
        "product_name": "television",
        "price":22345,
        "qty": 2
    },
    {
        "product_name": "watch",
        "price":12,
        "qty": 10
    },
    {
        "product_name": "pen",
        "price":10,
        "qty": 200
    }
]
with open("practise.txt","w") as file:
    file.write("=========== Your Bill =============\n")
    total_price = 0
    for i in inventory:
            product_name = i["product_name"]
            price = i["price"]
            qty = i["qty"]
            total = price * qty
            file.write(f"{product_name}===> Rs. {total}\n")
            total_price += total
    file.write("=======================\n")
    file.write(f"Total price ===> Rs. {total_price}") 

    


