# Description: This script prints a numbered, ranked list of favorite
#              foods using enumerate(), and flags the top pick
# Author: Richard Elmorry

favorite_foods = ["pizza", "tacos", "sushi", "wings", "pasta"]

for index, food in enumerate(favorite_foods, start=1):
    if index == 1:
        print(f"{index}. {food} <- top pick!")
    else:
        print(f"{index}. {food}")