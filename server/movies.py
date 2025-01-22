MOVIES = "server/data/movies.txt"
BOOK = "server/data/bookings.txt"

def add_movie(movie_data):
    while True:
        try:
            with open(MOVIES, "a") as file:  
                file.write(movie_data)
            print("Movie added successfully.")
            break
        except Exception as e:
            print(f"Error writing to file: {e}")

def view_movie():
    while True:
        try:
            with open(MOVIES, "r") as file:
                movies = []
                for line in file:
                    line = line.strip()
                    movie, genre, duration, rating, showtime1, showtime2, showtime3 = line.split(',')
                    movies.append((movie, genre, duration, rating, showtime1, showtime2, showtime3))

                print(f"{'Movie':<40} {'Genre':<15} {'Duration':<10} {'Rating':<10}")

                for index, (movie, genre, duration, rating, showtime1, showtime2, showtime3) in enumerate(movies, start=1):
                    print(f"{index:<5} {movie:<40} {genre:<15} {duration:<10} {rating:<10}")

                user_input = input("Would you like to add or remove any movies? (y/n): ")
                if user_input.lower() == 'y':
                    user_input = input("Add(1) or Delete(2)): ")
                    if user_input == '1':
                        tempmov = input("Name of the Movie: ")
                        tempgen = input("Genre: ")
                        tempdur = input("Duration(mins): ")
                        temprat = input("Rating: ")
                        tempshowtime1 = input("Showtime: ")
                        tempshowtime2 = input("Showtime: ")
                        tempshowtime3 = input("Showtime: ")
                        movie_data = f"{tempmov},{tempgen},{tempdur},{temprat},{tempshowtime1},{tempshowtime2},{tempshowtime3}\n"
                        add_movie(movie_data)
                        break
                    elif user_input == '2':
                        x = int(input("Select movie to delete by number (0 to exit): "))
                        if 1 <= x <= len(movies):
                            movie_name = movies[x - 1][0]
                            print(f"Movie selected for deletion: {movie_name}")
                            movies.pop(x - 1)

                            with open(MOVIES, "w") as file:
                                for movie in movies:
                                    movie_data = ','.join(movie) + '\n'
                                    file.write(movie_data)

                            print(f"{movie_name} has been deleted successfully.")
                            break
                        elif x == 0:
                            break
                        else:
                            print("Invalid selection. Please try again.")
                    else:
                        print("Invalid selection. Please try again.")
                elif user_input.lower() == 'n':
                    break
                else:
                    print("Invalid input. Please try again.")
        except IOError:
            print("Error reading movies file.")
            return None

def view_movies(name):
    while True:
        try:
            with open(MOVIES, "r") as file:
                movies = []
                for line in file:
                    line = line.strip()
                    movie, genre, duration, rating, showtime1, showtime2, showtime3 = line.split(',')
                    movies.append((movie, genre, duration, rating, showtime1, showtime2, showtime3))

                print(f"{'Movie':<40} {'Genre':<15} {'Duration':<10} {'Rating':<10}")

                for index, (movie, genre, duration, rating, showtime1, showtime2, showtime3) in enumerate(movies, start=1):
                    print(f"{index:<5} {movie:<40} {genre:<15} {duration:<10} {rating:<10}")

                user_input = input("Would you like to book a movie? (y/n): ")
                if user_input.lower() == 'y':
                    x = int(input("Select movie to book by number (0-exit): "))
                    if 1 <= x <= len(movies):
                        movie_name = movies[x - 1][0]
                        showtime = book_movie(movie_name)
                        if showtime:
                            conf_book(name, movie_name, showtime)
                        break
                    elif x == 0:
                        break
                    else:
                        print("Invalid selection. Please try again.")
                elif user_input.lower() == 'n':
                    break
                else:
                    print("Invalid input. Please try again.")

        except IOError:
            print("Error reading movies file.")
            return None

def book_movie(movie_name):
    while True:
        print(f"Booking movie: {movie_name}")
        print("Available showtimes")
        try:
            with open(MOVIES, "r") as file:
                for line in file:
                    line_parts = line.strip().split(',')
                    if movie_name == line_parts[0]:
                        print(f"1. {line_parts[4]} \n2. {line_parts[5]} \n3. {line_parts[6]}")
                        x = int(input("Select a showtime: "))
                        if 1 <= x <= 3:
                            showtime = line_parts[x+3]
                            print(f"Selected showtime: {showtime}")
                            return showtime
                        else:
                            print("Invalid showtime selection. Please try again.")
                return None
        except IOError:
            print("Error reading showtimes file.")
            return None
        
def view_bookings(name):
    try: 
        with open(BOOK, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if name == data[0]:
                    print(f"\nName: {name} \nMovie: {data[1]} \nShowtime: {data[2]} \nPayment Amount: {data[3]}")
                else:
                    print("No Bookings to display! ")
            print()
    except IOError:
        print("Error reading bookings file file.")
    return None

def conf_book(user, movie, showtime):
    price = 9.99
    print("Your confirmation")
    print(f"User: {user}")
    print(f"Movie: {movie}")
    print(f"Showtime: {showtime}")
    print(f"Price: {price} AED")
    
    try:
        with open(BOOK, "a") as file:
            file.write(f"{user},{movie},{showtime},{price}\n")
    except IOError:
        print("Error writing to bookings file.")

def movies():
    view_movies()
