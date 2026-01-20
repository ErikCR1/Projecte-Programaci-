from funcions import *
import time
def verificador(tamaño, opcion):
    
    if isinstance(opcion, int):
        if opcion <= tamaño:
            return True
        
    return False    


def game(user):
    id_user = buscar_usuario(user)
    ingame = True
    while ingame:

        aventuras = cargar_aventura()
        mostrar_aventura(aventuras)
        op_aventura = input("Elige aventura: ")
        while (verificador(len(aventuras), op_aventura)):
            print("Has introducido una opcion incorrecta")
            op_aventura = input("Elige aventura: ")


        personajes = cargar_personaje()
        mostrar_personaje(personajes)
        op_personaje = input("Elige personaje: ")
        while (verificador(len(aventuras), op_personaje)):
            print("Has introducido una opcion incorrecta")
            op_personaje = input("Elige personaje: ")
        
        insert_partida(id_user[0], op_aventura, op_personaje)

def mostrar_aventura(adventures):
    for data in adventures:
        print(data.get('id_aventura'), data.get('nom'), data.get('descripcio'))

def mostrar_personaje(adventures):
    for data in adventures:
        print(data.get('id_personatge'), data.get('nom'), data.get('descripcio'))

def main():
    user = login()
    if not user:
        return
    while True:
        #menu principal
        print("\n" + "="*50)
        print("MENÚ PRINCIPAL".center(50))
        print("="*50)
        print("1. Jugar Nueva Aventura")
        print("2. Salir")
        
        opcion = input("\n>> Opción: ")
        
        if opcion == "2":
            print("Sesión finalizada.")
            break
        
        elif opcion == "1":
            game(user)
            


if __name__ == "__main__":
    main()