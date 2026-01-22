import mysql.connector

#--------------Conexion----------------
def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3308,
        user="super",
        password="1234",
        database="choose_your_story"
    )
#--------------------------------------

def buscar_usuario(query):
    conexion = conectar()
    cursor = conexion.cursor()

    a, b = str(query).split(";")
    buscar = "SELECT id_usuari FROM usuari WHERE username = %s and password = %s"
    cursor.execute(buscar, (a,b))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()
    return resultado

#-----------------Login----------------
def login():
    conexion = conectar()

    cursor = conexion.cursor()
    print("-"*120)
    print("LOGIN / REGISTRO".center(120))
    print("-"*120)
    user = input("Introduce tu nombre de usuario: ")
    password = input("Introduce su contraseña: ")

    buscar = "SELECT password FROM usuari WHERE username = %s"
    cursor.execute(buscar, (user,))
    resultado = cursor.fetchone()
    
    string =  f"{user};{password}"
    
    if resultado:
        if resultado[0] == password:
            print(f"S'ha iniciat sessió correctament. Benvingut de nou, {user}!")
            input("Enter para continuar...")
            return string
        else:
            print("Error: La contrasenya és incorrecta per a aquest usuari.")
            return False
    else:
        print("L'usuari no existeix. Registrant nou usuari...")
        query_insert = "INSERT INTO usuari (username, password) VALUES (%s, %s)"
        try:
            cursor.execute(query_insert, (user, password))
            conexion.commit() 
            print(f"Usuari '{user}' creat amb èxit.")
            input("Enter para continuar...")
            
            # CIERRA AQUÍ
            cursor.close()
            conexion.close()
            return string
        
        except Exception as e:
            # Y AQUÍ TAMBIÉN POR SI HAY ERROR
            cursor.close()
            conexion.close()
            return False
        
def get_adventures_with_chars():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)


    cursor.execute("SELECT id_aventura, nom, descripcio FROM aventura")
    
    lista = cursor.fetchall()
    cursor.close()
    conexion.close()
    return lista

def insertCurrentGame(id_usuari, id_personatge, id_aventura):

    conexion = conectar()
    cursor = conexion.cursor()

    query_insert = "INSERT INTO partida (id_usuari, id_personatge, id_aventura) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query_insert, (id_usuari, id_personatge, id_aventura))
        conexion.commit() 
        print(f"Partida creada amb exit.")
            

        cursor.close()
        conexion.close()
        return True
        
    except Exception as e:
        print(e)
        cursor.close()
        conexion.close()
        return False

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

