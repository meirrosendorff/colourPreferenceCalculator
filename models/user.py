USER_DATA_DELIMETER = "\t"
EXPECTED_USER_DETAILS_LENGTH = 2
ID_INDEX = 0
NAME_INDEX = 1

class User:
    def __init__(self, user_line):
        user_details = user_line.strip().split(USER_DATA_DELIMETER)
        if len(user_details) < EXPECTED_USER_DETAILS_LENGTH:
            raise ValueError(f"Invalid user value line provided: {user_line}, skipping")
        
        self.id = user_details[ID_INDEX]
        self.name = user_details[NAME_INDEX]