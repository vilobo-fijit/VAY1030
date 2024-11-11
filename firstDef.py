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