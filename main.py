def ask_for_the_name():
    name = ""
    while name == "":
        print("Please, enter a name : ")
        name = input()
    return name


def ask_for_the_age():
    age = ""
    while age == "":
        print("Please, enter your age : ")
        age = input()

    try:
        age == int(age)
    except:
        print("Your age must be a valid number")

    return age
    

name = ask_for_the_name()
age = ask_for_the_age()

print("Your name is " + name + " and you are " + age + " years old.")
