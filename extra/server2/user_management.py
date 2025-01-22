USER = "server/users.txt"

def view_users():
    try:
        with open(USER, "r") as file:
            for line in file:
                print(line.strip())
    except IOError:
        print("Error reading users file.")
