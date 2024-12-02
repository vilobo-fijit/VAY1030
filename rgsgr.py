def process_ais_data(filename: str, ship_type: str):
    stats: dict[str, int] = {}
    with open(filename, "r") as file:
        next(file)
        stats = {}
        for line in file:
            if line.split(";")[10] == ship_type:
                sog = line.split(";")[8]
                if sog in stats.keys():
                    stats[sog] += 1
                else:
                    stats[sog] = 1

    stats = dict(sorted(stats.items(), key=lambda ship: ship[1], reverse=True))
    return stats

def print_ship_speeds(stats, limit):
    stats = process_ais_data()
    if len(stats) == limit:
        print("pop")

def print_ship_speeds(stats: dict[float, int], limit: int):
    new_dict = {}
    for key, value in dict.items():
        if value < limit:
            new_dict[key] = value
    print(new_dict)

if __name__ == '__main__':
    print_ship_speeds(process_ais_data('../kontrolltoo/failslesson4/test_100k.csv','"CARGO"'),4)
