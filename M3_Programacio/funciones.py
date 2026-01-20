import mysql.connector

# Variables globales de contexto
game_context = {
    'idUser': None,
    'username': None,
    'idAdventure': None,
    'idCharacter': None,
    'idGame': None
}

def conectar():
    """Establece conexión con la base de datos."""
    return mysql.connector.connect(
        host="localhost",
        user="erik",        # Configurar credenciales
        password="123",     
        database="choose_your_story"
    )

def login():
    """Gestiona la autenticación y registro de usuarios."""
    conexion = conectar()
    cursor = conexion.cursor()

    print("\n" + "*"*40)
    print("      CHOOSE YOUR STORY - LOGIN")
    print("*"*40)
    
    while True:
        user = input("Usuario: ")
        password = input("Contraseña: ")

        # Verificación de credenciales
        query = "SELECT id_usuari, password FROM usuari WHERE username = %s"
        cursor.execute(query, (user,))
        resultado = cursor.fetchone()

        if resultado:
            db_id, db_pass = resultado
            if db_pass == password:
                print(f"\n>> Bienvenido, {user}!")
                game_context['idUser'] = db_id
                game_context['username'] = user
                cursor.close()
                conexion.close()
                return True
            else:
                print(">> Contraseña incorrecta.")
        else:
            # Registro de nuevo usuario
            print(">> Usuario no encontrado. Creando cuenta...")
            try:
                query_insert = "INSERT INTO usuari (username, password) VALUES (%s, %s)"
                cursor.execute(query_insert, (user, password))
                conexion.commit()
                game_context['idUser'] = cursor.lastrowid
                game_context['username'] = user
                print(f">> Usuario '{user}' registrado correctamente.")
                cursor.close()
                conexion.close()
                return True
            except Exception as e:
                print(f">> Error en registro: {e}")

# --- Acceso a Datos ---

def get_adventures_with_chars():
    """Recupera todas las aventuras disponibles."""
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id_aventura, nom, descripcio FROM aventura")
    result = cursor.fetchall()
    conn.close()
    
    adventures = {}
    for row in result:
        adventures[row['id_aventura']] = row
    return adventures

def get_characters():
    """Recupera lista de personajes."""
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id_personatge, nom, descripcio FROM personatge")
    result = cursor.fetchall()
    conn.close()
    return result

def get_first_step_adventure(id_aventura):
    """Obtiene el ID del paso inicial de la aventura."""
    conn = conectar()
    cursor = conn.cursor()
    query = "SELECT id_pas FROM pas WHERE id_aventura = %s ORDER BY id_pas ASC LIMIT 1"
    cursor.execute(query, (id_aventura,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def get_step_data(id_pas):
    """Obtiene descripción y estado (final) del paso actual."""
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT descripcio_text, es_final FROM pas WHERE id_pas = %s"
    cursor.execute(query, (id_pas,))
    step = cursor.fetchone()
    conn.close()
    return step

def get_answers_bystep_adventure(id_pas):
    """Recupera opciones disponibles para el paso actual."""
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT id_opcio, text_resposta, id_pas_seguent FROM opcio WHERE id_pas_actual = %s"
    cursor.execute(query, (id_pas,))
    answers = cursor.fetchall()
    conn.close()
    return answers

def insertCurrentGame():
    """Registra el inicio de una nueva partida."""
    conn = conectar()
    cursor = conn.cursor()
    query = """
        INSERT INTO partida (id_usuari, id_personatge, id_aventura, data_inici) 
        VALUES (%s, %s, %s, NOW())
    """
    vals = (game_context['idUser'], game_context['idCharacter'], game_context['idAdventure'])
    cursor.execute(query, vals)
    conn.commit()
    game_context['idGame'] = cursor.lastrowid
    conn.close()

def insertCurrentChoice(id_pas, id_opcio):
    """Registra la decisión tomada por el usuario."""
    conn = conectar()
    cursor = conn.cursor()
    query = "INSERT INTO decisio_partida (id_partida, id_pas, id_opcio_triada) VALUES (%s, %s, %s)"
    cursor.execute(query, (game_context['idGame'], id_pas, id_opcio))
    conn.commit()
    conn.close()

# --- Utilidades Visuales ---

def formatText(text, lenLine=100):
    """Formatea texto a un ancho fijo sin cortar palabras."""
    palabras = text.split(' ')
    lineas = []
    linea_actual = ""
    
    for palabra in palabras:
        if len(linea_actual) + len(palabra) + 1 <= lenLine:
            linea_actual += palabra + " "
        else:
            lineas.append(linea_actual)
            linea_actual = palabra + " "
    lineas.append(linea_actual)
    return "\n".join(lineas)

def getOpt(options):
    """Muestra menú de opciones y valida la entrada del usuario."""
    print("\n" + "-"*30)
    for i, opt in enumerate(options):
        print(f"{i + 1}) {opt['text_resposta']}")
    print("-"*30)
    
    while True:
        try:
            eleccion = int(input("\n>> Elige tu destino (número): "))
            if 1 <= eleccion <= len(options):
                return options[eleccion - 1]
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Entrada inválida. Introduzca un número.")