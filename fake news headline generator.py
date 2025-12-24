import random

subjects = [
    "Virat Kohli",
    "Rohit Sharma",
    "Chandra Babu",
    "Jagan",
    "Crocodile",
    "Elephant",
    "Monkey"
]

actions = [
    "is dancing",
    "is an athlete",
    "is fighting for coconut",
    "is flying in the air",
    "runs 1000 km per second",
    "plays tennis well",
    "is a singer"
]

places = [
    "at Markapur center",
    "in Pacific Ocean",
    "in desert",
    "in basketball court",
    "in bathroom",
    "on the water"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"Breaking News: {subject} {action} {place}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()

    if user_input == "no":
        print("\nThanks for using, hope you enjoyed")
        break
