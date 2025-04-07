import tkinter as tk
from tkinter import ttk, messagebox

class ListaTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas Pendientes")

        self.tareas = []

        # Campo de entrada para añadir nuevas tareas
        self.nueva_tarea_entry = ttk.Entry(root, width=40)
        self.nueva_tarea_entry.pack(pady=5, padx=10)
        self.nueva_tarea_entry.bind("<Return>", self.agregar_tarea_teclado)

        # Frame para los botones de acción
        botones_frame = ttk.Frame(root)
        botones_frame.pack(pady=5)

        self.agregar_button = ttk.Button(botones_frame, text="Añadir Tarea", command=self.agregar_tarea)
        self.agregar_button.pack(side=tk.LEFT, padx=5)

        self.completar_button = ttk.Button(botones_frame, text="Completar", command=self.marcar_como_completada)
        self.completar_button.pack(side=tk.LEFT, padx=5)

        self.eliminar_button = ttk.Button(botones_frame, text="Eliminar", command=self.eliminar_tarea)
        self.eliminar_button.pack(side=tk.LEFT, padx=5)

        # Lista de tareas
        self.tareas_list = tk.Listbox(root, width=60, height=15)
        self.tareas_list.pack(pady=10, padx=10)
        self.actualizar_lista()

        # Atajos de teclado
        root.bind("<Escape>", self.cerrar_aplicacion)
        root.bind("<c>", self.marcar_como_completada_teclado)
        root.bind("<Delete>", self.eliminar_tarea_teclado)
        root.bind("<d>", self.eliminar_tarea_teclado) # Otro atajo para eliminar

    def agregar_tarea(self):
        tarea = self.nueva_tarea_entry.get().strip()
        if tarea:
            self.tareas.append({"tarea": tarea, "completada": False})
            self.nueva_tarea_entry.delete(0, tk.END)
            self.actualizar_lista()

    def agregar_tarea_teclado(self, event):
        self.agregar_tarea()

    def marcar_como_completada(self):
        seleccion_indices = self.tareas_list.curselection()
        if seleccion_indices:
            indice = seleccion_indices[0]
            if 0 <= indice < len(self.tareas):
                self.tareas[indice]["completada"] = True
                self.actualizar_lista()

    def marcar_como_completada_teclado(self, event):
        self.marcar_como_completada()

    def eliminar_tarea(self):
        seleccion_indices = self.tareas_list.curselection()
        if seleccion_indices:
            indice = seleccion_indices[0]
            if 0 <= indice < len(self.tareas):
                tarea_a_eliminar = self.tareas[indice]["tarea"]
                confirmacion = messagebox.askyesno("Confirmar", f"¿Seguro que desea eliminar la tarea: '{tarea_a_eliminar}'?")
                if confirmacion:
                    del self.tareas[indice]
                    self.actualizar_lista()

    def eliminar_tarea_teclado(self, event):
        self.eliminar_tarea()

    def actualizar_lista(self):
        self.tareas_list.delete(0, tk.END)
        for tarea_data in self.tareas:
            tarea_texto = tarea_data["tarea"]
            if tarea_data["completada"]:
                tarea_texto = f"[Completada] {tarea_texto}"
                self.tareas_list.itemconfig(tk.END, fg="gray")
            self.tareas_list.insert(tk.END, tarea_texto)

    def cerrar_aplicacion(self, event):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareas(root)
    root.mainloop()