from modelo import verificar_usuario
from vistas import VistaLogin
from vistas import VistaPrincipal
from tkinter import messagebox

class Controlador:
    def __init__(self, master):
        self.master = master
        self.vista_login = VistaLogin(master,self)
        self.vista_principal = None
        
           
       
    def validar_login(self, usuario, password):
        """ Método que valida las credenciales """
        if verificar_usuario(usuario, password):
            self.mostrar_ventana_principal()
        else:
            self.mostrar_error("Credenciales incorrectas.")
    
    def mostrar_ventana_principal(self):
        """ Método que muestra la ventana principal después de un login exitoso """
        if not self.vista_principal:
            self.vista_principal = VistaPrincipal(self.master, self)
            self.vista_principal.master.deiconify() # Mostrar la ventana principal
            #self.vista_login.master.withdraw()  # Ocultar la ventana de login
    
    def mostrar_error(self, mensaje):
        """ Método para mostrar un mensaje de error al usuario """
        messagebox.showerror("Error", mensaje)