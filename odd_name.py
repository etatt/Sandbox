'''Eriq Tatti'''

def main():
    name = get_name()

    letters = format_name(name)

    print(letters)


def format_name(name):
    for char in name:
        letters = name[1::2]
    return letters


def get_name():
    name = input("please enter your name: ")
    while name == "":
        print("invalid name!!!!!!!!")
        name = input("please enter your name: ")
    return name


main()