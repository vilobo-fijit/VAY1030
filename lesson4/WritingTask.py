def get_name_and_age():
    name = input("What your name: ")
    age = input("What your age: ")
    return name, age

def save(fail):
    name, age = get_name_and_age()
    if name.lower() == "stop" or age.lower() == "stop":
        return False
    fail.write(f"{name},{age}\n")

with open('../lesson 7/failslesson4/students.csv', 'a') as fail:
    while True:
        if save(fail) == False:
            break
