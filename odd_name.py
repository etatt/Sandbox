'''Eriq '' Tatti'''

def main():
    name = input("please enter your name :")

    while name == "":
        print("invalid name!!!!!!!!")
        name = input("please enter your name :")

    for char in range (len(name)):
        print("{}".format(name[::2]), end=". ")

main()