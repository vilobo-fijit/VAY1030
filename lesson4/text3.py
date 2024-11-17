def read_conclusion():
    print("\n\nStart reading motivation\n========================================")

    with open('failslesson4/file_1_motivation.txt', 'r') as file:
        for line in file:
            if not line.startswith("Conclusion"):
                pass
            else:
                print(line)
                break

        for line in file:
            print(line)

    print("=========================================\n\nEnd reading motivation\n")

read_conclusion()