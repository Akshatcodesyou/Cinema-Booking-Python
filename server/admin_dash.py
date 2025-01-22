import os
import movies

BOOK = "server/data/bookings.txt"
USER = "server/data/users.txt"

def view_users():
    while True:
        try:
            with open(USER, "r") as file:
                for index, line in enumerate(file, start=1):
                    line_part = line.strip().split(',')
                    print(f"\nUser {index} : {line_part[0]}\n")
                break
        except IOError:
            print("Error reading user file.")
            return None

def view_revenue():
    while True:
        try:
            with open(BOOK, "r") as file:
                total = 0
                for line in file:
                    line_part = line.strip().split(',')
                    total = total + float(line_part[3])
            print(f"\nTotal Revenue: {total} aed\n")
            break
        except IOError:
            print("Error reading revenue file.")
            return None


def view_bookings():
    while True:
        try:
            with open(BOOK, "r") as file:
                for line in file:
                    line_part = line.strip().split(',')
                    print(f"\n{'Customer: ':<10} {line_part[0]:<20} \n{'Movie: ':<10} {line_part[1]:<40} \n{'Showtime: ': <10} {line_part[2]: <10} \n{'Payment: ':<10} {line_part[3]}")
                break
        except IOError:
            print("Error reading bookings file.")
            return None

def admin_dash():
    while True:
        print("This is admin dashboard")
        print("1. View Bookings")
        print("2. Manage shows")
        print("3. View Revenue")
        print("4. View Users")
        print("0. Exit")

        choice = int(input("Choose: "))
        match choice:
            case 1:
                view_bookings()
            case 2:
                movies.view_movie()
            case 3:
                view_revenue()
            case 4:
                view_users()
            case 0:
                break
            case _:
                print("Invalid option")
