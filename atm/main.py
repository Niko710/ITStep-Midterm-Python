import json
from pathlib import Path


DATABASE = Path(__file__).parent/"users.json"

# reading database and returning it, with creating, if it doesn't exist
def read_database():
    try:
        with open(DATABASE, mode="r", encoding="utf-8") as f:
            users: dict = json.load(f)
        return users
    except FileNotFoundError:
        with open(DATABASE, mode="w", encoding="utf-8") as f:
            structure = {
                "users": []
            }

            json.dump(structure, f)
        
        return structure

# saving changes in database
def save_changes_database(user: dict):
    users: dict = read_database()

    for i, u in enumerate(users["users"]):
        if u["id"] == user["id"]:
            users["users"][i] = user
            break
    
    with open(DATABASE, mode="w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

# generate unique id for registration
def generate_id(user_list: list[dict]) -> int:
    if not user_list:
        return 1001
    return max(user["id"] for user in user_list) + 1

# getting and validating username
def get_username() -> str:
    users = read_database()
    while True:
        username = input("Enter your username: ").strip()
        if username:
            for user in users["users"]:
                if username == user["username"]:
                    print("Username is already taken, try another username")
                    break
            else:
                return username
        else:
            print("Invalid username, try again...")

# validating password
def get_password() -> str:
    while True:
        password = input("Enter the password minimum of length 8: ").strip()
        if len(password) < 8:
            print("Invalid length, must be at least 8 symbols, try again!")
            continue
        return password

# creating user and adding him to databse
def create_user():
    users: dict = read_database()

    new_user = {
        "id": generate_id(users["users"]),
        "username": get_username(),
        "password": get_password(),
        "first_name": input("Enter your first name: ").strip().capitalize(),
        "last_name": input("Enter your last name: ").strip().capitalize(),
        "balance": 0.0
    }

    users["users"].append(new_user)

    with open(DATABASE, mode="w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

    return new_user

# performing user authorization
def login() -> dict:
    username = input("Enter your username for authorization: ")

    users = read_database()

    for user in users["users"]:
        if user["username"] == username:
            for i in range(3):
                password = input("Enter your password: ")
                if user["password"] == password:
                    print("Authorization was successful!")
                    return user
                else:
                    if (2 - i) == 0:
                        print("Authorization failed, no more attempts!")
                        return {}
                    else:
                        print(f"Incorrect password, you have {2 - i} attempts, try again...")
    else:
        print("Username was not found, try another time...")
        return {}

# showing user balance
def view_balance(user: dict):
    print(f"Balance: {user['balance']:.2f}$")

# depositing money to authorized user account
def deposit(user: dict):
    amount = input("Please, enter amount to deposite: ")
    
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid datatype. Amount must be float or int!")
        return

    if amount <= 0:
        print("Amount is incorrect, must be > 0")
        return

    user["balance"] += amount

    save_changes_database(user)
    

# withdrawing money from authorized user account
def withdraw(user: dict):
    amount = input("Please, enter amount to withdraw: ")

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid datatype. Amount must be float or int!")
        return

    if amount <= 0:
        print("Amount is incorrect, must be > 0")
        return

    if amount > user["balance"]:
        print("Not enough balance!")
        return
    
    user["balance"] -= amount

    save_changes_database(user)


def main():
    # User authoriation
    while True:
        action = input("Welcome to ATM. Choose your action (login/register): ").strip().lower()

        if action == "register":
            user: dict = create_user()
            break
        elif action == "login":
            user: dict = login()
            break
        else:
            print("Uknown commands, try again...")

    # Authorization failed
    if not user:
        print("Program is closing due to login error!!!")
        return

    # Implementing balance/deposit/withdraw/exit features
    while True:
        action = input("Choose your action (balance/deposit/withdraw/exit): ").strip().lower()

        if action == "balance":
            view_balance(user)
        elif action == "deposit":
            deposit(user)
        elif action == "withdraw":
            withdraw(user)
        elif action == "exit":
            print("Programm has been finished! All data is saved! Thank you for using our system!")
            break
        else:
            print("Wrong command, use only listed ones, try again...") 


if __name__ == "__main__":
    main()