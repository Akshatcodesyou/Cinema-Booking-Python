BOOK = "server2/bookings.txt"

def view_revenue():
    try:
        with open(BOOK, "r") as file:
            total = sum(float(line.strip().split(',')[3]) for line in file)
        print(f"\nTotal Revenue: {total} AED\n")
    except IOError:
        print("Error reading revenue file.")
