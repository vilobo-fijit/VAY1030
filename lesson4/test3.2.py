def read_conclusion():
    print("\n\nStart reading motivation\n========================================")

    with open('../lesson 7/failslesson4/file_1_motivation.txt', 'r') as file:
        for line in file:
            if not line.startswith("7. Future-Proofing Skills"):
                pass
            else:
                print(line)
                break

        for line in file:
            print(line)

    print("=========================================\n\nEnd reading motivation\n")

read_conclusion()