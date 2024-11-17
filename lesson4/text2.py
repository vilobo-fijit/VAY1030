if __name__ == '__main__':
    with open('failslesson4/file_1_motivation.txt', 'r') as file:
        for line in file:
            print(line.strip())  # `.strip()` removes leading/trailing whitespace.
    print("\n\nStart parsing CSV AIS data")
    with open('failslesson4/ais_data.csv', 'r') as file:
        lines = file.readlines()
        # `lines` is a list where each element is a line from the file.
        # print(lines)
        for line in lines:
            print(line)  # `lines` is a list where each element is a line from the file.
