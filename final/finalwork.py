import numpy as np

"task 1"
def task1_check_age(age:int) -> str:
    if age < 18:
        return "you are too young"
    else:
        return "welcome"


"task 2"
def task2_normalize_name(name: str) -> str:
    cap_name = ""
    for sub_name in name.split(" "):
        cap_name += sub_name.capitalize() + " "
    cap_name = cap_name[:-1]
    return cap_name


"task 3"
def task3_read_population(filename:str, group:int):
    with open(filename, "r") as file:
        next(file)
        data = {}
        total = 0

        for line in file:
            country = line.split(",")
            data[country[0]] = int(country[group])
            total += int(country[group])
    print(data)
    print(f"Total of yout group is {total}")