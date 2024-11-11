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