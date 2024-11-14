import tkinter as tk
from tkinter import messagebox, Frame


class VistaLogin:

    def __init__(self, master, controlador):
        
        self.master = master
        self.master.title("Inicio de Sesión")
        self.master.geometry("500x200")
        self.controlador = controlador
        
        # Crear un Frame que se centrará en la ventana
        self.frame = tk.Frame(self.master)
        
        # Centrar el frame
        self.frame.place(relx=0.5, rely=0.5, anchor="center")  
        # Crear los elementos del formulario de login
        self.label_usuario = tk.Label(self.frame, text="Usuario:",  font=("Arial",11, "bold"))
        self.label_usuario.grid(row=0, column=2, padx=10, pady=10)

        self.entry_usuario = tk.Entry(self.frame)
        self.entry_usuario.grid(row=0, column=3, padx=10, pady=10)
        
        self.label_password = tk.Label(self.frame, text="Contraseña:", font=("Arial", 11, "bold"))
        self.label_password.grid(row=1, column=2, padx=10, pady=10)
        
        self.entry_password = tk.Entry(self.frame, show="*")
        self.entry_password.grid(row=1, column=3, padx=10, pady=10)
        
        
        self.boton_login = tk.Button(self.frame, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_login.grid(row=2, column=3,padx=10,  pady=20)


    def iniciar_sesion(self):
        """ Método que ejecutará el controlador para verificar las credenciales. """
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        self.controlador.validar_login(usuario, password)  # Llamamos al método del controlador directamente

class VistaPrincipal:
    def __init__(self, master, controlador):
        self.master = master
        self.controlador =controlador
        self.master.title("Ventana Principal")
        self.master.geometry("400x300")
            
        self.label_bienvenida = tk.Label(master, text="Bienvenido a la aplicación!", font=("Arial", 16))
        self.label_bienvenida.pack(pady=50)
            
        self.boton_salir = tk.Button(master, text="Cerrar Sesión", command=self.salir)
        self.boton_salir.pack(pady=20)

    def salir(self):
        """ Método para cerrar la ventana principal. """
        self.master.quit()
