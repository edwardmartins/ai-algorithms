from id3 import *

def separator():
    return '########################################################'

def menu():

    title = separator() + '\nID3 - Algorithm\n' + separator()
    print(title)
    print('1) Mostrar tabla')
    print('2) Aplicar algoritmo')
    print('3) Salir de la aplicacion')
    separator()
    return int(input("Por favor introduce una opcion: "))
  

def main():
    table = read_data()
    option = menu()

    while(option != 3):
        if option == 1:
            print(separator())
            print(table)
            print(separator())
            input("Presiona enter para continuar...")
        elif option == 2:
            tree = build_tree(table)
            print(separator())
            pprint.pprint(tree)
            print(separator())
            input("Presiona enter para continuar...")
        option = menu()


main()