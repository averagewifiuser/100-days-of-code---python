'''
login with file

'''
import json


json_db = open('sample.json', 'r')

# sample = open('sample.json', 'w')
# json.dump(data, sample, indent=1)
# sample.close()


def login():
    users = json_db.read()
    print("Enter your credentials to login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username]["password"] == password:
        print(f"Welcome {users[username]['name']}")
    else:
        print("email/password mismatch")


def register():
    users = json_db.read()
    print("Register with your username, name and password")

    name = input("Enter your name: ")
    username = input("Enter your preferred username: ")

    while username in users:
        print("That username is taken use another one")
        username = input("Enter your preferred username: ")

    print("Passwords must be at least 8 characters long")
    password = input("Enter your password: ")

    while len(password) < 8:
        print("Invalid Password")
        print("Passwords must be at least 8 characters long")
        password = input("Enter your password: ")

    
    new_user = {
            "name": name,
            "password": password
        }

    users[username] = new_user

    sample = open('sample.json', 'w')
    json.dump(users, sample, indent=1)
    sample.close()


    print("User created successfully!")

    print("\n")
    login()


def init():
    print("Welcome!")
    user_choice = input("Enter R to register and any other key to Login: ")

    if user_choice == "R" or user_choice=="r":
        register()
    else:
        login()

if __name__ == '__main__':
    init()



