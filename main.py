# (5 points): As a developer, I want to make at least three commits with descriptive messages.

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists.

# (5 points): As a user, I want a destination to be randomly selected for my day trip.

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# (10 points): As a user, I want to display my completed trip in the console.

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

def user_destination( )

destination = ["Chicago", "Miami", "Dallas", "New Orleans", "Orlando", "New Jersey", "St. Louis", "Los Angeles", "New York", "Atlanta"]
import random
print(random.choice(destination))

def user_restaurant()

restaurant = {"Italian", "Mexican", "Soul Food", "Chinese", "BBQ", "New Orleans food", "Chain restaurant"}

def user_transportation()

transportation = ["Car Rental", "Train", "Bike", "Ride Share App"]
print(random.choice(transportation))

def user_entertainment()

entertainment = ["Comedy Show", "Musical Perfomance", "Tourist Attractions", "Conventions", "Amusement Park"]
print(random.choice(entertainment))