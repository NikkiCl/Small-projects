import random
from random import randint
import math
NUM_ROUNDS = 5
def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    score = 0
    for i in range(NUM_ROUNDS):
        i += 1
        random1 = randint(1,100)
        random2 = randint(1,100)
        print(f"Round {i}")
        print(f"Your number is {random1}")
        userIn = input("Do you think your number is higher or lower than the computer's?: ").lower()
        while userIn not in ["lower","higher"]:
            userIn = input("Please enter either higher or lower: ")
        if userIn == "lower" and random2 > random1 or userIn == "higher" and random1 > random2:
            print(f"You were right! The computer's number was {random2}")
            score += 1
        elif userIn == "lower" and random1 > random2 or userIn == "higher" and random2 > random1:
            print(f"Aww, that's incorrect. The computer's number was {random2}")
        elif random1 == random2:
            print(f"Aww, that's incorrect. The computer's number was {random2}")
        print(f"Your score is now {score}\n")
    if score >= NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= math.floor(NUM_ROUNDS / 2):
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    main()