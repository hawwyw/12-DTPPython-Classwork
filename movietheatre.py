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
        sure = buttonbox("Movie already being shown - do you want to change details?", "Movie Theatre", choices = ("Yes", "No"))
        if sure == "No":
            return True
    msg = "Please fill out movie details below: "
    title = "Movie Theatre"
    field_names = ["Genre : ", "Duration(minutes) : ", "Showtime : ", "Tickets sold : "]
    answer = []
    run = True
    while run:
        answer = multenterbox(msg,title, field_names)
        run = False
        if not answer[3].isdigit() or not answer[2].isdigit() or not answer[1].isdigit():
            msgbox("Enter an integer for duration, showtime and tickets sold - use 24 hour time eg 700 for 7am or 1300 for 1 PM")
            run = True
        elif int(answer[2]) > 2400 or int(answer[2]) < 0:
            msgbox("Enter a number between 0 and 2400.")
            run = True
        elif int(answer[3]) > 150:
            msgbox("Max tickets is 150")
            run = True
    temp = {"Genre": answer[0], "Duration": answer[1], "Showtime": answer[2], "Tickets sold": answer[3]}
    movies[movie] = temp
    return True



def edit():
    pass

# Main program
menu()