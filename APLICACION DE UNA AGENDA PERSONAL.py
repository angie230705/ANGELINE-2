import tkinter as tk
from tkinter import ttk  # Importamos ttk para Treeview y estilos modernos
from tkinter import messagebox  # Importamos messagebox para diálogos de confirmación
from tkcalendar import DateEntry  # Importamos DateEntry de tkcalendar para la selección de fechas

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")  # Establecemos el título de la ventana principal

        # Contenedores (Frames) para organizar la interfaz
        self.frame_eventos = tk.Frame(root)  # Frame para la lista de eventos
        self.frame_eventos.pack(pady=10)  # Añadimos padding vertical

        self.frame_entradas = tk.Frame(root)  # Frame para las entradas de datos
        self.frame_entradas.pack(pady=5)  # Añadimos padding vertical

        self.frame_botones = tk.Frame(root)  # Frame para los botones de acción
        self.frame_botones.pack(pady=10)  # Añadimos padding vertical

        # TreeView para mostrar eventos en forma de tabla
        self.tree = ttk.Treeview(self.frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")  # Encabezado de la columna Fecha
        self.tree.heading("Hora", text="Hora")  # Encabezado de la columna Hora
        self.tree.heading("Descripción", text="Descripción")  # Encabezado de la columna Descripción
        self.tree.pack()  # Empaquetamos el Treeview

        # Entradas de datos para fecha, hora y descripción
        tk.Label(self.frame_entradas, text="Fecha:").grid(row=0, column=0)  # Etiqueta para la fecha
        self.fecha_entry = DateEntry(self.frame_entradas, width=12, background='darkblue', foreground='white', borderwidth=2)  # Entrada de fecha con DateEntry
        self.fecha_entry.grid(row=0, column=1)  # Posicionamos la entrada de fecha

        tk.Label(self.frame_entradas, text="Hora:").grid(row=1, column=0)  # Etiqueta para la hora
        self.hora_entry = tk.Entry(self.frame_entradas, width=15)  # Entrada de texto para la hora
        self.hora_entry.grid(row=1, column=1)  # Posicionamos la entrada de hora

        tk.Label(self.frame_entradas, text="Descripción:").grid(row=2, column=0)  # Etiqueta para la descripción
        self.descripcion_entry = tk.Entry(self.frame_entradas, width=30)  # Entrada de texto para la descripción
        self.descripcion_entry.grid(row=2, column=1)  # Posicionamos la entrada de descripción

        # Botones para agregar, eliminar y salir
        tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0)  # Botón para agregar evento
        tk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1)  # Botón para eliminar evento
        tk.Button(self.frame_botones, text="Salir", command=root.quit).grid(row=0, column=2)  # Botón para salir de la aplicación

    def agregar_evento(self):
        # Función para agregar un evento a la lista
        fecha = self.fecha_entry.get()  # Obtenemos la fecha seleccionada
        hora = self.hora_entry.get()  # Obtenemos la hora ingresada
        descripcion = self.descripcion_entry.get()  # Obtenemos la descripción ingresada
        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))  # Insertamos el evento en el Treeview

    def eliminar_evento(self):
        # Función para eliminar un evento seleccionado
        seleccion = self.tree.selection()  # Obtenemos el elemento seleccionado en el Treeview
        if not seleccion:  # Si no hay nada seleccionado
            messagebox.showerror("Error", "Selecciona un evento para eliminar.")  # Mostramos un mensaje de error
            return  # Salimos de la función

        if messagebox.askyesno("Confirmar", "¿Eliminar el evento seleccionado?"):  # Mostramos un diálogo de confirmación
            self.tree.delete(seleccion)  # Eliminamos el evento seleccionado

if __name__ == "__main__":
    root = tk.Tk()  # Creamos la ventana principal
    app = AgendaPersonal(root)  # Creamos una instancia de la clase AgendaPersonal
    root.mainloop()  # Iniciamos el bucle principal de la aplicación



