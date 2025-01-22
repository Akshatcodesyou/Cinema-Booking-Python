import os
import movies

BOOKINGS = "server/data/bookings.txt"

def user_dash(name):
    while True:
        print("1. View Movies")
        print("2. View Booking")
        print("0. Exit")

        x = int(input("Choice: "))
        match x:
            case 0:
                break
            case 1: 
                movies.view_movies(name)
            case 2:
                movies.view_bookings(name)
            case _:
                pass

            
