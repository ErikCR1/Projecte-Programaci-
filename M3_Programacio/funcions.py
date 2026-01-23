import mysql.connector

#--------------Conexion----------------  
def conectar(): #Creamos una funcion para conectarse a la base de datos
    return mysql.connector.connect(
        host="127.0.0.1", #El host 
        port=3308, #El puerto del servidor
        user="super", #El usuario
        password="1234", # La contraseña
        database="choose_your_story" #Y la base de datos que vayamos a usar
    )
#--------------------------------------

def buscar_usuario(query): #Con esta funcion lo que queremos es sacar el id del usuario para luego poder printearlo por pantalla
    conexion = conectar()
    cursor = conexion.cursor()

    a, b = str(query).split(";") #Como guardamos una variable string con el user y la contra con un ; vamos hacer que a sea el user y b la contra
    #y con el split rompemos el;
    buscar = "SELECT id_usuari FROM usuari WHERE username = %s and password = %s" #buscamos el id usuario de la tabla usuario donde user sea como el valor a y password como el valor b
    cursor.execute(buscar, (a,b))
    resultado = cursor.fetchone() #recogemos solo una linea que coincida
    cursor.close()
    conexion.close()
    return resultado #y la devolvemos

#-----------------Login----------------
def login(): #Creamos una funcion para poder logearse
    conexion = conectar() 
    #Siempre antes de empezar algo donde necesitemos hacer algo con la bdd creamos una variable que sea conexion y sea igual a la funcion conectar

    cursor = conexion.cursor() #Creamos un cursor que nos servira para selecionar y executar cosas en especificos de la tabla
    print("-"*120)
    print("LOGIN / REGISTRO".center(120))
    print("-"*120)
    user = input("Introduce tu nombre de usuario: ")
    password = input("Introduce su contraseña: ")

    buscar = "SELECT password FROM usuari WHERE username = %s" #Creamos una variable que es buscar y con comandos de sql selecionamos la contraseña
    #de la tabla de usuarios donde username sea igual al valor dado que pondremos ahora

    cursor.execute(buscar, (user,)) #ahora con el cursor de antes hacemos un execute para decir que con la variable de antes buscar haga el selct y el valor de %s es user
    resultado = cursor.fetchone() # Hacemos una variable resultado donde el cursor apunta a solo la primera fila que coincide.
    #Como en este caso buscas por username (que debería ser único), solo te interesa que te traiga esa fila específica.
    # Intentamos pillar la contra del usuario que nos han dado.
    
    string =  f"{user};{password}" #Creamos un string con el usuario y la contraseña para la funcion de arriba
    
    if resultado: #Si resultado existe entonces: # Si hemos encontrado algo (significa que el usuario existe), entramos a chequear la contra
        if resultado[0] == password: #vuelve a mirar si el resultado que es la contraseña es igual a la contra que nos han dado
            print(f"S'ha iniciat sessió correctament. Benvingut de nou, {user}!")
            input("Enter para continuar...")
            return string #si es que si nos devuelve el string que hemos echo antes
        else:
            print("Error: La contrasenya és incorrecta per a aquest usuari.") #si la contraseña no es igual devuelve false
            return False 
    else: #Si resultado está vacío (significa que el usuario no existe en la bdd), nos ponemos a registrarlo como nuevo.
        print("L'usuari no existeix. Registrant nou usuari...")
        query_insert = "INSERT INTO usuari (username, password) VALUES (%s, %s)" #creamos una variable de insert escribimos comando de sql donde dice que 
        #en la tabla usuari especialmente y username y password le añadimos los valores dados que son %S que ahora se ponen 

        try: #hacemos la prueba
            cursor.execute(query_insert, (user, password)) #apuntamos a una ejecutacion donde la variable creada añade esos valores sustituyendo %s
            conexion.commit() #se hace un commit
            print(f"Usuari '{user}' creat amb èxit.")
            input("Enter para continuar...")
            
            # CIERRA AQUÍ
            cursor.close()
            conexion.close()
            return string
        
        except Exception as e: #Si no lo logra devuelve false
            # Y AQUÍ TAMBIÉN POR SI HAY ERROR
            cursor.close()
            conexion.close()
            return False
        
def get_adventures_with_chars(): #Creamos una funcion para sacar las aventuras de la bdd
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True) #al añadir dictionary estamos haciendo que nos lo devuelva en forma de dicionario para luego trabajar con ellos


    cursor.execute("SELECT id_aventura, nom, descripcio FROM aventura") 
    
    lista = cursor.fetchall() #hacemos una variable donde sacara TODAS las filas que encuentre en la tabla, distinto a fetchone que solo saca la primera fila (usada en el login)
    cursor.close()
    conexion.close()
    return lista #cerramos para no gastar recursos y que no de errores y devolvemos la lista que tenemos de todos los diccionarios

def insertCurrentGame(id_usuari, id_personatge, id_aventura): #Esta funcion la vamos a usar para insertar los id de las partidas

    conexion = conectar()
    cursor = conexion.cursor()

    query_insert = "INSERT INTO partida (id_usuari, id_personatge, id_aventura) VALUES (%s, %s, %s)" #query insert  va ser un instert en la tabla partida de los id con los valores siguientes
    try:
        cursor.execute(query_insert, (id_usuari, id_personatge, id_aventura)) #los valores son las variables que pondremos en game.py
        conexion.commit()  #un commit y un aviso de que hemos creado
        print(f"Partida creada amb exit.")
            

        cursor.close()
        conexion.close()
        return True #si sale bien devuelve un true
        
    except Exception as e:
        print(e)
        cursor.close()
        conexion.close()
        return False #si sale mal que imprima el error y un false

#INSERT DE DECISIONES & EVENTOS
def insertCurrentChoice(id_partida, id_pas, id_opcio_triada):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    query_insert = "INSERT INTO decisio_partida (id_partida, id_pas, id_opcio_triada) VALUES (%s, %s, %s)"

    try:
        cursor.execute(query_insert, (id_partida, id_pas, id_opcio_triada))
        conexion.commit()

        cursor.close()
        conexion.close()
        return True

    except Exception as e:
        print(e)
        cursor.close()
        conexion.close()
        return False




def get_characters():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT id_personatge, nom, descripcio FROM personatge")
    
    lista = cursor.fetchall()
    cursor.close()
    conexion.close()
    return lista


def get_answers_bystep_adventure(opcion):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    print("Comenzant la historia", opcion, "...")
    input("Enter para continuar...")
    query = "SELECT * FROM pas WHERE id_aventura = %s"
    cursor.execute(query, (opcion,))
    
    lista = cursor.fetchall()
    cursor.close()
    conexion.close()
    return lista

def get_id_bystep_adventure(opcion):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    query = "SELECT * FROM opcio WHERE id_pas_actual = %s"
    cursor.execute(query, (opcion,))
    
    lista = cursor.fetchall()
    cursor.close()
    conexion.close()
    return lista

def get_id_current_game():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    query = "SELECT id_partida FROM partida ORDER BY Id_partida DESC LIMIT 1;"
    cursor.execute(query)
    
    lista = cursor.fetchall()
    cursor.close()
    conexion.close()
    return lista
#-------------------------------------------------------------------------------------

