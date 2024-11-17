with open('failslesson4/test_100k.csv', 'r') as fail:
    lines = fail.readlines()
    ships_types = []
    for line in lines:
        split_line = line.split(";")
        ships_types.append(split_line[10])

#print(ships_types)

ships_types_count = {}

for ship in ships_types:
    if ship not in ships_types_count:
        ships_types_count[ship] = 1
    else:
        ships_types_count[ship] = ships_types_count[ship] + 1

for ship_type in ships_types_count:
    print(f"{ship_type}: {ships_types_count[ship_type]}")
