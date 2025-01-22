import os
import admin_dash
from user import user_dash
USER = "server/data/users.txt"

def admin_login():
    print("\nAdmin Login")
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "admin":
        print("Admin login successful.")
        admin_dash.admin_dash()
    else:
        print("Invalid admin credentials.")


def createAcc():
    pass
    

def user():
    while True:
        print("1. Log In")
        print("2. Create Account")
        print("0. Exit")

        choice = int(input("Choice: "))

        match choice:
            case 0:
                break
            case 1:
                user_login()
            case 2:
                createAcc()
            case _:
                print("Error")

def user_login():
    while True:
        umail = input("Email id: ").strip()
        upass = input("Password: ").strip()
        udata = auth_user(umail, upass)
        if udata:
            print(f"Welcome {udata['name']}!")
            user_dash(udata['name'])
            break
        else:
            print("Error finding user! Create account?(y/n)")
            x = str(input()).strip().upper
            if x == 'Y':
                user.createAcc()
            else:
                break

def auth_user(mail, pword):
    try:
        with open(USER, "r") as file:
            for line in file:
                name, stored_email_id, stored_pass = line.strip().split(',')
                if stored_email_id.strip() == mail.strip() and stored_pass.strip() == pword.strip():
                    print("Logged In")
                    return {'name': name, 'college_id': stored_email_id, 'password': stored_pass}
    except IOError:
        print("Error reading user file.")
    return None
