import sqlite3

def crear_base_datos():
    """
    Crea la base de datos 'usuarios.db' si no existe y una tabla de usuarios.
    La tabla tiene tres columnas: id (clave primaria autoincrementable), 
    username (único y no nulo), y password (no nulo).
    """
    try:
        with sqlite3.connect("usuarios.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY,
                                username TEXT UNIQUE NOT NULL,
                                password TEXT NOT NULL
                            )''')
            conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al interactuar con la base de datos: {e}")

# Función para agregar un usuario a la base de datos
def agregar_usuario(username, password):
    try:
        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al insertar el usuario: {e}")
    finally:
        conexion.close()

# Función para verificar si las credenciales son correctas
def verificar_usuario(username, password):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    # Buscar el usuario en la base de datos
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado is not None  # Retorna True si las credenciales son correctas

