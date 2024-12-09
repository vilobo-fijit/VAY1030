def motivation_read():
    fail =  open('../lesson 7/failslesson4/file_1_motivation.txt', 'r')
    for line in fail:
        print(line.strip())
    fail.close()

if __name__ == '__main__':
    motivation_read()
