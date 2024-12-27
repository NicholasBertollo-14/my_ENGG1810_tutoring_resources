
print("ND Lists")
# This is for multi-dimensional lists
nicks_list_of_lists: list[list[int]] = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]]

# What is:
print(nicks_list_of_lists[2])
print(nicks_list_of_lists[2][1])
print(nicks_list_of_lists[1])
print(nicks_list_of_lists[1][2])


# f string:
# Think of it like format, but better
name: str = "Nicholas Bertollo"
print(f"Hello my name is {name}")

# enumerate
print(list(enumerate(["a", "b", "c"])))

# Iterating over a list of lists
for list_index, nicks_list in enumerate(nicks_list_of_lists):
    for nicks_item in nicks_list:
        print(nicks_item)
    print(f"Finished printing list {list_index}")

# This is for multi-dimensional dictionaries
sweet_treat_rating: dict[str: int] = {
    "chocolate": 7,
    "biscuits": 10,
    "lollies": 8
}
dinner_rating: dict[str: int] = {
    "dal": 10,
    "pizza": 9,
    "pasta": 8
}
food_ratings: dict[str: dict[str: int]] = {
    "sweet_treat": sweet_treat_rating,
    "dinner": dinner_rating
}

print(f"{food_ratings['sweet_treat']['lollies']=}")
print(f"{food_ratings['dinner']['dal']=}")

# Therefore to get a list of (food, rating) pairs
# [(0, dict_1), (1, dict_2), ...]
for dictionary_index, food_rating in enumerate(food_ratings.values()):
    for food_and_rating in food_rating.items():
        print(food_and_rating)
    print(f"Finished printing dictionary {dictionary_index}")

