import tkinter as tk
from tkinter import messagebox


class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Datos")
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Ingrese información:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Agregar", command=self.add_item)
        self.add_button.pack(pady=5)

        self.listbox = tk.Listbox(root)
        self.listbox.pack(pady=5, fill=tk.BOTH, expand=True)

        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_items)
        self.clear_button.pack(pady=5)

    def add_item(self):
        item = self.entry.get()
        if item:
            self.listbox.insert(tk.END, item)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El campo no puede estar vacío")

    def clear_items(self):
        self.listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
