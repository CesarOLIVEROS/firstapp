import tkinter as tk
from modelo import crear_base_datos
from controlador import Controlador
  

def main(*args, **kargs ):
    # Crear la base de datos y la tabla de usuarios (si no existe)
    crear_base_datos()
    
    # Crear la ventana principal
    root = tk.Tk()
    controlador = Controlador(root)
    
    # Iniciar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()