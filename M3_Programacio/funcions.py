import mysql.connector

#--------------Conexion----------------
def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3307,
        user="super",
        password="1234",
        database="choose_your_story"
    )
#--------------------------------------

#---------Menu---------------------
def menu(options):
    print("CHOOSE YOUR STORY".center)



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

    if resultado:
        if resultado[0] == password:
            print(f"S'ha iniciat sessió correctament. Benvingut de nou, {user}!")
            return True
        else:
            print("Error: La contrasenya és incorrecta per a aquest usuari.")
            return False
    else:
        print("L'usuari no existeix. Registrant nou usuari...")
        query_insert = "INSERT INTO usuari (username, password) VALUES (%s, %s)"
        try:
            cursor.execute(query_insert, (user, password))
            conexion.commit() 
            print(f"Usuari '{user}' creat amb èxit. Ja pots començar!")
            return True
        except Exception as e:
            print(f"Error al registre: {e}")
            return False
    cursor.close()
    conexion.close()
        
    
def personatge_aventura():
    conexion = conectar()
    
    cursor = conexion.cursor()
    
    print ("-----SELECCIÓN DE PERSONAJES-------")
    cursor.execute("SELECT id_personatge, nom, descripcio FROM personatge")
    
    
#-------------------------------------------------------------------------------------
