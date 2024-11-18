
def get_name_and_age():
    name = input("What your name: ")
    age = input("What your age: ")
    if name.lower() == "stop" or age.lower() == "stop":
        return  False
    else:
        return name, age

def save(fail):
    result = get_name_and_age()
    if result == False:
        return False
    else:
        name, age = result
        fail.write(f"{name},{age}\n")
        return True


if __name__ == '__main__':
    with open('failslesson4/students.csv', 'a') as fail:
        while True:
            if save(fail) == False:
                break



