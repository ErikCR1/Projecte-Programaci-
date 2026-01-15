import mysql.connector

#--------------Conexion----------------
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="erik",
        password="123",
        database="choose_your_story"
    )
#--------------------------------------


#-----------------Login----------------
def login():
    conexion = conectar()

    cursor = conexion.cursor()

    print("-----LOGIN / REGISTRO--------")
    user = input("Introduce tu nombre de usuario: ")
    password = input("Introduce su contraseña: ")

    buscar = "SELECT password FROM usuari WHERE username = %s"
    cursor.execute(buscar, (nom_usuari,))
    resultado = cursor.fetchone()

    if resultado:
        if resultado[0] == contrasenya:
            print(f"S'ha iniciat sessió correctament. Benvingut de nou, {nom_usuari}!")
            return True
        else:
            print("Error: La contrasenya és incorrecta per a aquest usuari.")
            return False
    else:
        print("L'usuari no existeix. Registrant nou usuari...")
        query_insert = "INSERT INTO usuari (username, password) VALUES (%s, %s)"
        try:
            cursor.execute(query_insert, (nom_usuari, contrasenya))
            conexion.commit() 
            print(f"Usuari '{nom_usuari}' creat amb èxit. Ja pots començar!")
            return True
        except Exception as e:
            print(f"Error al registre: {e}")
            return False
    cursor.close()
    conexion.close()
        
#-------------------------------------------------------------------------------------
