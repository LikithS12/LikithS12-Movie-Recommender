#imports the ability to randomize
import random

#makes lists and then creates variables to randomize list
print("Movie Rater")
g_movies = ["Toy Story", "Monsters inc.", "Wall-E", "Cars"]
g_random = random.choice(g_movies)

pg_movies = ["Despicable Me", "Inside Out 2", "Wonka", "Kung Fu panda"]
pg_random = random.choice(pg_movies)

pg_13_movies = ["Twisters", "Interstellar", "Batman", "Dune"]
pg13_random = random.choice(pg_13_movies)

r_movies = ["Joker", "Deadpool", "Gladiator", "Oppenheimer"]
r_random = random.choice(r_movies)

user_age = int(input("What is your age: "))
#.lower() allows the input to be all lowercase
adult = input("Are you watching with someone(Yes/No): ").lower()

if adult == "yes":
    adult_age = int(input("What is the age of the person you are watching with: "))


#This if/elif/else statement uses the user and parent age to reccomend
    if user_age < 13:
        print("The best movies for your age are in the PG category!")
        print("You should watch" + " " + pg_random)
        if adult_age > 20:
            print("You can watch PG-13 movies with an adult!")
            print("You should watch" + " " + pg13_random)
    elif 13 <= user_age < 17:
        print("The best movies for your age are in the PG-13 category!")
        print("You should watch" + " " + pg13_random)
        if adult_age > 20:
            print("You can watch R-category movies with an adult!")
            print("You should watch" + " " + r_random)
    elif user_age >= 17:
        print("The best movies for your age group are in the R category!")
        print("You should watch" + " " + r_random)
else:
    if user_age < 13:
        print("The best movies for your age are in the G category!")
        print("You should watch" + " " + g_random)
    elif 13 <= user_age < 17:
        print("The best movies for your age are in the PG-13 category!")
        print("You should watch" + " " + pg13_random)
    elif user_age >= 17:
        print("The best movies for your age group are in the R category!")
        print("You should watch" + " " + r_random)
