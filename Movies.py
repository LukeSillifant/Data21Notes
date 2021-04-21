age_check = True
name_check = True

while name_check:
    name = input("Please enter your name: ")
    if (type(name) == str) & name.isalpha():
        print("Success!")
        name_check = False
    else:
        print(f"\"{name}\" is not a valid answer, try again")


while age_check:
    age = input("Please enter your age in years: ")
    if age.isdigit():
        age = int(age)
        if 5 < age < 120:
            print("Success!")
            age_check = False
        else:
            print(f" Your age of \"{age}\" is not possible, try again")
    else:
        print(f"\"{age}\" is not a valid answer, try again")

movies = {
    "U": ["Lion King", "12 Angry Men", "WALL-E"],
    "PG": ["Monster House", "Toy Story", "How to Train your Dragon"],
    "12": ["The Dark Knight", "Inception", "Avatar"],
    "15": ["The Shawshank Redemption", "The Godfather", "The Matrix"],
    "18": ["Pulp Fiction", "Fight Club", "Goodfellas"]
}
print("I recommend these movies:")
if 5 <= age < 9:
    print(movies["U"][:])
elif 9 <= age < 12:
    print(movies["PG"][:], "\n ", movies["U"][:])
elif 12 <= age < 15:
    print(movies["12"][:], "\n ", movies["PG"][:], "\n ", movies["U"][:])
elif 15 <= age < 18:
    print(movies["15"][:], "\n ", movies["12"][:], "\n ", movies["PG"][:], "\n ", movies["U"][:])
else:
    print(movies["18"][:], "\n ", movies["15"][:], "\n ", movies["12"][:], "\n ", movies["PG"][:], "\n ", movies["U"][:])
