def motivation_read():
    file = open('../lesson 7/failslesson4/file_1_motivation.txt', 'r')
    for line in file:
            print(line.strip())
    file.close()

if __name__ == '__main__':
    motivation_read()