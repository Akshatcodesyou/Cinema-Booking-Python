import os
from admin_dash import admin_dash
import user
import auth

def main():
    while True:
        print("Welcome to cinema ticket booking!")
        print("1. Admin ")
        print("2. User ")
        print("0. Exit ")

        choice = int(input("Choice: "))

        match choice:
            case 1:
                auth.admin_login()
            case 2:
                auth.user_login()
            case 0:
                print("Session end!")
                break
            case _:
                print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
