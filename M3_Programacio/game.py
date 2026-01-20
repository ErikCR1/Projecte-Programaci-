ogramacio\game.py
@@ -1,113 +0,0 @@
#Fabian: Motor de juego, bucle incial y toma de desciciones 

from funciones import *
import time

def main():
    if not login():
        return
    while True:
        #menu principal
        print("\n" + "="*50)
        print("          MENÚ PRINCIPAL")
        print("="*50)
        print("1. Jugar Nueva Aventura")
        print("2. Salir")
        
        opcion = input("\n>> Opción: ")
        
        if opcion == "2":
            print("Sesión finalizada.")
            break
        
        elif opcion == "1":
            #configuracion partida
            
            #seleccon de aventura
            aventuras = get_adventures_with_chars()
            if not aventuras:
                print(">> Error: No se encontraron aventuras.")
                continue
                
            print("\n--- AVENTURAS DISPONIBLES ---")
            for id_adv, datos in aventuras.items():
                print(f"ID [{id_adv}]: {datos['nom']}")
                print(formatText(datos['descripcio'], 80))
                print("-" * 20)
                
            try:
                id_seleccion = int(input("\n>> ID Aventura: "))
                if id_seleccion not in aventuras:
                    print("ID no válido.")
                    continue
                game_context['idAdventure'] = id_seleccion
            except ValueError:
                print("Entrada inválida.")
                continue

            #selección de Personaje
            personajes = get_characters()
            print("\n--- SELECCIÓN DE PERSONAJE ---")
            for i, p in enumerate(personajes):
                print(f"{i+1}) {p['nom']} - {p['descripcio']}")
                
            try:
                p_sel = int(input("\n>> Nº Personaje: "))
                if 1 <= p_sel <= len(personajes):
                    char_elegido = personajes[p_sel - 1]
                    game_context['idCharacter'] = char_elegido['id_personatge']
                    print(f"\n>> Personaje seleccionado: {char_elegido['nom']}")
                else:
                    print("Selección inválida.")
                    continue
            except ValueError:
                continue

            #inicializacion
            insertCurrentGame()
            print("\n>> Inicializando partida...")
            time.sleep(1)
            print("\n" + "#"*50)
            print("      INICIO DE LA AVENTURA")
            print("#"*50 + "\n")

            #blucle game
            
            current_step_id = get_first_step_adventure(game_context['idAdventure'])
            
            if not current_step_id:
                print("Error crítico: Aventura sin pasos definidos.")
                continue

            while True:
                #recuperacion de datos del paso
                step_data = get_step_data(current_step_id)
                
                #renderizado
                print("\n" + formatText(step_data['descripcio_text'], 100))
                
                #condicion victoria/derrota
                if step_data['es_final']:
                    print("\n" + "="*30)
                    print("       FIN DE LA PARTIDA")
                    print("="*30)
                    input("\n(Presiona Enter para continuar)")
                    break
                
                #gestion opciones
                opciones = get_answers_bystep_adventure(current_step_id)
                
                if not opciones:
                    print("\n>> Error de lógica: Paso no final sin opciones.")
                    break

                #input usuario persistencia
                eleccion = getOpt(opciones)
                insertCurrentChoice(current_step_id, eleccion['id_opcio'])
                
                #avance estado
                current_step_id = eleccion['id_pas_seguent']

if __name__ == "__main__":
    main()