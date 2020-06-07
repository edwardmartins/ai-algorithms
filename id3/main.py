from id3 import *

def separator():
    return '########################################################'

def menu():

    title = separator() + '\nID3 - Algorithm\n' + separator()
    print(title)
    print('1) Show the data')
    print('2) Apply ID3')
    print('3) Exit')
    separator()
    return int(input("Please choose an option: "))
  

def main():
    table = read_data()
    option = menu()

    while(option != 3):
        if option == 1:
            print(separator())
            print(table)
            print(separator())
            input("Press enter to continue...")
        elif option == 2:
            tree = build_tree(table)
            print(separator())
            pprint.pprint(tree)
            print(separator())
            input("Press enter to continue...")
        option = menu()


if __name__ == "__main__":
    main()