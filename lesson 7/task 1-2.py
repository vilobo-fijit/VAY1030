import csv


def read_file():
    with open('../lesson 7/failslesson4/test_10k.csv', 'r') as file, open('../lesson 7/failslesson4/students.csv', 'w') as file_output:
        next(file)
        lines: list[str] = file.readlines()
        for line in lines:
            #tokens = line.split(',')

            #mmsi = tokens[4]
            #shiptype = tokens[10]
            #lat = tokens[5]
            #long = tokens[6]
            #sog = tokens[8]


            mmsi = line.split(';')[4]
            shiptype = line.split(';')[10]
            lat = line.split(';')[5]
            long = line.split(';')[6]
            sog = line.split(';')[8]
            file_output.write(f"{mmsi},{shiptype},{lat},{long},{sog}\n")




if __name__ == '__main__':
    read_file()

