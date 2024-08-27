spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    new_list = []
    for spicy_food in spicy_foods:
        new_list.append(spicy_food['name'])
    return new_list


def get_spiciest_foods(spicy_foods):
    new_list = []
    for i in range(0,len(spicy_foods)):
        if spicy_foods[i]["heat_level"] > 5:
            new_list.append(spicy_foods[i])
    return new_list

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {'🌶'*spicy_food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in range(0,len(spicy_foods)):
        if spicy_foods[i]["cuisine"] == cuisine:
            return spicy_foods[i]

def print_spiciest_foods(spicy_foods):
    new_list = get_spiciest_foods(spicy_foods)
    print_spicy_foods(new_list)


def get_average_heat_level(spicy_foods):
    total = 0
    for item in spicy_foods:
        total = total + item["heat_level"]
    return total/len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

# food = {'name': 'Griot',
#          'cuisine': 'Haitian',
#          'heat_level': 10,}

# # print(create_spicy_food(spicy_foods, {'name': 'Griot',
# #         'cuisine': 'Haitian',
# #         'heat_level': 10,}))

# #print(food)
# #print(spicy_foods)
# print(create_spicy_food(spicy_foods,food))
