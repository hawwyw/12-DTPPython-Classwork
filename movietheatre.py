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
        "Add movies": add_movies,
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
    out_string = ""
    for key in movies:
        print(key)
        temp = f"{key}: Genre : {movies[key]['Genre']}, Duration : {movies[key]['Duration']}, Showtime : {movies[key]['Showtime']}, Tickets sold : {movies[key]['Tickets sold']}\n"

        out_string += temp
    
    msgbox(out_string)

def search():
    choices = []
    for i in movies:
        choices.append(i)
    selection = choicebox("Select a movie to see details: ", "Search Movies", choices)
    
    genre = movies[selection]['Genre']
    duration = movies[selection]['Duration']
    showtime = movies[selection]['Showtime']
    tickets_sold = movies[selection]['Tickets sold']

    msg = ("Genre : ", genre, "\n", "Duration : ", duration, "\n", "Showtime : ", showtime, "\n", "Tickets sold : ", tickets_sold)

    msgbox(msg, "Search Movies")

def add_movies():
    movie = enterbox("What movie do you want to add? : ")
    if movie in movies:
        sure = choicebox("Movie already being shown - do you want to change details?", "Movie Theatre", choices = ("Yes", "No"))
        if sure == "Yes":
            edit()
        else:
            msgbox("No details changed.")
    else:
        msg = "Please fill out movie details below: "
        title = "Movie Theatre"
        field_names = ["Genre : ", "Duration : ", "Showtime : ", "Tickets sold : "]
        field_values = []
        field_values = multenterbox(msg,title, field_names)


def edit():
    pass

# Main Menu
menu()