MOVIES = "server2/movies.txt"

def add_movie(movie_data):
    try:
        with open(MOVIES, "a") as file:
            file.write(movie_data)
        print("Movie added successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def remove_movie(movie_name):
    try:
        with open(MOVIES, "r") as file:
            movies = file.readlines()
        
        with open(MOVIES, "w") as file:
            for movie in movies:
                if not movie.startswith(movie_name):
                    file.write(movie)
        print(f"{movie_name} removed successfully.")
    except Exception as e:
        print(f"Error removing movie: {e}")

def manage_movies():
    # Admin can add or remove movies
    user_input = input("Add(1) or Remove(2): ")
    if user_input == '1':
        movie_data = input("Enter movie details (Title, Genre, Duration, Rating, Showtimes): ")
        add_movie(movie_data)
    elif user_input == '2':
        movie_name = input("Enter the movie name to remove: ")
        remove_movie(movie_name)
    else:
        print("Invalid selection.")
    
def view_movies():
    try:
        with open(MOVIES, "r") as file:
            movies = [line.strip().split(',') for line in file]
        
        print(f"{'Movie':<40} {'Genre':<15} {'Duration':<10} {'Rating':<10}")
        for movie in movies:
            print(f"{movie[0]:<40} {movie[1]:<15} {movie[2]:<10} {movie[3]:<10}")
    except IOError:
        print("Error reading movie file.")
