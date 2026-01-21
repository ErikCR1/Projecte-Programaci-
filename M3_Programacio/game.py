from funcions import *
import time
def verificador(tamaño, opcion):
    if opcion.isdigit():
        if int(opcion) <= int(tamaño) and int(opcion) > 0:
            return False

    return True    


def game(user):
    id_user = buscar_usuario(user)
    ingame = True

    while ingame:
        aventuras = get_adventures_with_chars()
        mostrar_aventura(aventuras)
        op_aventura = input("Elige aventura: ")
        while (verificador(len(aventuras), op_aventura)):
            print("Has introducido una opcion incorrecta")
            mostrar_aventura(aventuras)
            op_aventura = input("Elige aventura: ")


        personajes = get_characters()
        mostrar_personaje(personajes)
        op_personaje = input("Elige personaje: ")
        while (verificador(len(aventuras), op_personaje)):
            print("Has introducido una opcion incorrecta")
            mostrar_personaje(personajes)
            op_personaje = input("Elige personaje: ")
        
        insertCurrentGame(id_user[0], op_aventura, op_personaje)
        partida_actual = get_id_current_game()


        evento = get_answers_bystep_adventure(op_aventura)
        fin_partida = 0
        pas = 1
        id_pas = 1
        if int(op_aventura) == 2:
                    id_pas = 20
        while fin_partida == 0:
            print(evento[pas - 1].get('descripcio_text'))
            if int(evento[pas - 1].get('es_final')) == 1:
                fin_partida = 1
            else:
                decisiones = get_id_bystep_adventure(id_pas)
                mostrar_decisiones(decisiones)
                opcion_decision = input("Que decision escoges: ")
                while (verificador(len(decisiones), opcion_decision)):
                    print("Opcion no valida: ")
                    mostrar_decisiones(decisiones)
                    opcion_decision = input("Que decision escoges: ")

                insertCurrentChoice(partida_actual[0].get ('id_partida'), evento[int(pas) - 1].get('id_pas'), decisiones[int(opcion_decision) - 1].get('id_opcio'))
                pas = decisiones[int(opcion_decision) - 1].get('id_pas_seguent')
                id_pas = pas 

                if int(op_aventura) == 2:
                    pas -= 19
                


        acabar = input("Partida finalizar, quieres seguir jugando ? (1:Si / 2:No)")
        while (verificador(2, acabar)):
            print("Seleciona una opcion correcta: ")
            acabar = input("Partida finalizar, quieres seguir jugando ? (1:Si / 2:No)")

        if int(acabar) == 2:
            ingame = False
        
def mostrar_aventura(adventures):
    for data in adventures:
        print(str(data.get('id_aventura')).ljust(10), str(data.get('nom')).ljust(10), str(data.get('descripcio')).ljust(10))

def mostrar_personaje(adventures):
    for data in adventures:
        print(data.get('id_personatge'), data.get('nom'), data.get('descripcio'))

def mostrar_decisiones(decision):
    i = 1
    for data in decision:
        print(i, data.get('text_resposta'))
        i += 1

def main():
    user = login()
    while not user:
        print("Contraseña incorrecta")
        user = login()
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