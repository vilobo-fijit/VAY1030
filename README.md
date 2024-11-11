
   # Ask the user to enter their
def greet_user(msg="Please enter your name: "):
    # function input() asks input from console
    name: str = input(msg)
    name = name.capitalize()

    # Print the greeting message with custom name
    print(f"Hello, {name}!")


if __name__ == '__main__':
    greet_user()
    greet_user("Tere, Vika")

    if __name__ == '__main__':
    animals = {
        'Lion': {'name': 'Leo', 'sex': 'Male', 'alias': 'King of the Jungle'},
        'Tiger': {'name': 'Tara', 'sex': 'Female', 'alias': 'The Striped Hunter'},
        'Elephant': {'name': 'Ennyla', 'sex': 'Female', 'alias': 'Mighty Trunk'},
        'Penguin': {'name': 'Penny', 'sex': 'Female', 'alias': 'The Waddler'},
        'Kangaroo': {'name': 'Kenny', 'sex': 'Male', 'alias': 'Jumping Jack'},
        'Dolphin': {'name': 'Danny', 'sex': 'Male', 'alias': 'The Flipper'},
        'Zebra': {'name': 'Zara', 'sex': 'Female', 'alias': 'The Striped Wonder'},
        'Giraffe': {'name': 'Gigi', 'sex': 'Female', 'alias': 'Tall and Graceful'},
        'Bear': {'name': 'Benny', 'sex': 'Male', 'alias': 'The Grizzly'},
        'Monkey': {'name': 'Milo', 'sex': 'Male', 'alias': 'The Playful Primate'}
    }

    # Sort the animals dictionary by the animal name (key)
    sorted_animals = sorted(animals.items())

    # Print the header
    print(f"{'Animal':<12} {'Name':<10} {'Sex':<6} {'Alias':<20}")
    print("-" * 50)

    # Print the sorted rows
    #for animal, details in sorted_animals:
        #print(f"{animal:<12} {details['name']:<10} {details['sex']:<6} {details['alias']:<20}")

    # Print the sorted rows
    #for animal, details in sorted_animals:
        #if details['sex'] == 'Male':  # Check if the animal is male
            #print(f"{animal:<12} {details['name']:<10} {details['sex']:<6} {details['alias']:<20}")

    for animal, details in sorted_animals:
        #if details['name'][-3:] == "nny":
        if details['name'].endswith("nny"):
            print(f"{animal:<12} {details['name']:<10} {details['sex']:<6} {details['alias']:<20}")

    print("-" * 2)
    for animal, details in sorted_animals:
        if "nny" in details['name'] and not details['name'].endswith("nny"):
            print(f"{animal:<12} {details['name']:<10} {details['sex']:<6} {details['alias']:<20}")

def method_name(name, score, staatus):
    print(f"{name.ljust(15)}{score.rjust(8)}{staatus.rjust(10)}")


if __name__ == '__main__':
    names: list[str] = [
        "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivy",
        "Jack", "Katherine", "Liam", "Megan", "Nathan", "Olivia", "Georg", "Mike"
    ]

    exam_results: dict[str, float] = {
        "Alice": 85.5, "Bob": 92.3, "Charlie": 68.9, "David": 88.4, "Eva": 91.2,
        "Frank": 14, "Grace": 95.1, "Hannah": 43.8, "Ivy": 89.6, "Jack": 80.2,
        "Katherine": 90, "Liam": 86.7, "Megan": 57.3, "Nathan": 93.5, "Olivia": 91.8,
        "Vera": 92.7, "Walter": 76.5, "Xander": 85.3, "Yvonne": 77.9, "Zane": 89.0
    }
    #for x in names:
    #    x = x.upper()
    #    print(f"{x}")



    for x in names:
        if exam_results.get(x) :
            if exam_results.get(x) < 50:
                staatus = "Failed"
            else:
                staatus = "Pass"

            score: str = f"{exam_results[x]:0.2f}"
            method_name(x, score, staatus)
        else:
            method_name(x, '--.--', "MISSED")



