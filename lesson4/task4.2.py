from turtledemo.penrose import start

if __name__ == "__main__":
    stats: dict[str, int] = {}
    with open('failslesson4/test_100k.csv',"r") as file:
        next(file)
        stats = {}
        for line in file:
            ship_type = line.split(';')[10]

            if ship_type in stats:
                stats[ship_type] += 1
            else:
                stats[ship_type] = 1

        ship_sum = sum(stats.values())
        for key, values in stats.items():
            ship_percent = str(round(values/ ship_sum * 100, 2)) + " %"
            amount = "Total " + str(values) + " ships"
            print(f"{key.rjust(25)}{ship_percent.rjust(15)}\t\t\t{amount.ljust(20)}")

        # for ship_type in stats:
        #     print(f"{ship_type} - {stats[ship_type]}")