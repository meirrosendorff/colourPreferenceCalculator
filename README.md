# Colour Preference Calculator
Given a set of users and their colour preference we calculate the top colour choice.

## Requirements 
- Python
- File containing a tab seperated list of users in the format 
`{USER_ID}\t{USER_NAME}`
- File containing a space seperated list of user votes in the format  
`{USER_ID} {COLOUR_CHOICE}`
- A deep yearning to know what your users' favourite colour is.

## Running 
```
python3 main.py --favourites_file {FAVOURITES_FILE} --user_file {USERS_FILE}
```

eg:

```
python3 main.py --favourites_file data/favourites.txt --user_file data/users.txt
```

## Discussion on Language Choice

### Advantages
Python has strong built in data processing capabilities leading to quick and easy implementation for the given problem.

### Disadvantages
Python being not strongly typed or compiled means that it is a lot easier to make mistakes and when these mistakes are made they are alot harder to pickup as you do not have a compiler checking things over for you. These issues can be mitigated by adding types and using a good IDE but they cannot be completly removed.

### Reasoning 
Python was chosen for a few reasons, the task involved reading a given file, iterating over its lines and interpreting that data. These data processing tasks are very straight forward in Python and I am familiar with how to implement them. 

### Optimizations
- The set of users was stored in a map which mapped `user_id -> User`, this allowed for constant time lookup of a user given the ID. 
- The favorite votes where counted by grouping the user ids by choice, this meant that once all items had been grouped we simply had to take the largest group, rather than having to go re-lookup the users after the votes had been counted. 

## Discussion 
Given more time (and the ability to hit up google for some ideas) it would be very interesting to explore this idea of favourite colour further. It would be fascinating to see if rather than taking the naive approach and counting the number of votes per colour, we attempted to convert the colours to numerical values and apply some kind of clustering, like a weighted k-means clustering, and saw where the cluster centres turned out. We could then treat these centres as the favourite colour. It may be that `Thistle` is the most voted for colour but when you group all the users that voted for 'purple like' colours you find that the average favorite colour is actually slightly different. 