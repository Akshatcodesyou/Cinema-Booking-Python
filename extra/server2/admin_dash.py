import os
from movies import manage_movies
from user_management import view_users
from revenue import view_revenue
from bookings import view_bookings

def admin_dash():
    while True:
        print("This is the admin dashboard")
        print("1. View Bookings")
        print("2. Manage Movies")
        print("3. View Revenue")
        print("4. View Users")
        print("0. Exit")

        choice = int(input("Choose: "))
        match choice:
            case 1:
                view_bookings()
            case 2:
                manage_movies()
            case 3:
                view_revenue()
            case 4:
                view_users()
            case 0:
                break
            case _:
                print("Invalid option")
