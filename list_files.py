def main():
    import os

    print("The files / folders in {} are:".format(os.getcwd()))
    items = os.listdir('.')
    for item in items:
        print(item)

main()
