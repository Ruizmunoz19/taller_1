import tkinter as tk
from tkinter import messagebox

class InfoPopup:
    def __init__(self, mensaje_info):
        self.mensaje_info = mensaje_info

    def mostrar_info(self):
        messagebox.showinfo("Información", self.mensaje_info)

class WarningPopup:
    def __init__(self, mensaje_warning):
        self.mensaje_warning = mensaje_warning

#MENSAJES YA PERSONALIZADO DE ADVERTENCIA Y DE INFORMACIÓN.
    def mostrar_advertencia(self):
        messagebox.showwarning("ADVETENCIA 🚨", self.mensaje_warning)

class CombinedPopup(InfoPopup, WarningPopup):
    def __init__(self, mensaje_info, mensaje_warning):
        InfoPopup.__init__(self, mensaje_info)
        WarningPopup.__init__(self, mensaje_warning)

    def mostrar_ambos_mensajes(self):
        self.mostrar_info()
        self.mostrar_advertencia()

def ejecutar_popup():
    root = tk.Tk()
    root.withdraw()

    #  clase hija CombinedPopup
    popup_combinado = CombinedPopup("Mensaje De Precaución.", "PELIGRO NO ENTRAR")
    popup_combinado.mostrar_ambos_mensajes()
    root.mainloop()


if __name__ == "__main__":
    ejecutar_popup()
