month_dict = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

month_dict_list = [
    {'January': 1},
    {'February': 2},
    {'March': 3},
    {'April': 4},
    {'May': 5},
    {'June': 6},
    {'July': 7},
    {'August': 8},
    {'September': 9},
    {'October': 10},
    {'November': 11},
    {'December': 12}
]


def create_big_dict(old_dict):
    dict_keys = []
    dict_values = []
    for key, value in old_dict.items():
        dict_keys.append(key)
        dict_values.append(value)
    new_dict = {tuple(dict_keys): tuple(dict_values)}
    return new_dict


print(create_big_dict(month_dict))
