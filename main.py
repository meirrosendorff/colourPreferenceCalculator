
import argparse

from utils.favourite_calculator import FavouriteCalculator

def sort_user_list(user_list):
    def sort_criteria(user):
        return user.name

    user_list.sort(key=sort_criteria)

def print_result(favourite_colour, users):
    print(f"Favourite colour: {favourite_colour}")
    print(f"Users who voted for {favourite_colour}:")

    for user in users:
        print(f"\t- {user.id}\t:\t{user.name}")

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user_file")
    parser.add_argument("--favourites_file")

    args = parser.parse_args()

    return args.user_file, args.favourites_file

if __name__ == "__main__":

    user_file, favourites_file = parse_arguments()

    calculator = FavouriteCalculator(user_file, favourites_file)

    favourite_colour, user_list = calculator.calculate_favourite_colour(calculator.users, calculator.favourite_choices)
    sort_user_list(user_list)
    print_result(favourite_colour, user_list)