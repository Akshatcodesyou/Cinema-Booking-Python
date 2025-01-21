import os
from auth import auth_user
import movies

def create_account():
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    try:
        with open("server/users.txt", "a") as file:
            file.write(f"{name},{email},{password}\n")
        print("Account created successfully!")
    except IOError:
        print("Error creating account.")

def user_dash(name):
    while True:
        print("1. View Movies")
        print("2. View Booking")
        print("0. Exit")

        choice = int(input("Choice: "))
        match choice:
            case 1: 
                movies.view_movies(name)
            case 2:
                pass  
            case _:
                break
