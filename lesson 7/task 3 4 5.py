def process_ais_data(filename: str, ship_type: str):
    stats: dict[str, int] = {}
    with open(filename, "r") as file:
        next(file)
        stats = {}
        for line in file:
            if line.split(";")[10][1:-1] == ship_type:
                sog = line.split(";")[8]
                if sog in stats.keys():
                    stats[sog] += 1
                else:
                    stats[sog] = 1

    stats = dict(sorted(stats.items(), key=lambda ship: ship[0], reverse=True))
    print(stats)

if __name__ == '__main__':
    process_ais_data('../lesson 7/failslesson4/test_100k.csv','CARGO')
