from easygui import *

movies  = {
    "The Shawshank Redemption": {"Genre": "Drama", "Duration": 142, "Showtime": 2200, "Tickets sold": 143},
    "The Godfather": {"Genre": "Drama", "Duration": 175, "Showtime": 1530, "Tickets sold": 111},
    "Back to the future": {"Genre": "Comedy", "Duration": 116, "Showtime": 1200, "Tickets sold": 102},
    "Spirited away": {"Genre": "Family", "Duration": 125, "Showtime": 930, "Tickets sold": 98},
    "The Lion King": {"Genre": "Family", "Duration": 88, "Showtime": 700, "Tickets sold": 123},
}

def menu():
    options = {
        "Add movie": add_movies,
        "Find movie showing": search,
        "Update": edit,
        "List movies": print_dict,
        "Exit": leave
    }

    get_input = True

    while get_input != None:

        msg = "What u wanna do?"
        title = "Movie theatre"
        choices = []
        for i in options:
            choices.append(i)
        
        selection = buttonbox(msg, title, choices)

        get_input = options[selection]()

def leave():
    return None

def print_dict():
    output = ["\n\n***Movie Details***\n\n"]
    for movie, details in movies.items():
        output.append(f"\nMovie: {movie}\n")
        for key, value in details.items():
            output.append(f"\t{key}: {value}")
        
    msgbox("\n".join(output))



def search():
    choices = []
    for i in movies:
        choices.append(i)
    selection = choicebox("Select a movie to see details: ", "Search Movies", choices)
    
    details = movies[selection]
    output = [f"\n\n***Movie Details***\n\n{selection}\n"]
    for key, value in details.items():
        output.append(f"\t{key}: {value}")
    msg = ("\n".join(output))

    msgbox(msg, "Search Movies")
    return True

def add_movies():
    movie = enterbox("What movie do you wish to add?")
    if movie in movies:
        sure = buttonbox(f"{movie} is already scheduled to show. Do you wish to change the details?", "Movie already showing", choices = ("Yes", "No"))
        if sure == "Yes":
            edit()
            return True
        else:
            msgbox("Nothing changed", "Movie Theatre")
    else:
        running = True
        input_list = ["Genre", "Duration", "Showtime ( 24 hour time, EG 900 for 9 am or 1500 or 3pm", "Tickets sold(150 max)"]
        while running:
            user_in = multenterbox("Enter movie details", "Movie details", input_list)
            running = False
            if not user_in:
                msgbox("Enter something", "Error")
                user_in = []
                running = True

            if "" in user_in:
                msgbox("Enter something", "Error")
                user_in = []
                running = True
            
            if not user_in[3].isdigit() or not user_in[2].isdigit() or not user_in[1].isdigit():
                msgbox("Enter number for 2, 3, 4", "Error")
                user_in = []
                running = True

            if int(user_in[3]) > 150 or int(user_in[3]) < 0:
                msgbox("Enter number between 0 and 150 for tickets sold", "Error")
                user_in = []
                running = True

            if int(user_in[1]) <= 0:
                msgbox("Enter a time above 0 for tickets sold", "Error")
                user_in = []
                running = True
            
            if int(user_in[2]) > 2400 or int(user_in[2]) < 0:
                msgbox("Enter number between 0 and 2400 for time", "Error")
                user_in = []
                running = True


        temp = {
            "Genre": user_in[0],
            "Duration": int(user_in[1]),
            "Showtime": int(user_in[2]),
            "Tickets sold": int(user_in[3])
        }

        movies[movie] = temp

        print_dict()
        return True

def edit():
    movie = choicebox("What movie do you wish to edit?", "Edit details", movies)
    running = True
    while running:
        change = buttonbox("What part of the movie do you wish to change?", "Edit details", choices = ("Genre", "Duration", "Showtime", "Tickets sold", "Nothing, I'm done editing movies"))
        if change == "Nothing, I'm done editing movies":
            output = [f"\n\n***Movie Details***\n\n{movie}\n"]
            for key, value in movies[movie].items():
                output.append(f"\t{key}: {value}")
            msg = ("\n".join(output))

            msgbox(msg, "Search Movies")
            return True
        else:
            running1 = True
            while running1:
                temp = enterbox(f"Enter the new details for {change}", "Update details")
                running1 = False
                if change != "Genre" and not temp.isdigit():
                    msgbox("Enter a number", "Error")
                    running1 = True
                
                if change == None:
                    False
                



            movies[movie][change] = temp
            

# Main Menu
menu()