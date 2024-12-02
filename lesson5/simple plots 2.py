import plotly.express as px

if __name__ == "__main__":
    stats: dict[str, int] = {}
    with open('../lesson4/failslesson4/test_100k.csv',"r") as file:
        next(file)
        stats = {
            "UNAVAILABLE": 0
        }
        for line in file:
            ship_type = line.split(';')[10]

            if ship_type == '"UNKNOWN"' or ship_type == '"UNDEFINED"':
                stats["UNAVAILABLE"] += 1
            elif ship_type in stats:
                stats[ship_type] += 1
            else:
                stats[ship_type] = 1

        ship_sum = sum(stats.values())
        for key, values in stats.items():
            ship_percent = round(values/ ship_sum * 100, 2)
            ship_percent = str(ship_percent) + "%"
            amount = "Total " + str(values) + " ships"
            # print(f"{key.rjust(25)}{ship_percent.rjust(15)}\t\t\t{amount.ljust(20)}")

    stats = dict(sorted(stats.items(), key=lambda ship: ship[1], reverse=True))
    print(stats)
    ship_in_percent = []
    for key, values in stats.items():
        ship_percent = round(values / ship_sum * 100, 2)
        ship_in_percent.append(ship_percent)
    fig = px.bar(x=stats.keys(), y=ship_in_percent)
    fig.show()
