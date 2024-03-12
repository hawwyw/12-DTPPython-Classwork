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
        "Change tickets sold": tickets_sold

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

def tickets_sold():
    movie = choicebox("What movie do you want to sell more tickets for", "Change tickets sold", movies)
    max_tickets = 150 - movies[movie]["Tickets sold"]
    new_time = integerbox(f"Enter how many more tickets have been sold - max tickets per cinema is 150 - the previous amount, which is {max_tickets}", "Change time", lowerbound = 1, upperbound = max_tickets)
    movies[movie]["Showtime"] = new_time

    temp = [f"\n\n***{movie} Details***\n\n"]
    for key, details in movies[movie].items():
        temp.append(str(key) +  " : " + str(details) + "\n")
        print(temp)
    msgbox(temp)


menu()