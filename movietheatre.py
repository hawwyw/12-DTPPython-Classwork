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
        "Change Tickets Sold": tickets_sold,
        "Exit": leave,
        None: leave
    }

    get_input = True

    while get_input != None:

        msg = "What u wanna do?"
        title = "Movie theatre"
        choices = []
        for i in options:
            choices.append(i)
        choices.remove(i)
        
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
    return True



def search():
    choices = []
    for i in movies:
        choices.append(i)
    selection = choicebox("Select a movie to see details: ", "Search Movies", choices)
    if not selection:
        return True
    
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
<<<<<<< HEAD
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
        else:
            temp = {"Genre": answer[0], "Duration": answer[1], "Showtime": answer[2], "Tickets sold": answer[3]}
            movies[movie] = temp
            
    return True
=======
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

            elif "" in user_in:
                msgbox("Enter something", "Error")
                user_in = []
                running = True
            
            elif not user_in[3].isdigit() or not user_in[2].isdigit() or not user_in[1].isdigit():
                msgbox("Enter number for 2, 3, 4", "Error")
                user_in = []
                running = True

            elif int(user_in[3]) > 150 or int(user_in[3]) < 0:
                msgbox("Enter number between 0 and 150 for tickets sold", "Error")
                user_in = []
                running = True

            elif int(user_in[1]) <= 0:
                msgbox("Enter a time above 0 for tickets sold", "Error")
                user_in = []
                running = True
            
            elif int(user_in[2]) > 2400 or int(user_in[2]) < 0:
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
>>>>>>> cd8ead5b6267e11d3d0f4ef575b28c0ff22d07b9



def edit():
    movie = choicebox("What movie do you wish to edit?", "Edit details", movies)
    if not movie:
        return True

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
        elif not change:
            return True
        else:
            running1 = True
            while running1:
                temp = enterbox(f"Enter the new details for {change}", "Update details")
                running1 = False
                
                if not temp:
                    return True

                if change != "Genre" and not temp.isdigit():
                    msgbox("Enter a number", "Error")
                    running1 = True
                
                if change == "Tickets sold" and int(temp) < 0 or change == "Tickets sold" and int(temp) > 150:
                    running1 = True         


            movies[movie][change] = temp
            
def tickets_sold():
    movie = choicebox("What movie do you want to sell more tickets for", "Change tickets sold", movies)
    if not movie:
        return True
    max_tickets = 150 - movies[movie]["Tickets sold"]
    new_time = integerbox(f"Enter how many more tickets have been sold - max tickets per cinema is 150 - the previous amount, which is {max_tickets}", "Change time", lowerbound = 1, upperbound = max_tickets)
    movies[movie]["Showtime"] = new_time

    output = [f"\n\n***Movie Details***\n\n{movie}\n"]
    for key, value in movies[movie].items():
        output.append(f"\t{key}: {value}")
        msg = ("\n".join(output))
    msgbox(output, "Tickets sold")
    return True

# Main program
menu()