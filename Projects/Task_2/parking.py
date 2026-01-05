import os
from datetime import datetime

# Create folders if not exist
os.makedirs("token", exist_ok=True)
os.makedirs("bill", exist_ok=True)

def enter_vehicle():
    vehicle_no = input("Enter vehicle number: ")
    name = input("Enter name: ")
    address = input("Enter address: ")
    vehicle_type = int(input("Enter vehicle type (2 or 4): "))

    entry_time = datetime.now()

    token_filename = f"token/{vehicle_no}_token.txt"

    with open(token_filename, "w") as file:
        file.write("===== Your Token =====\n")
        file.write(f"Vehicle number: {vehicle_no}\n")
        file.write(f"Name: {name}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Entry time: {entry_time.strftime('%I:%M %p')}\n")
        file.write(f"Vehicle type: {vehicle_type}\n")

    print("\n✅ Vehicle entered successfully!")
    print(f"📄 Token created: {token_filename}\n")


def generate_bill():
    vehicle_no = input("Enter vehicle number: ")
    token_filename = f"token/{vehicle_no}_token.txt"

    if not os.path.exists(token_filename):
        print("❌ Token not found!")
        return

    with open(token_filename, "r") as file:
        lines = file.readlines()

    name = lines[2].split(":")[1].strip()
    address = lines[3].split(":")[1].strip()
    entry_time_str = lines[4].split(":",1)[1].strip()
    vehicle_type = int(lines[5].split(":",1)[1].strip())

    entry_time = datetime.strptime(entry_time_str, "%I:%M %p")
    exit_time = datetime.now()

    minutes = abs(int((exit_time - exit_time.replace(
        hour=entry_time.hour, minute=entry_time.minute)).total_seconds() / 60))

    rate = 10 if vehicle_type == 2 else 20
    total_price = minutes * rate

    bill_filename = f"bill/{vehicle_no}_exit_bill.txt"

    with open(bill_filename, "w") as file:
        file.write("======= Your Bill =======\n")
        file.write(f"Vehicle number: {vehicle_no}\n")
        file.write(f"Name: {name}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Entry time: {entry_time.strftime('%I:%M %p')}\n")
        file.write(f"Exit time: {exit_time.strftime('%I:%M %p')}\n")
        file.write(f"Vehicle type: {vehicle_type}\n")
        file.write("=========================\n")
        file.write(f"Total price: Rs {total_price}\n")

    print("\n🧾 Bill generated successfully!")
    print(f"📄 Bill file: {bill_filename}\n")


# Main loop (terminal never closes automatically)
while True:
    print("===== Bharatpur Parking System =====")
    print("1. Vehicle Entry")
    print("2. Generate Bill")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        enter_vehicle()
    elif choice == "2":
        generate_bill()
    elif choice == "3":
        print("👋 Exiting system. Thank you!")
        break
    else:
        print("❌ Invalid choice! Try again.\n")
