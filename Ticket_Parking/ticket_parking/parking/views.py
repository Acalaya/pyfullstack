from django.shortcuts import render
import os
from datetime import datetime 
# Create your views here.


TOKEN_DIR = "token"
BILL_DIR = "bill"

os.makedirs(TOKEN_DIR, exist_ok=True)
os.makedirs(BILL_DIR, exist_ok=True)


def home(request):
    return render(request, "parking/home.html")


def enter_vehicle(request):
    if request.method == "POST":
        vehicle_no = request.POST.get("vehicle_no")
        name = request.POST.get("name")
        address = request.POST.get("address")
        vehicle_type = int(request.POST.get("vehicle_type"))

        entry_time = datetime.now()

        token_filename = f"{TOKEN_DIR}/{vehicle_no}_token.txt"

        with open(token_filename, "w") as file:
            file.write("===== your token =====\n")
            file.write(f"Vehichle number: {vehicle_no}\n")
            file.write(f"Name: {name}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Entry time: {entry_time.strftime('%I:%M %p')}\n")
            file.write(f"Vehicle type: {vehicle_type}\n")

        return render(request, "parking/success.html", {"msg": f"Token created: {token_filename}"})

    return render(request, "parking/enter_vehicle.html")


def generate_bill(request):
    if request.method == "POST":
        vehicle_no = request.POST.get("vehicle_no")

        token_filename = f"{TOKEN_DIR}/{vehicle_no}_token.txt"

        if not os.path.exists(token_filename):
            return render(request, "error.html", {"msg": "Token not found!"})

        with open(token_filename, "r") as file:
            lines = file.readlines()

        name = lines[2].split(":")[1].strip()
        address = lines[3].split(":")[1].strip()
        entry_time_str = lines[4].split(":", 1)[1].strip()
        vehicle_type = int(lines[5].split(":", 1)[1].strip())

        entry_time = datetime.strptime(entry_time_str, "%I:%M %p")
        exit_time = datetime.now()

        minutes = abs(int((exit_time - exit_time.replace(
            hour=entry_time.hour, minute=entry_time.minute
        )).total_seconds() / 60))

        rate = 10 if vehicle_type == 2 else 20
        total_price = minutes * rate

        bill_filename = f"{BILL_DIR}/{vehicle_no}_exit_bill.txt"

        with open(bill_filename, "w") as file:
            file.write("======= Your Bill =======\n")
            file.write(f"Vehichle number: {vehicle_no}\n")
            file.write(f"Name: {name}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Entry time: {entry_time.strftime('%I:%M %p')}\n")
            file.write(f"Exit time: {exit_time.strftime('%I:%M %p')}\n")
            file.write(f"Vehicle type: {vehicle_type}\n")
            file.write("=========================\n")
            file.write(f"Total price: Rs {total_price}\n")

        return render(request, "success.html", {"msg": f"Bill created: {bill_filename}"})

    return render(request, "parking/generate_bill.html")

