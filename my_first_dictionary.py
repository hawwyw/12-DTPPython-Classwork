# Original Dictionary
hogwarts = {
    "Harry Potter": "Gryfindor",
    "Ron Weasly": "Gryfindor",
    "Hermione Granger": "Gryfindor"
}

print(hogwarts.keys())
# Adds individual items to dictionary
hogwarts ["Draco Malfoy"] = "Slytherin"
# Will also change value if the name is already in dictionary
# Dictionary - Key - Value
hogwarts ["Cedric Diggery"] = "Hufflepuff"
hogwarts ["Cho Chang"] = "Ravenclaw"
# New dictionary
Teachers = {
    "Albus Dumbledore": "Gryfindor"
}
# Adds new dictionary to og one
hogwarts.update(Teachers)

print(hogwarts)
# Prints out the pair to what the name was
person = input("Person: ")
print(hogwarts[person])

student = input("Student: ")
house = input("House: ")
hogwarts [student] = house
print(hogwarts)