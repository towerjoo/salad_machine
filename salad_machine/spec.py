# Only 2 levels for testing
import random
FRUITS = [
    {
        "id" : 0,
        "name" : "Apple",
    },
    {
        "id" : 1,
        "name" : "Pear",
    },
    {
        "id" : 2,
        "name" : "Orange",
    },
    {
        "id" : 3,
        "name" : "Tomato",
    },
    {
        "id" : 4,
        "name" : "Banana",
    },
    {
        "id" : 5,
        "name" : "Watermelon",
    },
]
SPECS = [
    [
        {
            "fruit_id" : 0,
            "include_rate" : 0.3,
            "min_qty" : 2,
            "max_qty" : 5,
        },
        {
            "fruit_id" : 1,
            "include_rate" : 0.4,
            "min_qty" : 1,
            "max_qty" : 6,
        },
        {
            "fruit_id" : 2,
            "include_rate" : 0.2,
            "min_qty" : 3,
            "max_qty" : 9,
        },
    ],
    [
        {
            "fruit_id" : 3,
            "include_rate" : 0.1,
            "min_qty" : 2,
            "max_qty" : 5,
        },
        {
            "fruit_id" : 4,
            "include_rate" : 0.4,
            "min_qty" : 1,
            "max_qty" : 6,
        },
        {
            "fruit_id" : 5,
            "include_rate" : 0.6,
            "min_qty" : 3,
            "max_qty" : 9,
        },
    ],
]
def get_fruit_info_from_id(fid):
    if fid < 0 or fid >= len(FRUITS):
        return None
    return FRUITS[fid]

def get_random_basket(level):
    if level < 0 or level >= len(SPECS):
        return None
    candidates = SPECS[level]
    fruits_num = random.randint(1, len(candidates) -1)
    fruits = random.sample(candidates, fruits_num)
    for f in fruits:
        f.update({
            "name" : get_fruit_info_from_id(f.get("fruit_id")).get("name"),
            })
    return fruits


