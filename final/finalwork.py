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
    print(f"To"
          f"tal of yout group is {total}")


"task 4"
def task4_calculate_population_stats(filename:str, group: int):
    with open(filename, "r") as file:
        age_group = next(file).split(",")[group]
        ages_list = []
        for line in file:
            ages_list.append(int(line.split(",")[group]))
        average = round(np.average(ages_list), 2)
        median = round(np.median(ages_list), 2)
    print(f"In age group of {age_group} the median is {median} and average is {average}")

task4_calculate_population_stats("population_by_age_group.csv", 4)

