BOOK = "server2/bookings.txt"

def view_bookings():
    try:
        with open(BOOK, "r") as file:
            for line in file:
                user, movie, showtime, price = line.strip().split(',')
                print(f"{'Customer:':<10} {user:<20} \n{'Movie:':<10} {movie:<40} \n{'Showtime:': <10} {showtime:<10} \n{'Payment:':<10} {price}")
    except IOError:
        print("Error reading bookings file.")
