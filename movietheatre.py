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
    pass

def search():
    choices = []
    for i in movies:
        choices.append(i)
    selection = choicebox("Select a movie to see details: ", "Search Movies", choices)
    
    for key, value in movies.items():
        genre = "Genre : " + str(value['Genre'])
        duration = "Duration : " + str(value['Duration'])
        showtime = "Showtime : " + str(value['Showtime'])
        tickets_sold = "Tickets sold (150 max) : " + str(value['Tickets sold'])

    msg = (genre, "\n", duration, "\n", showtime, "\n", tickets_sold)

    msgbox(msg, "Search Movies")

def add_movies():
    pass

def check_exists():
    pass

def edit():
    pass

# Main Menu
menu()