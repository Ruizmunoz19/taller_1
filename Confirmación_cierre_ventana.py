import tkinter as tk
from tkinter import messagebox

class ErrorPopup:
    def __init__(self, mensaje_no_corre):
        self.mensaje_no_corre = mensaje_no_corre

    def mostrar_error(self):
        messagebox.showerror("no corre", self.mensaje_error)


# Clase hija
class CustomErrorPopup(ErrorPopup):
    def __init__(self, mensaje_no_corre):
        super().__init__(mensaje_no_corre)
    def mostrar_error(self):
        # Mostrar    error modificado
        messagebox.showerror("no da nada", f"no_corre: {self.mensaje_no_corre}")
def ejecutar_popup():
    root = tk.Tk()
    root.withdraw()

    popup_personalizado = CustomErrorPopup("no_corre ")
    popup_personalizado.mostrar_error()


    root.mainloop()


# Ejecutar el popup personalizado
if __name__ == "__main__":
    ejecutar_popup()
