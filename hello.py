# Ask the user to enter their
def greet_user():
    # function input() asks input from console
    firstname = input("Please enter your firstname: ")
    lastname = input("Please enter your lastname: ")
    firstname = firstname.capitalize()
    lastname = lastname.capitalize()
    age = int(input("Please enter your age: "))

    userdata = {}
    userdata['firstname'] = firstname
    userdata['lastname'] = lastname
    userdata['age'] = age
    return userdata

    # Print the greeting message with custom name
    #print(f"Hello, I am {firstname} {lastname}! My age is {age}.")
if __name__ == '__main__':
    userdatalist = []

    for x in range(5):
        userdatalist.append(greet_user())

    print(userdatalist)