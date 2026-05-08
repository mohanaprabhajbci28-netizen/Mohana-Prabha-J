import datetime

# 1. Custom Errors
class RoomNotAvailableError(Exception): pass
class InvalidCustomerError(Exception): pass
class PaymentError(Exception): pass

# 2. Global Storage
rooms, customers, bookings = {}, {}, {}

def log(msg):
    with open("hotel_errors.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] {msg}\n")

# 3. Core Functions
def add_room():
    rid = int(input("Room ID: "))
    rooms[rid] = {"price": float(input("Price: ")), "cap": int(input("Cap: ")), "avail": True}

def register():
    cid = int(input("Cust ID: "))
    customers[cid] = input("Name: ")

def book():
    try:
        bid, cid, rid = input("Book ID: "), int(input("Cust ID: ")), int(input("Room ID: "))
        guests = int(input("Guests: "))
        
        if cid not in customers: raise InvalidCustomerError("No Customer")
        if rid not in rooms or not rooms[rid]["avail"]: raise RoomNotAvailableError("Taken")
        if guests > rooms[rid]["cap"]: raise OverflowError("Too many guests")
        if input("Pay? (y/n): ") != 'y': raise PaymentError("No Pay")
        
        rooms[rid]["avail"] = False
        bookings[bid] = {"cid": cid, "rid": rid}
        print("Success!")
    except Exception as e:
        log(e); print(f"Error: {e}")
    finally: print("Done.")

# 4. Simple Menu
while True:
    print("\n1:AddRoom 2:Reg 3:Book 4:Exit")
    op = input("Op: ")
    if op == '1': add_room()
    elif op == '2': register()
    elif op == '3': book()
    elif op == '4': break
