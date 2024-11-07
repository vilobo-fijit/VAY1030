shopping = {
    "bread": 0,
    "milk": 0,
    "eggs": 0,
    "meat": 0,
    "cat food": 0
}
for key in shopping:
    count = input(f"How many {key} you need: ")
    shopping[key] = count

for key in shopping:
    if shopping[key] != "0" and shopping[key] != "":
     print(f"{key} - {shopping[key]}")
