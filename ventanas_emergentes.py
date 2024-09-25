import tkinter as tk
from tkinter import messagebox
class PopupBase:
    def __init__(self, ejercicio):
        self.ejercicio = ejercicio

    def mostrar_popup(self):
        messagebox.showinfo("Popup Base", self.ejercicio)

class CustomPopup(PopupBase):
    def __init__(self, ejercicio):
        super().__init__(ejercicio)

    def mostrar_popup(self):
        messagebox.showinfo("Popup Personalizado", f"ejercio matematico: {self.ejercicio}")

def ejecutar_popup():
    root = tk.Tk()
    root.withdraw()

    # instancia de la clase hija
    popup_personalizado = CustomPopup("124+543")
    popup_personalizado.mostrar_popup()

    # Finalizar el mainloop de tkinter
    root.mainloop()

# Ejecutar el popup personalizado
if __name__ == "__main__":
    ejecutar_popup()
