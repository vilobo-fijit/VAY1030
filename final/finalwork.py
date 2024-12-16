

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
