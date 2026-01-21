import mysql.connector

#--------------Conexion----------------
def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3308,
        user="admin",
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

    print("-----LOGIN / REGISTRO--------")
    user = input("Introduce tu nombre de usuario: ")
    password = input("Introduce su contraseña: ")

    buscar = "SELECT password FROM usuari WHERE username = %s"
    cursor.execute(buscar, (user,))
    resultado = cursor.fetchone()
    
    string =  f"{user};{password}"
    
    if resultado:
        if resultado[0] == password:
            print(f"S'ha iniciat sessió correctament. Benvingut de nou, {user}!")
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
            
            # CIERRA AQUÍ
            cursor.close()
            conexion.close()
            return string
        
        except Exception as e:
            # Y AQUÍ TAMBIÉN POR SI HAY ERROR
            cursor.close()
            conexion.close()
            return False
        
def cargar_aventura():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    print ("----AVENTURAS DISPONIBLES----")
    cursor.execute("SELECT id_aventura, nom, descripcio FROM aventura")
    
    lista = cursor.fetchall()
    cursor.close()
    conexion.close()
    return lista

def insert_partida(id_usuari, id_personatge, id_aventura):

    conexion = conectar()
    cursor = conexion.cursor()

    query_insert = "INSERT INTO partida (id_usuari, id_personatge, id_aventura) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query_insert, (id_usuari, id_personatge, id_aventura))
        conexion.commit() 
        print(f"Partida creada amb exit.")
            
            # CIERRA AQUÍ
        cursor.close()
        conexion.close()
        return True
        
    except Exception as e:
        # Y AQUÍ TAMBIÉN POR SI HAY ERROR
        cursor.close()
        conexion.close()
        return False



def cargar_personaje():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    print ("----Personajes DISPONIBLES----")
    cursor.execute("SELECT id_personatge, nom, descripcio FROM personatge")
    
    lista = cursor.fetchall()
    cursor.close()
    conexion.close()
    return lista


def cargar_eventos(opcion):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    print("Comenzant la historia", opcion, "...")
    query = "SELECT * FROM pas WHERE id_aventura = %s"
    cursor.execute(query, (opcion,))
    
    lista = cursor.fetchall()
    cursor.close()
    conexion.close()
    return lista

def cargar_decisiones(opcion):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    query = "SELECT * FROM opcio WHERE id_pas_actual = %s"
    cursor.execute(query, (opcion,))
    
    lista = cursor.fetchall()
    cursor.close()
    conexion.close()
    return lista


#-------------------------------------------------------------------------------------