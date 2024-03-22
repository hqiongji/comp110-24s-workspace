"""Some functions for my garden plan!"""
    
__author__: str = "730520183"

by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
# print(by_kind["flower"])

# only want to print zinnia by using index 
# print(by_kind["flower"][1])

# if "flower" is already in by_kind, want also add "daisy" in by_kind flowers 
# new_plant: str = "daisy"
# new_plant_kind: str = "flower"


def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str):
    """Add by kind."""
# if "flower" is already in by_kind, want also add "daisy" in by_kind flowers 2
    if new_plant_kind in by_kind:
        by_kind[new_plant_kind].append(new_plant)
    else:
        by_kind[new_plant_kind] = []
        by_kind[new_plant_kind].append(new_plant)
# if we are using this definition, we do not need to type what is new plant and what is new plant type and insert it in the dict.


# because the value is a list, so it can append
# by_kind[new_plant_kind].append(new_plant)
# print(by_kind)

# if the kind is not in dictionary (like fruit is not in the dictionary)
# new_fruit: str = "berry"
# new_fruit_kind: str = "fruit"
# by_kind[new_fruit_kind] = [] 
# by_kind[new_fruit_kind].append(new_fruit)
# print(by_kind)


def add_by_date(garden_by_date: dict[str, list[str]], month: str, plant: str):
    """Add by date."""
    if month in garden_by_date:
        garden_by_date[month].append(plant)
    else:
        garden_by_date[month] = []
        garden_by_date[month].append(plant)
# Function name: lookup_by_kind_and_date
# Parameters: dict[str, list[str]], dict[str, list[str]], str, str
# Return Type: str


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], kind: str, month: str) -> str:
    """Look up what kind of this plant and what date it been planted."""
    assert kind in plants_by_kind
    assert month in plants_by_date
    # Get a list of all plants to specific kind input 
    kind_list: list[str] = plants_by_kind[kind]
    month_list: list[str] = plants_by_date[month]
    combined_list: list[str] = []
    # Go through every elements appear in both 
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant:  # plant is in both month and kind list
                combined_list.append(other_plant)
        if len(combined_list) > 0:
            return f"{kind}s to plant in {month}:{combined_list}"
        else:
            return f"No {kind}s to plant in {month}."