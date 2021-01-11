
def ask_age():
    age = 0
    while age == 0:
        try:
            age = int(input("Please enter your age : "))
        except:
            print("I need a integer please !")
    return age


def ask_name():
    name = ""
    while name == "":
        name = input("Please enter your name : ")
        if name == "":
            print("You give me nothing ! please retry")
    return name


name = ask_name()
age = ask_age()

print("Hello " + name + " ! You have " + str(age) + " years old.")

