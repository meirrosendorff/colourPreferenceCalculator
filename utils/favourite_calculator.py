from models.favourite_choice import FavouriteChoice
from models.user import User


class FavouriteCalculator:
    def __init__(self, users_file, favourites_file):
        self.users = self._read_users(users_file)
        self.favourite_choices = self._read_favourite_choices(favourites_file)

    def _read_users(self, user_file_name):
        user_map = {}

        with open(user_file_name, 'r') as user_file:
            for line in user_file:
                try:
                    user = User(line)
                    user_map[user.id] = user
                except ValueError as e:
                    print(e)

        return user_map
    
    def _read_favourite_choices(self, favourite_file_name):
        favourites_map = {}
        with open(favourite_file_name, 'r') as favourites_file:
            for line in favourites_file:
                try:
                    choice = FavouriteChoice(line)

                    if choice.colour not in favourites_map:
                        favourites_map[choice.colour] = []

                    favourites_map[choice.colour].append(choice.user_id)
                except ValueError as e:
                    print(e)

        return favourites_map

    def calculate_favourite_colour(self, user_map, favourites_map):
        favourite_colour = None
        max_votes = -1

        for colour, user_ids in favourites_map.items():
            if len(user_ids) > max_votes:
                max_votes = len(user_ids)
                favourite_colour = colour

        user_list = []
        for user_id in favourites_map[favourite_colour]:
            if user_id not in user_map:
                print(f"User id {user_id} voted but not found, skipping")
                continue
            user_list.append(user_map.get(user_id))

        return favourite_colour, user_list