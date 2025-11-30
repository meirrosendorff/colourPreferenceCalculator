FAVOURITE_DATA_DELIMETER = " "
EXPECTED_FAVOURITE_LENGTH = 2
ID_INDEX = 0
FAVOURITE_INDEX = 1

class FavouriteChoice:
    def __init__(self, data_line):
        data = data_line.strip().split(FAVOURITE_DATA_DELIMETER)
        if len(data) < EXPECTED_FAVOURITE_LENGTH:
            raise f"Invalid favourite line provided: {data_line}, skipping"

        self.user_id = data[ID_INDEX]
        self.colour = data[FAVOURITE_INDEX]