from funcions import *
import time
def verificador(tamaño, opcion):
    if opcion.isdigit():
        if int(opcion) <= int(tamaño) and int(opcion) > 0:
            return False

    return True    


def game(user): #Esta es la funcion en la que funcionara todo el juego
    id_user = buscar_usuario(user) #usamos la funcion de buscar usuario para encontrar el id del usuario que recordemos que user
    #la funcion de login nos lo devolvio como user:password, ahora al usar esta funcion nos dara su ID
    ingame = True #Empezamos con ingmae en True

    while ingame: #Mientras ingame sea True
        aventuras = get_adventures_with_chars() #la lista que nos devolvera la funcion pasara a ser aventuras
        getFormatedAdventures(aventuras) #Y mostramos de forma bonita la lista con la funcion
        op_aventura = input("Elige aventura: ") #Un input para elegir
        while (verificador(len(aventuras), op_aventura)): #Usamos el verificador para que mientras la funcion sea true se repita 
            print("Has introducido una opcion incorrecta")
            getFormatedAdventures(aventuras)
            op_aventura = input("Elige aventura: ")


        personajes = get_characters() #Esto es lo mismo que antes 
        getFormatedCharacters(personajes)
        op_personaje = input("Elige personaje: ")
        while (verificador(len(aventuras), op_personaje)):
            print("Has introducido una opcion incorrecta")
            getFormatedCharacters(personajes)
            op_personaje = input("Elige personaje: ")
        
        insertCurrentGame(id_user[0], op_aventura, op_personaje) #Aqui usamos la funcion insert con el iduser que hemos sacado antes, la opcion aventura que ha elegido el usuario y la opcion
        partida_actual = get_id_current_game() #partida actual va a pasar a ser la lista de los id de las partidas


        evento = get_answers_bystep_adventure(op_aventura) #ahora evento va a pasar a ser la lista de todos los dialogos con decisiones utilizando op aventura que a la hora de buscar en la funcion simula que es el id_aventura
        fin_partida = 0
        pas = 1
        id_pas = 1
        if int(op_aventura) == 2:
                    id_pas = 20 #20 porque es el primer id que tiene la aventura 2
        while fin_partida == 0: #Mientras fin de partida sea 0 se va a repetir

            nombre_aventura = aventuras[int(op_aventura) - 1].get('nom') #nombre de la aventura va a ser aventuras que recordemos que es la lista de las aventuras que hay
            #con el indice del la opcion de aventura que elegio el usuario y menos uno porque las listas empiezan por 0. Con el .get devolvemos del diccionario el nom
            print("*"*120)
            print(str(nombre_aventura).center(120, "="))
            print("*"*120)
            print()

            print(evento[pas - 1].get('descripcio_text')) #printeamos evento que es la lista de todos los dialogos con decisiones con un indice del pas que ahora es 1 por
            #lo tanto es el primero pero restamos 1 porque las listas empiezan a contar por 0 
            print()
            if int(evento[pas - 1].get('es_final')) == 1: #si el diccionario del evento con el pas 1  es = a 1 se acaba la partida 
                fin_partida = 1
            else: #si no
                decisiones = get_id_bystep_adventure(id_pas) # decisiones pasa a ser la lista de los id de las decisiones que se pueden tomar con el id_pas que depende que aventura hayas escogido o al principio es 20 o 1
                getFormatedAnswers(decisiones)
                opcion_decision = input("Que decision escoges: ")
                while (verificador(len(decisiones), opcion_decision)):
                    print("Opcion no valida: ")
                    getFormatedAnswers(decisiones)
                    opcion_decision = input("Que decision escoges: ")

                insertCurrentChoice(partida_actual[0].get ('id_partida'), evento[int(pas) - 1].get('id_pas'), decisiones[int(opcion_decision) - 1].get('id_opcio'))
                #una vez acabe el bucle significa que ha elegido opciones correctas, por lo que hacemos un insert con la funcion que hemos creado
                #con partidaactual que es la lista de los id con un indice de 0 para sacar la primera partida de la lista, le sacamos el idpartida con get. evento que es la
                #evento con indice pas - 1 y lo mismo con decisiones
                pas = decisiones[int(opcion_decision) - 1].get('id_pas_seguent') # Actualizamos 'pas' con el ID del siguiente paso que viene de la decisión que ha tomado el usuario
                id_pas = pas 

                if int(op_aventura) == 2: 
                    pas -= 19 # Si es la aventura 2, le restamos 19 
                    #al ID para que el número coincida con la posición de nuestra lista, porque si usamos el 20 directamente nos salimos de la lista y da error.
                


        acabar = input("Partida finalizar, quieres seguir jugando ? (1:Si / 2:No)")
        while (verificador(2, acabar)):
            print("Seleciona una opcion correcta: ")
            acabar = input("Partida finalizar, quieres seguir jugando ? (1:Si / 2:No)")

        if int(acabar) == 2:
            ingame = False
        
def getFormatedAdventures(adventures):
    ancho_id = 20    # 12 de texto + 8 espacios de margen
    ancho_nom = 40   # Espacio de sobra para el título
    
    linea_sup = "Adventure".center(120, "=")
    header = "Id Adventure".ljust(ancho_id) + "Adventure".ljust(ancho_nom) + "Description"
    separador = "*" * len(linea_sup)
    
    resultado = linea_sup + "\n\n" + header + "\n" + separador + "\n"
    print (resultado)
    for data in adventures:
        print(str(data.get('id_aventura')).ljust(ancho_id), str(data.get('nom')).ljust(ancho_nom), str(data.get('descripcio')))
        print()

def getFormatedCharacters(adventures):
    ancho_id = 20    # 12 de texto + 8 espacios de margen
    ancho_nom = 40   # Espacio de sobra para el título
    
    linea_sup = "Characters".center(120, "=")
    header = "Id Character".ljust(ancho_id) + "Character".ljust(ancho_nom) + "Description"
    separador = "*" * len(linea_sup)
    
    resultado = linea_sup + "\n\n" + header + "\n" + separador + "\n"
    print (resultado)
    for data in adventures:
        print(str(data.get('id_personatge')).ljust(ancho_id), str(data.get('nom')).ljust(ancho_nom), str(data.get('descripcio')))
        print()

def getFormatedAnswers(decision):    
    i = 1
    for data in decision:
        print(i, ")", data.get('text_resposta'))
        print()
        i += 1

def main(): #la funcion de main va a ser el menu principal
    user = login() #llamamos la funcion login para que el usuario meta sus datos en la variable user
    while not user: #mientras el user sea falso porque el login ha devuelto false entramos en un bucle hasta que lo haga bien 
        print("Contraseña incorrecta")
        user = login()
    while True: #Una vez logeado creamos un bucle infito paara que siempre salga este menu 
        #menu principal
        print("\n" + "="*120)
        print("MENÚ PRINCIPAL".center(120))
        print("="*120)
        print("1. Jugar Nueva Aventura")
        print("2. Salir")
        
        opcion = input("\n>> Opción: ")
        
        if opcion == "2":
            print("Sesión finalizada.") #si la opcion es 2 se hace un break y se acaba
            break
        
        elif opcion == "1":
            game(user) #si la opcion es 1 llamamos a la funcion game con la variable del user
            


if __name__ == "__main__": # Esto sirve para que el menú principal solo se abra si ejecutamos este archivo directamente. Si alguien importa este archivo desde otro sitio, el juego no se lanzará solo.
    main() # Si estamos en el archivo principal, arrancamos el motor del juego.